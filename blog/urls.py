#tokensite/blog/urls.py
from rest_framework.authtoken import views as authviews
from django.urls import path

from django.conf.urls import include, url
from blog import views

urlpatterns = [
	path('api-token-auth/', authviews.obtain_auth_token),
	path('post/', views.AllPost.as_view()),
]