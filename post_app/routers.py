from rest_framework import routers

from .views import PostsViewSet

post_router = routers.DefaultRouter()
# post_router = routers.SimpleRouter()

post_router.register(r'posts', PostsViewSet)
# post_router.register(r'posts', PostsViewSet, basename="basename")  # if no queryset in ViewSet
