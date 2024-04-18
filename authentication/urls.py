from django.urls import path
from .views import *
from django.urls import re_path
from rest_framework_simplejwt import views as jwt_views
from authentication import views

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('changepassword/(?P<user_id>[0-9]+)/$',Changepassword.as_view(),name='changepassword'),
    path('userregister/',UserRegister.as_view(),name='userregister'),
    path('userlist/',UserList.as_view(),name='userlist'),
    path('userbyid/<int:pk>/',UserById.as_view(),name='userbyid'),
    path('refreshtoken/',jwt_views.TokenRefreshView.as_view(),name ='refreshtoken'),
    path('access_token/',jwt_views.TokenObtainPairView.as_view(),name ='access token'),
]



