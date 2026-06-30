from rest_framework.routers import DefaultRouter
from .views_api import (
    TypeViewSet,
    StatusViewSet,
    CategoryViewSet,
    SubCategoryViewSet
)

router = DefaultRouter()

router.register(r"types", TypeViewSet)
router.register(r"statuses", StatusViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"subcategories", SubCategoryViewSet)

urlpatterns = router.urls