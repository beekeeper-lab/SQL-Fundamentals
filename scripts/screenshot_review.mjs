/**
 * Take scrolling screenshots of every page in every HTML file for visual review.
 *
 * Usage: node scripts/screenshot_review.mjs
 *
 * Output: screenshots/<module>/page-NN.png  (full-page captures, 1280px wide)
 *         screenshots/index.png             (course landing page)
 */

import { chromium } from 'playwright';
import { readdirSync, mkdirSync, existsSync } from 'fs';
import { resolve, basename } from 'path';

const PROJECT_ROOT = resolve(import.meta.dirname, '..');
const HTML_DIR = resolve(PROJECT_ROOT, 'html');
const SCREENSHOT_DIR = resolve(PROJECT_ROOT, 'screenshots');

// Order matters for review. Generated from scripts/build_course.py MODULES
// list, with any crash-course-*.html / reference-*.html appended.
const FILE_ORDER = [
  'module-00-what-is-sql.html',
  'module-01-creating-tables.html',
  'module-02-inserting-data.html',
  'module-03-select-and-filtering.html',
  'module-04-sorting-and-limiting.html',
  'module-05-aggregate-functions.html',
  'module-06-joins.html',
  'module-07-subqueries-and-views.html',
  'module-08-updating-and-deleting.html',
  'module-09-indexes-and-best-practices.html',
  'crash-course-overview.html',
];

async function screenshotFile(browser, htmlFile) {
  const moduleName = basename(htmlFile, '.html');
  const moduleDir = resolve(SCREENSHOT_DIR, moduleName);
  mkdirSync(moduleDir, { recursive: true });

  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 900 });

  const filePath = resolve(HTML_DIR, htmlFile);
  if (!existsSync(filePath)) {
    console.log(`  ${moduleName}: SKIP (file not found in html/)`);
    await page.close();
    return 0;
  }
  await page.goto(`file://${filePath}`, { waitUntil: 'networkidle' });

  // Get total page count (multi-page module template)
  const totalPages = await page.evaluate(() => {
    const pages = document.querySelectorAll('.page');
    return pages.length;
  });

  if (totalPages === 0) {
    // Single-page document (e.g. crash-course / reference)
    const screenshotPath = resolve(moduleDir, 'page-00.png');
    await page.screenshot({ path: screenshotPath, fullPage: true });
    console.log(`  ${moduleName}: 1 page (single-page document)`);
    await page.close();
    return 1;
  }

  console.log(`  ${moduleName}: ${totalPages} pages`);

  for (let i = 0; i < totalPages; i++) {
    // Navigate to page
    await page.evaluate((idx) => showPage(idx), i);
    await page.waitForTimeout(300); // let animations settle

    // Get the active page element and take a full-content screenshot
    const activePageEl = await page.$('.page.active');
    if (!activePageEl) {
      console.log(`    Page ${i}: no active page element found, skipping`);
      continue;
    }

    const paddedIndex = String(i).padStart(2, '0');
    const screenshotPath = resolve(moduleDir, `page-${paddedIndex}.png`);

    // Use full page screenshot to capture all scrollable content
    await page.screenshot({
      path: screenshotPath,
      fullPage: true,
    });

    // Get page title for logging
    const pageTitle = await page.evaluate(() => {
      const active = document.querySelector('.page.active');
      const h = active?.querySelector('h1, h2');
      return h?.textContent?.substring(0, 50) || '(untitled)';
    });

    console.log(`    Page ${paddedIndex}: ${pageTitle}`);
  }

  await page.close();
  return totalPages;
}

async function main() {
  console.log('Taking screenshots for visual review...');
  console.log(`Output: ${SCREENSHOT_DIR}\n`);

  mkdirSync(SCREENSHOT_DIR, { recursive: true });

  const browser = await chromium.launch();
  let totalScreenshots = 0;
  let totalModules = 0;

  for (const htmlFile of FILE_ORDER) {
    const count = await screenshotFile(browser, htmlFile);
    totalScreenshots += count;
    if (count > 0) totalModules += 1;
  }

  // Also screenshot index.html if present
  const indexPath = resolve(PROJECT_ROOT, 'index.html');
  if (existsSync(indexPath)) {
    const indexPage = await browser.newPage();
    await indexPage.setViewportSize({ width: 1280, height: 900 });
    await indexPage.goto(`file://${indexPath}`, { waitUntil: 'networkidle' });
    await indexPage.screenshot({
      path: resolve(SCREENSHOT_DIR, 'index.png'),
      fullPage: true,
    });
    await indexPage.close();
    totalScreenshots += 1;
    console.log(`\n  index.html: 1 page`);
  }

  await browser.close();

  console.log(`\nDone! ${totalScreenshots} screenshots across ${totalModules} modules saved to screenshots/`);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
