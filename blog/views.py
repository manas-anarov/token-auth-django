#tokensite/blog/views.py

from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import postSerializer
from blog.models import Post

from rest_framework.generics import (
	ListAPIView, 
	)


class AllPost(ListAPIView):
	serializer_class = postSerializer
	queryset = Post.objects.all()

	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)
