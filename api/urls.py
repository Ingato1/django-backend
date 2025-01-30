from .views import TeachersView,studentsView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('teachers',TeachersView)
router.register('students',studentsView)

urlpatterns=router.urls

