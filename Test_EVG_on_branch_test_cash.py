def test_submit_user_details():
    app.given_opened_text_box_page()

    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Text Box'))
    browser.element(by.text('Text Box')).should(be.visible)

    browser.element('#userForm').all('input, textarea').should(have.size(4))
    browser.all('.form-label').element_by(have.text('Address')).should(have.text('Current Address'))

    browser.element('#userName').type('yasha')

    submit = browser.element('#submit').click()
