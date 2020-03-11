from django.conf.urls import url
from user_auth.views import UserRegistrationView


urlpatterns = [
    url(r"^signup", UserRegistrationView.as_view()),
]

