from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, Tag

def product_search(request):
    """
    Search and filter products by description, category, and tag, with pagination.
    Returns a rendered template with filtered products and filter options.
    """
    # Base queryset with optimizations for related fields
    products = Product.objects.select_related('category').prefetch_related('tags')

    # Fetch filter options (only those with associated products)
    categories = Category.objects.filter(product__isnull=False).distinct()
    tags = Tag.objects.filter(product__isnull=False).distinct()    

    # Get query parameters with defaults
    description = request.GET.get('description', '')
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')
    
    # Dynamically build filters to reduce repetitive code
    filters = {}
    if description:
        filters['description__icontains'] = description
    if category_id:
        filters['category__id'] = category_id
    if tag_id:
        filters['tags__id'] = tag_id
    if filters:
        products = products.filter(**filters)
    
    # Paginate results (5 per page)
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # Default to first page if page number is invalid
        page_obj = paginator.page(1)
    except EmptyPage:
        # Go to last page if requested page is out of range
        page_obj = paginator.page(paginator.num_pages)

    # Prepare context for template
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
        'description': description,
        'selected_category': category_id,
        'selected_tag': tag_id,
    }
    return render(request, 'products/search.html', context)