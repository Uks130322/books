import dataclasses
import pytest
import testlib
from unittest import TestCase
from unittest.mock import patch

import books_with_authors as books


@dataclasses.dataclass
class Case:
    books_for_test: list[str]
    authors: list[str]
    number: int
    right_answers: int

    def __str__(self) -> str:
        return "exam_{}".format(self.books_for_test)


TEST_CASES = [
    Case(books_for_test=["Eugene Onegin", "The Capitan's Daughter"], authors=["Pushkin", "Pushkin"],
         number=2, right_answers=2)
]


###################
# Structure asserts
###################


def test_docs() -> None:
    assert testlib.is_function_docstring_exists(books.exam)


###################
# Tests
###################


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_exam(t: Case) -> None:

    pass

