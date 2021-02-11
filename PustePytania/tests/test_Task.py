import pytest
from tests.Mocks import mockReaction
from PustePytania.Task import *

@pytest.fixture
def task():
    return Task([])

# ------------------------------------

def test_init():
    task = Task([])
    assert task.skip() == False
    assert task.end_of_exam() == False
    assert str(task) == "\n? ? ?  | 0.00 | prawda:0, fałsz:0"

@pytest.mark.parametrize("reactions, expected", [
    (   [mockReaction("✔️", 9), mockReaction("❌", 2)],
        f"\nPRAWDA | {round(100*(8/9), 2)} | prawda:8, fałsz:1"
    ),
    (   [mockReaction("✔️", 1), mockReaction("❌", 1)],
        f"\n? ? ?  | 0.00 | prawda:0, fałsz:0"
    ),
    (   [mockReaction("✔️", 1), mockReaction("❌", 1), mockReaction("🆕", 1)],
        f"\n? ? ?  | 0.00 | prawda:0, fałsz:0"
    ),
    (   [mockReaction("✔️", 41), mockReaction("❌", 101), mockReaction("⏭️", 11)],
        f"\nFAŁSZ  | {round(100*100/150, 2)} | prawda:40, fałsz:100, nie wiem:10"
    ),
    (   [],
        f"\n? ? ?  | 0.00 | prawda:0, fałsz:0"
    )
])
def test__str__(reactions, expected: str):
    actual = str(Task(reactions))
    assert actual == expected

def test_set_text(task: Task):
    example = "Example text"
    task.set_text(example)
    assert task.get_text() == example

# todo skip test
# todo end of exam test
