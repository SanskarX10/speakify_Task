from django.urls import path
from .views import index, user_login, signup, inside_base, user_logout,update_status


urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('signup/', signup, name='signup'),
    path('base/', inside_base, name='base'),
    path('logout/', user_logout, name='logout'),
    path('update_status/', update_status, name='update_status')
    # path('update_online_status/', update_online_status, name='update_online_status')
]