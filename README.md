simple-drf-pagination
=====================

Zero-boilerplate pagination helpers for Django REST Framework.

This package provides a single factory function, `paginate`, that returns a
DRF pagination class based on a short type string.

Installation
------------

```bash
pip install simple-drf-pagination
```

Quick start
-----------

```python
from simple_drf_pagination import paginate

# Page-number pagination
PagePagination = paginate(page_size=20, max_size=100)

# Limit/offset pagination
LimitPagination = paginate("limit", page_size=50, max_size=200)

# Cursor pagination
CursorPagination = paginate("cursor", page_size=25, ordering="-created_at")
```

Usage with DRF views
--------------------

```python
from rest_framework.viewsets import ModelViewSet
from simple_drf_pagination import paginate

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = paginate("page", page_size=20)
```

API
---

```python
paginate(
    type: str = "page",
    page_size: int = 10,
    max_size: int = 100,
    ordering: str = "-id",
)
```

Parameters
----------

- `type`: `"page"`, `"limit"`, or `"cursor"`. Defaults to `"page"`.
- `page_size`: Default page size for the pagination class.
- `max_size`: Maximum page size or limit (page and limit types).
- `ordering`: Cursor ordering field (cursor type only).

Behavior details
----------------

- `"page"`: returns a `PageNumberPagination` class with `page_size`,
  `page_size_query_param="page_size"`, and `max_page_size`.
- `"limit"`: returns a `LimitOffsetPagination` class with `default_limit` and
  `max_limit`.
- `"cursor"`: returns a `CursorPagination` class with `page_size` and `ordering`.

Errors
------

If `type` is not one of `"page"`, `"limit"`, or `"cursor"`, a `ValueError`
is raised.

License
-------

MIT
