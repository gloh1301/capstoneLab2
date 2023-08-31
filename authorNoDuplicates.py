class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title not in self.books:
            self.books.append(title)
        else:
            print(f'Duplicate {title} book not added.')

    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'
        return f'Name: {self.name} Books Published: {book_list}'


def main():
    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    shakespeare.publish('Richard III')


    print(shakespeare)

    grant = Author('Grant')
    print(grant)


main()
