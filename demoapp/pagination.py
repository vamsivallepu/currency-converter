from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class BooksViewPageNo(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'size'

class BooksViewLimitOffset(LimitOffsetPagination):
    default_limit = 3

class BooksViewCursor(CursorPagination):
    page_size = 3
    ordering = 'title'