"""
Basic syntax loops programming by While
"""

# Examples and reviews
# Loops by While

total_book = 10
print(f'total book {total_book}')

total_books_read = 0
print(f'total books reads and understood {total_books_read}')

print('Mom says : "read all the books until it is understood!')

while total_books_read < total_book * 2:
    total_books_read = total_books_read + 1
    if total_books_read == 9:
        print(f'Book {total_books_read} has been read and not understood')
    else:
        total_books_read = total_books_read + 1
        print(f'Book {total_books_read} has been read and understood')

print(f'total books reads and understood {total_books_read}')
