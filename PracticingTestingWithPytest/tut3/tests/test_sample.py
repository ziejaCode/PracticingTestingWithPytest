import sys

import pytest

from tut3.myapp.sample import add

pytestM = 6.21

@pytest.mark.skip(reason="just wanna skip it")
def test_add_num():
    assert add(1, 2) == 3

@pytest.mark.skipif(sys.version_info > (3, 9), reason="use python 3.7 or less")
def test_add_str():
    assert add("a", "b") == "ab"

@pytest.mark.skipif(pytestM > (6.2), reason="use pytest 6.2 or less")
def test_add_str1():
    assert add("a", "b") == "ab"


@pytest.mark.xfail(sys.platform == "linux", reason="dont run on linux")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()

# this test will fail
@pytest.mark.xfail(sys.platform == "Win32", reason="dont run on Window")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()



