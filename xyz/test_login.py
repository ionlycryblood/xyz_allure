from xyz.loginpage import LoginPage
import pytest



@pytest.mark.parametrize('username, password, expected',[
('standard_user', 'secret_sauce', True )
                         ])
def test_login(page, username, password, expected):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(username, password)

    if expected:
        assert 'inventory' in page.url
    else:
        assert page.get_by_text("Epic sadface: Sorry, this user has been locked out.").is_visible()