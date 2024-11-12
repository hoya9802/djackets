"""
Tests for product APIS.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

PRODUCT_URL = reverse('product:latest-product-list')


class ProductAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_latest_product_list(self):
        res = self.client.get(PRODUCT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
