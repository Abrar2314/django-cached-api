Django Cached API

This is a Django REST API project demonstrating caching to improve performance when fetching data from a database.

Features

Django REST API endpoints for items:

GET /api/items/ → List all items (paginated)

GET /api/items/<id>/ → Get a single item by ID

Caching implemented using Django's LocMemCache

Pagination for large datasets

Caching Approach
Caching Method

Backend: LocMemCache (local memory cache)

Timeout: 5 minutes (300 seconds)

Performance Improvement

Using caching significantly reduces the response time. Example measurements using curl:
time curl http://127.0.0.1:8000/api/items/
real    0m0.024s
user    0m0.008s
sys     0m0.010s

With Cache (after first request)
time curl http://127.0.0.1:8000/api/items/
real    0m0.013s
user    0m0.006s
sys     0m0.004s
Response time improved from 0.024s → 0.013s, showing caching reduces the API response time almost by half.
