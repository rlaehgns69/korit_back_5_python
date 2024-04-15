class Book:
   

    def __init__(self, bookId = 0, bookName = "", authorName = "", publisherName = "", isbn = ""):
        #파이썬은 멤버변수를 위에 생성하지 않는다. self. 으로 생성
        #print(self) this 주소
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.publisherName = publisherName
        self.isbn = isbn

    def setAuthor(self, author):
        self.author = author

    def __str__(self):
        return f"""Book[
bookId: {self.bookId},
bookName: {self.bookName},
authorName: {self.authorName},
publisherName: {self.publisherName}]"""
        # return "Book[bookId: {bookId}, bookName: {bookName}]".format(bookId = self.bookId, bookName= self.bookName)
        # return "Book[bookId: %d, bookName: %s]" % (self.bookId, self.bookName)
          