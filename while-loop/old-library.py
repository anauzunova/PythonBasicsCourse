wanted_book = input()
checked_books = 0

while True:
    book = input()

    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break

    checked_books += 1

    if book == wanted_book:
        print(f"You checked {checked_books} books and found it.")
        break