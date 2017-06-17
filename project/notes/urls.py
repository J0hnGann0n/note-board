from django.conf.urls import url, include
from rest_framework import routers
from project.notes import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

# API Endpoints
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'items', views.NoteItemViewSet)

urlpatterns = [
    # Api root url
    url(r'^api/', include(router.urls)),

    # Login / Logout
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
]