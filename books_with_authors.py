"""Enter authors' last names for books, and you'll get the number of right answers."""
# import sys
from random import sample
from argparse import ArgumentParser


collection = {"Pushkin": {"Eugene Onegin", "The Capitan's Daughter"},
              "Dostoevsky": {"Crime and Punishment", "The Idiot", "The Brothers Karamazov"},
              "Hugo": {"Les Miserables", "The Hunchback of Notre-Dame"},
              "Goethe": {"Faust", }, "London": {"White Fang", "The Iron Heel"},
              "Huxley": {"Brave New World", }, "Shakespeare": {"Romeo and Juliet", "Hamlet"}}

books = set()

# creating the set of all books from collection:
for book_set in collection.values():
    books = books | book_set


def exam(number_of_questions=5) -> None:
    """Function print The book's name, user should enter the author's last name
    number_of_questions: number of questions in the exam, default value is 5

    """

    right_answers = 0
    exam_collection = sample(books, number_of_questions)
    for book in exam_collection:
        print("Book: ", book, "\nPlease enter the author's last name:")
        author = input()
        if book in collection.get(author, set()):
            print("Correct!")
            right_answers += 1
        else:
            print("Incorrect!")
    print("Number of right answers: ", right_answers)
    print("You pass the exam" if right_answers > number_of_questions // 2 else "You fail the exam")


def main():
    parser = ArgumentParser()
    parser.add_argument("-n", "--number", type=int, default=5, help="Number of questions in the exam")

    args = parser.parse_args()

    exam(args.number)


if __name__ == "__main__":
    main()
else:
    print("books_with_authors loaded as a module")
