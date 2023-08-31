from django.urls import path
from .views import index, category, contact, about, single_post

urlpatterns = [
    path("", index, name="index"),
    path("category/", category, name="category"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("<slug:slug>/", single_post, name="detail"),
]
