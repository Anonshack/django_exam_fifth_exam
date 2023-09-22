from django.urls import path
from .views import (HomePageView,
                    BlogDetailView,
                    CreatePostView,
                    BlogDeleteView,
                    # my_view,
                    BlogUpdateView,
                    )

urlpatterns = [
    path('new/post/', CreatePostView.as_view(), name='new_post'),
    path('post/<int:pk>/edit ', BlogUpdateView.as_view(), name='post_edit'),
    path('clay/', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/delete ', BlogDeleteView.as_view(), name='post_delete'),
]