from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)


def paginate(
    type: str = "page",
    page_size: int = 10,
    max_size: int = 100,
    ordering: str = "-id",
):
    """
    Factory function that returns a DRF pagination class.
    """

    if type == "page":
        class CustomPagePagination(PageNumberPagination):
            page_size_query_param = "page_size"
            max_page_size = max_size

        CustomPagePagination.page_size = page_size
        return CustomPagePagination

    if type == "limit":
        class CustomLimitPagination(LimitOffsetPagination):
            max_limit = max_size

        CustomLimitPagination.default_limit = page_size
        return CustomLimitPagination

    if type == "cursor":
        class CustomCursorPagination(CursorPagination):
            pass

        CustomCursorPagination.page_size = page_size
        CustomCursorPagination.ordering = ordering
        return CustomCursorPagination

    raise ValueError("Invalid pagination type")
