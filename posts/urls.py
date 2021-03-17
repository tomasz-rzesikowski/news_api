from rest_framework import routers

from posts.views import UserViewSet, PostViewSet

router = routers.SimpleRouter()
router.register(r'v1/users', UserViewSet, basename='users')
router.register(r'v1/posts', PostViewSet, basename='posts')

urlpatterns = router.urls
