from lib.webui import login_check
import pytest


class Test_错误登录:
    @pytest.mark.parametrize('username, password, expectalert', [
        (None, '88888888', '请输入用户名'),
        ('byhy', None, '请输入密码'),
        ('byh', '88888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '8888888', '登录失败 : 用户名或者密码错误'),
        ('byhy', '888888888', '登录失败 : 用户名或者密码错误'),
    ])
    def test_ui_0001_0005(self, username, password, expectalert):
        alerttext = login_check(username, password)
        assert alerttext == expectalert

    # def test_ui_0001(self):
    #     pwd = 88888888
    #     alert_text = login_check(None, pwd)
    #     assert alert_text == '请输入用户名'

    # def test_ui_0002(self):
    #     username = 'byhy'
    #     alert_text = login_check(username, None)
    #     assert alert_text == '请输入密码'

    # def test_ui_0003(self):
    #     username = 'byh'
    #     pwd = 88888888
    #     alert_text = login_check(username, pwd)
    #     assert alert_text == '登录失败 : 用户名或者密码错误'

    # def test_ui_0004(self):
    #     username = 'byhy'
    #     pwd = 8888888
    #     alert_text = login_check(username, pwd)
    #     assert alert_text == '登录失败 : 用户名或者密码错误'

    # def test_ui_0005(self):
    #     username = 'byhy'
    #     pwd = 888888888
    #     alert_text = login_check(username, pwd)
    #     assert alert_text == '登录失败 : 用户名或者密码错误'
