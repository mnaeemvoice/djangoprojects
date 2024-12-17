# dua_goats_sahiwal/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  # Ensure this is included
]
