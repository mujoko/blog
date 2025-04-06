from django.urls import path
from .views import post_abc_list, post_cde_detail  # new

urlpatterns = [
    path("post/<int:pk>/", post_cde_detail, name="post_detail"),  # new
    path("", post_abc_list, name="home"),
]
