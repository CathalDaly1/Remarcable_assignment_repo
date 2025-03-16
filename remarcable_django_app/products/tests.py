from django.test import TestCase
from django.urls import reverse
# Assuming these models are in products/models.py
from products.models import Category, Tag, Product

class ProductSearchTests(TestCase):
    """Test case class for product search functionality"""
    
    def setUp(self):
        """
        Set up test data before each test method runs.
        Creates a category, tag, and initial product for testing.
        """
        # Create a test category
        self.category = Category.objects.create(name="Instruments")
        
        # Create a test tag
        self.tag = Tag.objects.create(name="new-release")
        
        # Create a test product with category and tag
        self.product = Product.objects.create(
            name="Electric Guitar",
            description="Classic rock guitar",
            category=self.category,
            price=299.99
        )
        self.product.tags.add(self.tag)

    def test_search_view(self):
        """
        Test the product search view functionality.
        Verifies that searching by description returns correct results.
        """
        # Perform a GET request to the search view with a query parameter
        response = self.client.get(reverse("product_search") + "?description=guitar")
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verify that the response contains the product name
        self.assertContains(response, "Electric Guitar")
        
        # Check that exactly one product is returned in the page object
        self.assertEqual(len(response.context["page_obj"]), 1)

    def test_pagination(self):
        """
        Test pagination functionality of the product search view.
        Creates multiple products and verifies pagination works correctly.
        """
        # Create 10 additional products to test pagination (page size is 5)
        for i in range(10):  # More than 5 (page size)
            Product.objects.create(
                name=f"Guitar {i}",
                description="Test",
                category=self.category,
                price=100
            )
        
        # Request the second page of results
        response = self.client.get(reverse("product_search") + "?page=2")
        
        # Verify successful response
        self.assertEqual(response.status_code, 200)
        
        # Check that the page contains exactly 5 items (page size)
        self.assertEqual(len(response.context["page_obj"]), 5)