from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from accounts.models import CustomUser

@api_view(['GET'])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    # Assuming you already have a PostSerializer
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
