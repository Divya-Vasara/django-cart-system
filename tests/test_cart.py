from django.test import TestCase
from django.contrib.auth.models import User
from cart.models import CartItem

class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_cart_item_creation(self):
        item = CartItem.objects.create(
            user=self.user,
            product_name='Sample Product',
            product_price=10.00,
            quantity=2
        )
        self.assertEqual(str(item), 'Sample Product (2)')