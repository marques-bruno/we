from django.urls import path

from test_app.views import (
    indexView,
    postFriend, 
    checkNickName
)


urlpatterns = [
    # ... other urls
    path('kapoue/', indexView),
    path('post/ajax/friend', postFriend, name = "post_friend"),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname")

]
