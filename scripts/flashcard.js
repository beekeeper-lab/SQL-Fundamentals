/* Web Flashcard runtime ----------------------------------------------------
 *
 * Aggregates every quiz question in a course into one shuffleable bank, with
 * spaced-repetition weighting persisted in localStorage. Vanilla JS, no deps.
 *
 * Required DOM:
 *   <script type="application/json" id="flashcard-data">{ ... }</script>
 *   <div id="flashcard-mount"></div>
 *   <meta name="flashcard-course-slug" content="agentic-engineering-101">
 *
 * Embedded JSON shape:
 *   {
 *     "course_name": "Agentic Engineering 101",
 *     "course_slug": "agentic-engineering-101",
 *     "questions": [
 *       {
 *         "id": "Quiz/Module_03_Quiz_File/module_03_quiz.json#3",
 *         "source_file": "Quiz/Module_03_Quiz_File/module_03_quiz.json",
 *         "source_index": 3,
 *         "quiz_title": "Module 3: Context Priming",
 *         "question": "...",
 *         "options": ["A", "B", "C", "D"],
 *         "answer": "B",
 *         "explanation": "..."   // optional
 *       },
 *       ...
 *     ]
 *   }
 *
 * Per-question SR state in localStorage[`flashcard-state-<slug>`]:
 *   {
 *     "<question-id>": { "right": <int>, "wrong": <int>, "last": "<ISO-date>" },
 *     ...
 *   }
 *
 * Weighting: wrong & never-seen = 3x. Right = 1x. Pick weighted-random for the
 * next card, never repeating the same card twice in a single session unless
 * the bank is smaller than the session size.
 */

(function () {
    "use strict";

    var WRONG_WEIGHT = 3;
    var RIGHT_WEIGHT = 1;
    var NEW_WEIGHT = 3;

    var dataEl = document.getElementById("flashcard-data");
    var mount = document.getElementById("flashcard-mount");
    if (!dataEl || !mount) {
        return;
    }

    var bank;
    try {
        bank = JSON.parse(dataEl.textContent);
    } catch (err) {
        mount.innerHTML = '<div class="flashcard-empty"><p>The flashcard bank failed to load. The embedded JSON is malformed.</p></div>';
        return;
    }

    var courseSlug = bank.course_slug || "course";
    var courseName = bank.course_name || "Flashcards";
    var allQuestions = Array.isArray(bank.questions) ? bank.questions : [];

    if (allQuestions.length === 0) {
        mount.innerHTML = (
            '<div class="flashcard-empty">' +
            '<h2>No flashcards yet</h2>' +
            '<p>This course doesn\'t have any quiz questions to study from yet. ' +
            'Check back once quiz files have been added.</p>' +
            '</div>'
        );
        return;
    }

    var STORAGE_KEY = "flashcard-state-" + courseSlug;
    var storageOk = true;

    function loadState() {
        if (!storageOk) return {};
        try {
            var raw = localStorage.getItem(STORAGE_KEY);
            if (!raw) return {};
            var parsed = JSON.parse(raw);
            return (parsed && typeof parsed === "object") ? parsed : {};
        } catch (err) {
            storageOk = false;
            return {};
        }
    }

    function saveState(state) {
        if (!storageOk) return;
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
        } catch (err) {
            storageOk = false;
        }
    }

    function recordResult(qid, correct) {
        var state = loadState();
        var entry = state[qid] || { right: 0, wrong: 0, last: null };
        if (correct) entry.right += 1; else entry.wrong += 1;
        entry.last = new Date().toISOString().slice(0, 10);
        state[qid] = entry;
        saveState(state);
    }

    function weightFor(qid, state) {
        var entry = state[qid];
        if (!entry || (entry.right === 0 && entry.wrong === 0)) {
            return NEW_WEIGHT;
        }
        // Mix: wrong dominate, but every right answer subtracts a little.
        // A card with one wrong and one right still leans heavier than pure right.
        var w = entry.wrong * WRONG_WEIGHT + entry.right * RIGHT_WEIGHT;
        // Floor to 1 so consistently-right cards still cycle in occasionally.
        if (w < 1) w = 1;
        // Cap so a single card with a long wrong streak doesn't monopolize the queue.
        if (w > 12) w = 12;
        return w;
    }

    function shuffle(arr) {
        var a = arr.slice();
        for (var i = a.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        return a;
    }

    function pickWeighted(pool, state) {
        // Plain random fallback if storage is dead.
        if (!storageOk || !state) {
            return pool[Math.floor(Math.random() * pool.length)];
        }
        var weights = pool.map(function (q) { return weightFor(q.id, state); });
        var total = weights.reduce(function (a, b) { return a + b; }, 0);
        if (total <= 0) {
            return pool[Math.floor(Math.random() * pool.length)];
        }
        var r = Math.random() * total;
        for (var i = 0; i < pool.length; i++) {
            r -= weights[i];
            if (r <= 0) return pool[i];
        }
        return pool[pool.length - 1];
    }

    function buildSessionQueue(sessionSize) {
        // Build a queue of `sessionSize` distinct questions, picked weighted.
        // If sessionSize >= bank size, queue is the whole shuffled bank.
        var state = loadState();
        if (sessionSize >= allQuestions.length) {
            return shuffle(allQuestions);
        }
        var pool = allQuestions.slice();
        var picked = [];
        var pickedIds = Object.create(null);
        while (picked.length < sessionSize && pool.length > 0) {
            var choice = pickWeighted(pool, state);
            if (pickedIds[choice.id]) {
                pool = pool.filter(function (q) { return q.id !== choice.id; });
                continue;
            }
            picked.push(choice);
            pickedIds[choice.id] = true;
            pool = pool.filter(function (q) { return q.id !== choice.id; });
        }
        return picked;
    }

    function escapeHtml(s) {
        return String(s).replace(/[&<>"']/g, function (c) {
            return ({
                "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
            })[c];
        });
    }

    // ── State machine ─────────────────────────────────────────────────────
    var session = null;

    function renderStart() {
        var state = loadState();
        var seenCount = 0;
        var rightCount = 0;
        var wrongCount = 0;
        for (var qid in state) {
            if (Object.prototype.hasOwnProperty.call(state, qid)) {
                seenCount += 1;
                rightCount += state[qid].right || 0;
                wrongCount += state[qid].wrong || 0;
            }
        }
        var newCount = allQuestions.length - seenCount;
        if (newCount < 0) newCount = 0;

        var statsLine = (
            "<strong>" + allQuestions.length + "</strong> question" +
            (allQuestions.length === 1 ? "" : "s") + " across this course." +
            (seenCount > 0
                ? " You've answered <strong>" + seenCount + "</strong> at least once " +
                  "(" + rightCount + " correct, " + wrongCount + " wrong). " +
                  newCount + " still new."
                : " None studied yet.")
        );

        var defaultSize = Math.min(20, allQuestions.length);

        mount.innerHTML = (
            '<div class="flashcard-container">' +
            '  <h2 class="flashcard-heading">Ready to study?</h2>' +
            '  <p class="flashcard-stats">' + statsLine + '</p>' +
            '  <div class="flashcard-form">' +
            '    <label for="flashcard-size">How many questions this session?</label>' +
            '    <div class="flashcard-size-row">' +
            '      <input type="number" id="flashcard-size" min="1" max="' + allQuestions.length + '" value="' + defaultSize + '">' +
            '      <button class="flashcard-btn secondary" id="flashcard-all">All ' + allQuestions.length + '</button>' +
            '    </div>' +
            '    <p class="flashcard-hint">Wrong answers and new cards weigh 3&times; over right answers, ' +
            'so the bank steers you toward what you don\'t know yet. Your progress is kept privately in your browser.</p>' +
            (storageOk ? '' : '<p class="flashcard-warn">Note: localStorage isn\'t available, so progress weighting falls back to a plain shuffle.</p>') +
            '    <button class="flashcard-btn" id="flashcard-start">Start session →</button>' +
            (seenCount > 0 ? '    <button class="flashcard-btn link" id="flashcard-reset">Reset progress</button>' : '') +
            '  </div>' +
            '</div>'
        );

        var sizeInput = document.getElementById("flashcard-size");
        document.getElementById("flashcard-all").addEventListener("click", function () {
            sizeInput.value = String(allQuestions.length);
            sizeInput.focus();
        });
        document.getElementById("flashcard-start").addEventListener("click", function () {
            var n = parseInt(sizeInput.value, 10);
            if (!isFinite(n) || n < 1) n = defaultSize;
            if (n > allQuestions.length) n = allQuestions.length;
            startSession(n);
        });
        var resetBtn = document.getElementById("flashcard-reset");
        if (resetBtn) {
            resetBtn.addEventListener("click", function () {
                if (window.confirm("Reset all flashcard progress for " + courseName + "? This wipes per-question history saved in this browser.")) {
                    if (storageOk) {
                        try { localStorage.removeItem(STORAGE_KEY); } catch (err) { /* ignore */ }
                    }
                    renderStart();
                }
            });
        }
    }

    function startSession(size) {
        var queue = buildSessionQueue(size);
        session = {
            queue: queue,
            index: 0,
            correct: 0,
            wrong: 0,
            results: [],
            size: queue.length,
            shuffledOptions: null,
            selected: null,
            answered: false,
        };
        renderQuestion();
    }

    function renderQuestion() {
        var q = session.queue[session.index];
        session.shuffledOptions = shuffle(q.options || []);
        session.selected = null;
        session.answered = false;

        var progressPct = ((session.index) / session.size) * 100;
        var sourceTag = q.quiz_title ? '<span class="flashcard-source">' + escapeHtml(q.quiz_title) + '</span>' : '';

        var optionsHtml = session.shuffledOptions.map(function (opt, i) {
            return (
                '<label class="quiz-option" data-opt-index="' + i + '">' +
                '<input type="radio" name="flashcard-opt" value="' + i + '">' +
                '<span>' + escapeHtml(opt) + '</span>' +
                '</label>'
            );
        }).join("");

        mount.innerHTML = (
            '<div class="flashcard-container quiz-container">' +
            '  <div class="quiz-header">' +
            '    <span>Card ' + (session.index + 1) + ' of ' + session.size + '</span>' +
            '    <span>Score: <strong>' + session.correct + '</strong> / ' + session.index + '</span>' +
            '    ' + sourceTag +
            '  </div>' +
            '  <div class="quiz-progress-track">' +
            '    <div class="quiz-progress-fill" style="width:' + progressPct + '%"></div>' +
            '  </div>' +
            '  <div class="quiz-question">' + escapeHtml(q.question) + '</div>' +
            '  <div class="quiz-options" id="flashcard-options">' + optionsHtml + '</div>' +
            '  <div class="quiz-feedback" id="flashcard-feedback"></div>' +
            '  <div class="quiz-actions">' +
            '    <button class="quiz-btn flashcard-btn" id="flashcard-submit" disabled>Submit Answer</button>' +
            '    <button class="quiz-btn secondary flashcard-btn" id="flashcard-quit">Quit session</button>' +
            '  </div>' +
            '</div>'
        );

        var optionsContainer = document.getElementById("flashcard-options");
        Array.prototype.forEach.call(optionsContainer.querySelectorAll(".quiz-option"), function (label) {
            label.addEventListener("click", function () {
                if (session.answered) return;
                var idx = parseInt(label.getAttribute("data-opt-index"), 10);
                session.selected = session.shuffledOptions[idx];
                Array.prototype.forEach.call(optionsContainer.querySelectorAll(".quiz-option"), function (el) {
                    el.classList.remove("selected");
                });
                label.classList.add("selected");
                document.getElementById("flashcard-submit").disabled = false;
            });
        });

        document.getElementById("flashcard-submit").addEventListener("click", submitAnswer);
        document.getElementById("flashcard-quit").addEventListener("click", function () {
            if (session.index === 0 || window.confirm("End this session and see results so far?")) {
                renderResults();
            }
        });
    }

    function submitAnswer() {
        if (session.answered || !session.selected) return;
        var q = session.queue[session.index];
        var correct = session.selected === q.answer;
        session.answered = true;
        if (correct) session.correct += 1; else session.wrong += 1;
        session.results.push({
            id: q.id,
            quiz_title: q.quiz_title || "",
            question: q.question,
            user_answer: session.selected,
            correct_answer: q.answer,
            status: correct ? "correct" : "wrong",
        });
        recordResult(q.id, correct);

        // Highlight options
        var optionsContainer = document.getElementById("flashcard-options");
        Array.prototype.forEach.call(optionsContainer.querySelectorAll(".quiz-option"), function (label) {
            var idx = parseInt(label.getAttribute("data-opt-index"), 10);
            var opt = session.shuffledOptions[idx];
            label.setAttribute("aria-disabled", "true");
            var input = label.querySelector("input");
            if (input) input.disabled = true;
            if (opt === q.answer) label.classList.add("correct");
            else if (opt === session.selected) label.classList.add("wrong");
        });

        var fb = document.getElementById("flashcard-feedback");
        if (correct) {
            fb.className = "quiz-feedback correct";
            fb.innerHTML = "Correct!" + (q.explanation ? '<div class="flashcard-explanation">' + escapeHtml(q.explanation) + '</div>' : "");
        } else {
            fb.className = "quiz-feedback wrong";
            fb.innerHTML = (
                "Incorrect. Correct answer: " + escapeHtml(q.answer) +
                (q.explanation ? '<div class="flashcard-explanation">' + escapeHtml(q.explanation) + '</div>' : "")
            );
        }

        var submitBtn = document.getElementById("flashcard-submit");
        submitBtn.disabled = false;
        submitBtn.textContent = (session.index + 1 < session.size) ? "Next card →" : "See results →";
        // Replace listener so it now advances instead of submitting again.
        var clone = submitBtn.cloneNode(true);
        submitBtn.parentNode.replaceChild(clone, submitBtn);
        clone.addEventListener("click", advance);
    }

    function advance() {
        session.index += 1;
        if (session.index >= session.size) {
            renderResults();
        } else {
            renderQuestion();
        }
    }

    function renderResults() {
        var pct = session.size > 0 ? Math.round((session.correct / session.size) * 100) : 0;
        var summary = session.results.map(function (r, i) {
            var icon = r.status === "correct" ? "✓" : "✗";
            var detail = "";
            if (r.status === "wrong") {
                detail = (
                    '<div class="row-detail">' +
                    'Your answer: ' + escapeHtml(r.user_answer || "(none)") +
                    '<br><span class="correct-ans">Correct: ' + escapeHtml(r.correct_answer) + '</span>' +
                    '</div>'
                );
            }
            var qTrunc = r.question.length > 120 ? r.question.slice(0, 119) + "…" : r.question;
            var src = r.quiz_title ? '<span class="flashcard-source-inline">' + escapeHtml(r.quiz_title) + '</span> · ' : '';
            return (
                '<div class="quiz-summary-row ' + r.status + '">' +
                '  <div class="row-head ' + r.status + '"><span class="status">' + icon + '</span>' + src + 'Q' + (i + 1) + '. ' + escapeHtml(qTrunc) + '</div>' +
                detail +
                '</div>'
            );
        }).join("");

        mount.innerHTML = (
            '<div class="flashcard-container quiz-container">' +
            '  <div class="quiz-results">' +
            '    <h3>Session complete</h3>' +
            '    <div class="score ' + (pct >= 80 ? "pass" : "fail") + '">' + session.correct + ' / ' + session.size + '</div>' +
            '    <div class="detail">' + pct + '%</div>' +
            '    <div class="detail">Your weighting now leans toward the cards you missed. ' +
            'Run another session to keep grinding them down.</div>' +
            '  </div>' +
            '  <div class="quiz-actions">' +
            '    <button class="quiz-btn flashcard-btn" id="flashcard-again">Start another session</button>' +
            '    <button class="quiz-btn secondary flashcard-btn" id="flashcard-summary-toggle">▼ Review answers</button>' +
            '  </div>' +
            '  <div class="quiz-summary" id="flashcard-summary" style="display:none;">' + summary + '</div>' +
            '</div>'
        );

        document.getElementById("flashcard-again").addEventListener("click", renderStart);
        var toggleBtn = document.getElementById("flashcard-summary-toggle");
        var summaryEl = document.getElementById("flashcard-summary");
        var open = false;
        toggleBtn.addEventListener("click", function () {
            open = !open;
            summaryEl.style.display = open ? "block" : "none";
            toggleBtn.textContent = open ? "▲ Hide review" : "▼ Review answers";
        });
    }

    renderStart();
})();
