# posts/urls.py

from django.urls import path

from .views import ModelPageView, CreatePostView, PhotoPageView, PhotoCreatePostView  # new
import posts.views

# from .filters import Userfilter
#post url


urlpatterns = [
    path('model/', ModelPageView.as_view(), name='model'),
    path('model/post/', CreatePostView.as_view(), name='post'),
    path('model/detail/<int:post_id>/', posts.views.detail, name="detail"),

    path('model/filter/orient/', posts.views.filter_orient, name="filter_orient"),
    path('model/filter/western/', posts.views.filter_western, name="filter_western"),
    path('model/filter/classic/', posts.views.filter_classic, name="filter_classic"),
    path('model/filter/modern/', posts.views.filter_modern, name="filter_modern"),

    path('photo/', PhotoPageView.as_view(), name="photo"),
    path('photo/post/', PhotoCreatePostView.as_view(), name="photo_post"),
    path('photo/detail/<int:photo_id>/', posts.views.photo_detail, name="photo_detail"),

    path('photo/filter/orient/', posts.views.photo_filter_orient, name="photo_filter_orient"),
    path('photo/filter/western/', posts.views.photo_filter_western, name="photo_filter_western"),
    path('photo/filter/classic/', posts.views.photo_filter_classic, name="photo_filter_classic"),
    path('photo/filter/modern/', posts.views.photo_filter_modern, name="photo_filter_modern"),

    path('', posts.views.home, name="home"),

]