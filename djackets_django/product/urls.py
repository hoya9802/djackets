from django.urls import path

from product import views


app_name = 'product'

urlpatterns = [
    path(
        'latest-products/',
        views.LatestProductsList.as_view(),
        name='latest-product-list'
    ),
    path(
        'products/<slug:category_slug>/<slug:product_slug>/',
        views.ProductDetail.as_view()
    )
]
