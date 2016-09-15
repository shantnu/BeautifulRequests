import BeautifulRequests
import vcr

@vcr.use_cassette("tests/get_text.yaml")
def test_get_text():
    ret_code, title, text = BeautifulRequests.get_text("https://pypi.python.org/pypi")

    assert ret_code == 200
    assert ('PyPI - the Python Package Index' in title)
    assert ('Customer: Now then, some cheese please, my good man.' in text)

@vcr.use_cassette("tests/get_text_err.yaml")
def test_wrong_page():
    ret_code, title, text = BeautifulRequests.get_text("https://pypi.python.or")
    assert ret_code == -99
    assert ('ERROR' in title)

