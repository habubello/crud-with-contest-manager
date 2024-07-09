

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __enter__(self):
        print('Book entered')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Book exited')


    def write(self):
        with open('book.txt', 'w') as file:
            file.write(self.title)
            file.write('\n')
            file.write(self.author)
            file.write('\n')
            file.write(self.year)
            file.write('\n')

    def update_book(self, old_title, new_title=None, new_author=None, new_year=None):
        with open('book.txt', 'w') as file:
            data = file.read
            if data['title'] == old_title:
                if new_title:
                    data['title'] = new_title
                if new_author:
                    data['author'] = new_author
                if new_year:
                    data['year'] = new_year
                return data
        return None
    @staticmethod
    def read():
        with open('book.txt', 'r') as file:
            data = file.read()
            print(data)
    @staticmethod
    def delete():
        with open('book.txt', 'w') as file:
            print("All is deleted")



# kitob = Book("Shaytanat", "Temur malik", "1995")
# kitob.write()
# print(Book.read())
# Book.delete()
# Book.update_book('Shaytanat',"Shaytanat","Shaytanat edited")
