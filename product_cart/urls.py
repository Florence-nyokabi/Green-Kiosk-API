from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import add_to_cart, view_cart, remove_item, empty_cart

urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('product_cart/', view_cart, name='view_cart'),
    path("remove_item/<int:id>/", remove_item, name = "remove_item"),
    path("empty/", empty_cart, name="empty_cart"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)