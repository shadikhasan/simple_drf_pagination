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

    Usage:
        paginate(page_size=20)
        paginate("limit", page_size=20)
        paginate("cursor", page_size=20, ordering="-created_at")
    """

    if type == "page":
        class CustomPagePagination(PageNumberPagination):
            page_size = page_size
            page_size_query_param = "page_size"
            max_page_size = max_size

        return CustomPagePagination

    if type == "limit":
        class CustomLimitPagination(LimitOffsetPagination):
            default_limit = page_size
            max_limit = max_size

        return CustomLimitPagination

    if type == "cursor":
        class CustomCursorPagination(CursorPagination):
            page_size = page_size
            ordering = ordering

        return CustomCursorPagination

    raise ValueError(
        "Invalid pagination type. Use 'page', 'limit', or 'cursor'."
    )
