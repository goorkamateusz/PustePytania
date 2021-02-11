import pytest
from PustePytania.Exam import Exam
from PustePytania.Exam import reapetedTask
from PustePytania.Task import Task
from tests.Mocks import mockReaction

examples_text_for_append = [
    ([ "oneoneone", "twotwotwotwo", "threethreethree" ],
     [ "oneoneone", "twotwotwotwo", "threethreethree" ]),
    ([ "oneoneone", "twotwotwotwo", "oneoneone" ],
     [ "oneoneone", "twotwotwotwo" ]),
    ([ "oneoneone", "oneoneone", "oneoneone", "oneoneone", ],
     [ "oneoneone" ]),
]

examples_text_for_sorting = [
    (["abc222", "cda11111", "bcd3333"],
     ["abc222", "bcd3333", "cda11111"]),
]

@pytest.fixture
def empty_exam():
    return Exam()

def create_task_list(task_text_list) -> list:
    tasks = []
    mock_reaction = [mockReaction()]
    for text in task_text_list:
        new_task = Task(mock_reaction)
        new_task.set_text(text)
        tasks.append(new_task)
    return tasks

# -------------------------------------------------

def test_init(empty_exam):
    assert empty_exam.task_list == []

def test_len_empty_exam(empty_exam):
    assert len(empty_exam) == 0

def test_is_empty(empty_exam):
    assert empty_exam.is_empty() == True

def test_append_once(empty_exam):
    empty_exam.append(Task([mockReaction()]))
    assert len(empty_exam) == 1
    assert empty_exam.is_empty() == False

def test_clear(empty_exam):
    empty_exam.append(Task([mockReaction()]))
    empty_exam.clear()
    assert empty_exam.is_empty() == True

@pytest.mark.parametrize("text_list, expected", examples_text_for_append)
def test_append_removing_reapeated(text_list, expected):
    exam = Exam()
    example_task_list = create_task_list(text_list)

    for task_example in example_task_list:
        try:
            exam.append(task_example)
        except Exception as e:
            assert isinstance(e, reapetedTask)

    actual = exam.task_list
    assert len(actual) == len(expected)
    assert all([a.text == e for a, e in zip(actual, expected)])

@pytest.mark.parametrize("text_list, expected", examples_text_for_sorting)
def test_sort(text_list, expected):
    exam = Exam()
    example_task_list = create_task_list(text_list)

    for task_example in example_task_list:
        try:
            exam.append(task_example)
        except Exception as e:
            assert isinstance(e, reapetedTask)

    exam.sort()

    actual = exam.task_list
    assert len(actual) == len(expected)
    assert all([a.text == e for a, e in zip(actual, expected)])
