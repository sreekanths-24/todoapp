from django.contrib import admin
from django.urls import path, include  # Import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # Import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include your app's URLs here
]

urlpatterns += staticfiles_urlpatterns()  # Add this line