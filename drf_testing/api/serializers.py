from rest_framework import serializers


class TrendKeywordSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    key = serializers.CharField()


class TrendSearchSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    exploreLink = serializers.CharField()
