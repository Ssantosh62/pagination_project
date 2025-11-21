from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from testapp.pagination import MyPagination,MyPagination2,MyPagination3

from rest_framework.pagination import PageNumberPagination
class MyPagination(PageNumberPagination):
    page_size = 20

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination
    pagination_class=MyPagination2
    pagination_class=MyPagination3
    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('ename')
        if name is not None:
            qs = qs.filter(ename__contains=name)
        return qs


'''from rest_framework.generics import ListAPIView
class EmployeeListView(ListAPIView):
	pagination_class = MyPagination'''