# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


from unicodedata import name


class Book:
    def __init__(self, title, price, authorfname, author=None):
        self.title = title
        self.price = price


        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for i in self.chapters:
            result += i.pagecount
        return result

class Author:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount) -> None:
        self.name = name
        self.pagecount = pagecount

auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, auth)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))


print(b1.author)

print(b1.title)

print(b1.getbookpagecount())