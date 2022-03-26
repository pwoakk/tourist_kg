
from django.urls import path
from accounts.views import logout_user, register, sign_in

urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register')
]
