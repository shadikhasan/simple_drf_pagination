from django.test import RequestFactory
from rest_framework.response import Response
from rest_framework.views import APIView

from simple_drf_pagination.paginate import paginate


class DummyView(APIView):
    pagination_class = paginate(page_size=2)

    def get(self, request):
        data = [
            {"id": 1, "name": "A"},
            {"id": 2, "name": "B"},
            {"id": 3, "name": "C"},
        ]

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(data, request, view=self)
        return paginator.get_paginated_response(page)


def test_real_pagination_response():
    factory = RequestFactory()
    request = factory.get("/users/?page=1")

    response: Response = DummyView.as_view()(request)

    assert response.status_code == 200
    assert "results" in response.data
    assert len(response.data["results"]) == 2
    assert response.data["count"] == 3
