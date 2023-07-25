from django.test import TestCase

from .models import *
from .serializer import *


class bookingtest(TestCase):
    def test(self):
        item = menu.objects.create(title="Jollof", price=32, category=3)
        assert item.title == 'Jollof'


class menuviewtest(TestCase):
    def setUp(self) -> None:
        item1 = menu.objects.create(title="Ice cream", price=10, category=2)
        item2 = menu.objects.create(title="Sandwich", price=5, category=1)
        item3 = menu.objects.create(title="Chips", price=4, category=5)

    def test_all(self):
        items = menu.objects.all()
        self.assertEqual(len(items), 3)
        assert self.setUp is not None
