exports.MultiplyPage = class MultiplyPage {

  constructor(page) {
    this.page = page;
    this.multiplicandInput = page.getByTestId('multiplicand-input');
    this.multiplicatorInput = page.getByTestId('multiplicator-input');
    this.resultInfo = page.getByTestId('result-info');
    this.multiplyBtn = page.getByTestId('multiply-btn');
  }

  async multiply(multiplicand, multiplicator) {
    await this.multiplicandInput.fill(multiplicand);
    await this.multiplicatorInput.fill(multiplicator);
    await this.multiplyBtn.click();
  }

  async getResult() {
    return await this.resultInfo.textContent();
  }
}