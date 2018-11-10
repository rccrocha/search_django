from django.contrib import admin
from django.urls import path, include

from my_search_site.core import views

urlpatterns = [
	path('', views.home, name='home'),
	path('signup/', views.signup, name='signup'),
	path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
