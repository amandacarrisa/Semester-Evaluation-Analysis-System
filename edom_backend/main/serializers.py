from rest_framework import serializers
from main.models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ["id", "nama", "npm", "angkatan"]
