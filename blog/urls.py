from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog, name="Blog"),
    path('git-github-post', git_github_post, name="Git")
    
]