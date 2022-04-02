from django.http import JsonResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TrendKeywordSerializer, TrendSearchSerializer
from .utils import trendSearchData, todayTrendData
from rest_framework import views


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/today_trends/'},
        {'GET': '/api/trend_keywords/'},
    ]

    return Response(routes)


class TodayTrendsViews(views.APIView):

    def get(self, request):
        trend_search = trendSearchData(request)
        results = TrendKeywordSerializer(trend_search, many=True).data
        return Response(results)


class TrendsSearchViews(views.APIView):

    def get(self, request):
        today_search = todayTrendData(request)
        results = TrendSearchSerializer(today_search, many=True).data
        return Response(results)
