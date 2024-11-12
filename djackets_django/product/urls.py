from django.urls import path

from product import views


app_name = 'product'

urlpatterns = [
    path(
        'latest-products/',
        views.LatestProductsList.as_view(),
        name='latest-product-list'
    ),
]
