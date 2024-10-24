from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.test import APISimpleTestCase


class MultiplyNumbersApiTestCase(APISimpleTestCase):
    """ Test api/multiply endpoint"""
    url: str = reverse('multiply')

    def test_multiply_success(self):
        response: Response = self.client.get(self.url, {'multiplicand': '5', 'multiplicator': '2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'res': 10})

    def test_multiply_multiplicand_missing(self):
        response: Response = self.client.get(self.url, {'multiplicator': '2'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['multiplicand'][0], ErrorDetail(string='This field is required.', code='required'))

    def test_multiply_multiplicator_missing(self):
        response: Response = self.client.get(self.url, {'multiplicand': '5'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['multiplicator'][0], ErrorDetail(string='This field is required.', code='required'))

    def test_multiply_wrong_format(self):
        response: Response = self.client.get(self.url, {'multiplicand': 'a', 'multiplicator': 'b'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['multiplicand'][0], ErrorDetail(string='A valid number is required.', code='invalid'))
        self.assertEqual(response.data['multiplicator'][0], ErrorDetail(string='A valid number is required.', code='invalid'))
