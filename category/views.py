from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def create(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #
    #
