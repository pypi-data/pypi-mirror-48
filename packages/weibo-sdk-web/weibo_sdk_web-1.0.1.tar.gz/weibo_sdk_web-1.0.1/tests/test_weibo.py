import pytest
import tests
from time import time
from weibo_web import Weibo

wb = Weibo(tests.username, tests.password)


def test_get_username():
    assert wb.get_username() == '瞎眼看海贼'


def test_post_text():
    res = wb.post_text('发布的微博lai[悲伤]%s' % int(time() * 1e3))

    assert res['msg'] == ''

def test_upload_pic():
    # pid = wb.upload_pic(base)
    # assert pid != ''
    pass
