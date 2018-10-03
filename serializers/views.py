from django.http import JsonResponse, HttpResponse
from .models import Company,Language,Frameworks,Technologies
from .serializers import (
                            CompanySerializer,
                            LanguageSerializer,GetLanguageSerializer,
                            FrameworksSerializer,GetFrameworksSerializer,
                            TechnologiesSerializer,GetTechnologiesSerializer,
                        )
from rest_framework import viewsets


class CompanyView(viewsets.ModelViewSet):
    queryset =  Company.objects.all()
    serializer_class = CompanySerializer


class LanguageView(viewsets.ModelViewSet):
    queryset =  Language.objects.all()
    serializer_class = LanguageSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = GetLanguageSerializer
        return serializer_class

class FrameworksView(viewsets.ModelViewSet):
    queryset =  Frameworks.objects.all()
    serializer_class = FrameworksSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = GetFrameworksSerializer
        return serializer_class

class TechnologiesView(viewsets.ModelViewSet):
    queryset =  Technologies.objects.all()
    serializer_class = TechnologiesSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = GetTechnologiesSerializer
        return serializer_class
