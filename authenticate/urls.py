
from django.contrib import admin
from django.urls import path, include

from mainapp.views import LandingView

urlpatterns = [
    path('', LandingView.as_view(), name='landing-view'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('mainapp.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]
