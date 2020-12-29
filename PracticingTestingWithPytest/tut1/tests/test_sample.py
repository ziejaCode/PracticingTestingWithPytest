#from tut1.myapp.sample import add
import sys 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from myapp.sample import add

print("test running from VSCode...")

def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"


print("test finished corected in vs")

print("confirmed from Eclipse")