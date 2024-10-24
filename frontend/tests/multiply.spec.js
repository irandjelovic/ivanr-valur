const { test, expect } = require('@playwright/test');
const { MultiplyPage } = require('./pages/multiply-page');

test.describe('Multiply Numbers', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('');
  });

  test('multiply two numbers', async ({ page }) => {
    const multiplyPage = new MultiplyPage(page);
    await expect(page).toHaveURL('http://localhost:3000');

    await multiplyPage.multiply('5', '9');
    await expect(await multiplyPage.getResult()).toBe('45');

  });

  test.afterEach(async ({ page }) => {
    await page.close();
  });
});
