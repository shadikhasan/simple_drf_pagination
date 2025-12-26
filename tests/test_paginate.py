import pytest
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)

from simple_drf_pagination.paginate import paginate

def test_default_page_pagination():
    Pagination = paginate(page_size=20)
    paginator = Pagination()

    assert isinstance(paginator, PageNumberPagination)
    assert paginator.page_size == 20


def test_limit_offset_pagination():
    Pagination = paginate("limit", page_size=15, max_size=50)
    paginator = Pagination()

    assert isinstance(paginator, LimitOffsetPagination)
    assert paginator.default_limit == 15
    assert paginator.max_limit == 50


def test_cursor_pagination():
    Pagination = paginate("cursor", page_size=10, ordering="-created_at")
    paginator = Pagination()

    assert isinstance(paginator, CursorPagination)
    assert paginator.page_size == 10
    assert paginator.ordering == "-created_at"


def test_invalid_pagination_type():
    with pytest.raises(ValueError):
        paginate("invalid")
