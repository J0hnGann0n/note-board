from django.conf.urls import url, include
from rest_framework import routers
from project.notes import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'items', views.NoteItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]