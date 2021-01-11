from rest_framework import serializers

from .models import DtAvgTable

class DtAvgTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtAvgTable
        fields = '__all__'