from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls .static import static

app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("products/", views.products, name="products"),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)