from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuItemViewTest(TestCase):

    def setUp(self):
        MenuItem.objects.create(title="Pasta", price=12.5, inventory=10)
        MenuItem.objects.create(title="Burger", price=8.5, inventory=20)
        MenuItem.objects.create(title="Pizza", price=15.0, inventory=5)

    def test_get_all(self):
        items = MenuItem.objects.all()
        serialized_data = MenuItemSerializer(items, many=True).data
        response = self.client.get("/api/restaurant/menuitem/")

        # Compare serialized data and API response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)
