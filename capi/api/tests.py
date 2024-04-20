from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Company, Employee
from datetime import datetime

class CompanyAPITest(APITestCase):
    def setUp(self):
        self.company1 = Company.objects.create(name='Company1', location='Location1', about='About company1', date=datetime(2022, 1, 1, 12, 0, 0), active=True)
        self.company2 = Company.objects.create(name='Company2', location='Location2', about='About company2', date=datetime(2022, 1, 2, 12, 0, 0), active=False)

    def test_list_companies(self):
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_company(self):
        url = reverse('company-list')
        data = {'name': 'NewCompany', 'location': 'NewLocation', 'about': 'New about', 'date': '2022-01-03T12:00:00Z', 'active': True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 3)
        self.assertEqual(Company.objects.last().name, 'NewCompany')

class EmployeeAPITest(APITestCase):
    def setUp(self):
        self.company1 = Company.objects.create(name='Company1', location='Location1', about='About company1', date=timezone.make_aware(datetime(2022, 1, 1, 12, 0, 0)), active=True)
        self.company2 = Company.objects.create(name='Company2', location='Location2', about='About company2', date=timezone.make_aware(datetime(2022, 1, 2, 12, 0, 0)), active=False)


    def test_list_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_employee(self):
        url = reverse('employee-list')
        data = {'name': 'NewEmployee', 'email': 'newemployee@example.com', 'address': 'NewAddress', 'phone': 1234567892, 'position': 'Tester', 'company': self.company.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 3)
        self.assertEqual(Employee.objects.last().name, 'NewEmployee')
