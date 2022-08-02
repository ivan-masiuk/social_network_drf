from django.urls import path, include

from .routers import post_router

urlpatterns = [
    path('', include(post_router.urls)),

    # path('api/women/', WomenViewSet.as_view({'get': "list"})),  # 127.0.0.1:8000/api/women
    # path('api/women/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]
