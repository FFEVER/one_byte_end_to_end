from django.conf.urls import url
from user_auth.views import UserRegistrationView
from user_auth.views import UserLoginView


urlpatterns = [
    url(r"^signup", UserRegistrationView.as_view()),
    url(r"^signin", UserLoginView.as_view()),
]

