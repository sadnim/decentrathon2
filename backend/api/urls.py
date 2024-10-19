from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, TeacherViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
