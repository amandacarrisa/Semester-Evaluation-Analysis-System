from rest_framework import viewsets
from main.models import Developer
from main.serializers import DeveloperSerializer
from main.permissions import IsAuthenticatedOrReadOnly


class DeveloperViewSet(viewsets.ModelViewSet):
    """
    This API will return this site's developers data.
    Use `?angkatan=2019` to filter developers from angkatan 2019.
    """

    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all().order_by("npm")
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        angkatan = self.request.GET.get("angkatan", None)
        if angkatan:
            self.queryset = self.queryset.filter(npm__startswith=angkatan[2:])
        return self.queryset
