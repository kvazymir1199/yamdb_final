from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.views import UserViewSet, get_token, signup
from .v1.views import (
    TitleViewSet, CategoryViewSet,
    GenreViewSet, ReviewViewSet,
    CommentViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', get_token, name='get_token'),
]
