# Design Overview
- **Architecture**: Django MVT with SQLite for simplicity.
- **Performance**: O(n) time complexity due to `Paginator.count()`; optimized queries (~4/request).
- **Scalability**: Pagination and filtering support growth beyond 20 products.

## Database Design
- Added index on `Product.description` for efficient filtering. SQLite offers partial speedup; future PostgreSQL migration with trigram indexing could achieve O(log n) for `icontains`.