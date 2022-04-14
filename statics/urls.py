from django.urls import include, path
# from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView, LogoutView

# from tutorial__ import views_
from statics.views import Static8FView, Static6FView


from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/statics/login')


app_name = "statics"

urlpatterns = [
    path('', login_redirect, name='login_redirect'),
    # path('', views_.login_redirect, name='login_redirect'),
    path('login/', LoginView.as_view(template_name='statics/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='statics/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    # path('profile/', views.view_profile, name='view_profile'),
    # url(r'^profile/$', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/', views.view_profile, name='view_profile'),
    # (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                #  {'document_root': settings.MEDIA_ROOT}),
    path('static8F/', Static8FView.as_view(), name='static8F'),
    path('static6F/', Static6FView.as_view(), name='static6F'),
]