import pytest
from PustePytania.Counter import Counter

@pytest.fixture
def example_cnt():
    return Counter()

def text_init():
    cnt = Counter()
    assert cnt.screen == 0
    assert cnt.skip == 0
    assert cnt.exam == 0
    assert cnt.msg == 0
    assert cnt.reapeted == 0

def test_limit_of_exam_for_no_limit(example_cnt):
    assert example_cnt.limit_of_exam() == False
    assert example_cnt.limit_of_exam(1) == False
    assert example_cnt.limit_of_exam(1000) == False

def test_limit_of_exam_for_with_limit(example_cnt):
    example_cnt.exam = 3
    assert example_cnt.limit_of_exam() == False
    assert example_cnt.limit_of_exam(1) == True
    assert example_cnt.limit_of_exam(3) == True
    assert example_cnt.limit_of_exam(1000) == False

def test_iadded():
    cnt1 = Counter()
    cnt2 = Counter()

    cnt1.screen = 10
    cnt1.skip = 10
    cnt1.exam = 2
    cnt1.msg = 10
    cnt1.reapeted = 20

    cnt2.screen = 5
    cnt2.skip = 10
    cnt2.exam = 1
    cnt2.msg = 10
    cnt2.reapeted = 20

    cnt1 += cnt2

    assert cnt1.screen == 15
    assert cnt1.skip == 20
    assert cnt1.exam == 3
    assert cnt1.msg == 20
    assert cnt1.reapeted == 40
