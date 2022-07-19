from django import views
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    # route to add products
    path('product/add/',views.AddProduct.as_view() ),

    # route to fetch products
    path('product/get/',views.GetProduct.as_view() ),

    # route to update products
    path('product/update/',views.UpdateProduct.as_view() ),

    # route to delete products
    path('product/delete/',views.DeleteProduct.as_view() ),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
