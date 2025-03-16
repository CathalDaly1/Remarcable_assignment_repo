from django.db import models

class Category(models.Model):
    """Model representing a product category."""
    
    # CharField for storing the category name, max length of 100 characters
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """Return string representation of the Category."""
        return self.name
    
    class Meta:
        """Metadata options for the Category model."""
        verbose_name_plural = 'Categories'  # Correct plural form for admin interface

class Tag(models.Model):
    """Model representing a tag for products."""
    
    # CharField for storing the tag name, max length of 50 characters
    name = models.CharField(max_length=50)
    
    def __str__(self):
        """Return string representation of the Tag."""
        return self.name

class Product(models.Model):
    """Model representing a product in the store."""
    
    # CharField for storing the product name, max length of 100 characters
    name = models.CharField(max_length=100)
    
    # TextField for product description with database index for faster searching
    description = models.TextField(db_index=True)
    
    # ForeignKey relationship to Category, deletes product if category is deleted
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    # ManyToManyField relationship to Tag, allowing multiple tags per product
    tags = models.ManyToManyField('Tag')
    
    # DecimalField for price, allowing up to 10 digits total with 2 after decimal
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # DateTimeField automatically set to creation time
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return string representation of the Product."""
        return self.name