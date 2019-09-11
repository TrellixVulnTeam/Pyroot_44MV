"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers       # urls for accessing API
from restapp.views import TaskViewSet
# from restapp.views import TaskViewSetDue, TaskViewSetCompleted   # commented for filter usage
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()    # use it with the filter

# router = routers.SimpleRouter()     # using a different router - for without filter
router.register(r'task', TaskViewSet)  # url with task

# with filter module

# router.register(r'due', TaskViewSetDue)  # url with due - commented for filter usage
# router.register(r'completed', TaskViewSetCompleted)  # url with completed - commented for filter usage

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
