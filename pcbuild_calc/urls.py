from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
]

from map.views import my_customized_server_error
handler500 = my_customized_server_error