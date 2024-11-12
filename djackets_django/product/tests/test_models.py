from django.test import TestCase

from product import models


class ModelTest(TestCase):
    """Test models."""

    def test_create_category(self):
        category = models.Category.objects.create(
            name='winter',
            slug='snowman'
        )

        self.assertEqual(str(category), category.name)

    def test_create_product(self):
        cate = models.Category.objects.create(
            name='winter',
            slug='snowman'
        )

        product = models.Product.objects.create(
            category=cate,
            name='car',
            slug='gm',
            price=1
        )

        self.assertEqual(str(product), product.name)
