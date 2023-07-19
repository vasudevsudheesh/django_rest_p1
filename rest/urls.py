from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restapp.views import TaskViewSet ,CreateUserview
from restapp import views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

# router = routers.DefaultRouter()
router = routers.SimpleRouter()

router.register('task', TaskViewSet)
router.register('completed_task', views.CompletedTaskViewSet)
router.register('due_task', views.DueTaskViewSet)

# router.register('task', Taskviewset, basename='task')

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(router.urls)),
                  path('register/', views.CreateUserview.as_view(), name='user'),
                  path('api_auth', include('rest_framework.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
