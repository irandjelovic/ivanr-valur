const { devices } = require('@playwright/test');

module.exports = {
  webServer: {
    command: 'npm run dev',
    port: 3000, 
    timeout: 120 * 1000, 
    reuseExistingServer: !process.env.CI, 
  },
  use: {
    baseURL: 'http://localhost:3000', 
    testIdAttribute: 'data-test'
  },
  projects: [
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        launchOptions: {
          args: ['--start-maximized'],
        },
      },
    },
  ],
  testDir: './',
};