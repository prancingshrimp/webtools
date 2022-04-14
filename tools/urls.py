from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('statics/', include('statics.urls', namespace='statics')),
    path('admin/', admin.site.urls),
]