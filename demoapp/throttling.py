from rest_framework.throttling import UserRateThrottle

class BooksViewThrottle(UserRateThrottle):
    scope = 'books-scope'

class BookDetailedViewThrottle(UserRateThrottle):
    scope = 'book-detailed-scope'