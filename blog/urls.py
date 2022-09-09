from . import views
from django.urls import path

urlpatterns = [
    # '' represents empty string and returns an result from ListPost
    path('', views.PostList.as_view(), name='home'),
    # <slug> in the brackets captures the values from the url and returns the post details
    path('<slug:slug>/', views.PostDetails.as_view(), name='details_post'),
]
