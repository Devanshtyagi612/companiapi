from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Company,Employee
from .serializers import Cpi,EmployeeSerializer


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=Cpi
    # compnies/{companyid/employee}
    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
        # print("get employess of companies",pk , "company")
        company=Company.objects.get(pk=pk)
        emps=Employee.objects.filter(company=company)
        emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
        
        return Response(emps_serializer.data)
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    
    