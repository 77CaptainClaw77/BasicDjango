"""firstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from home.views import home_page
from home.views import index_page
from home.views import addition_page

from account import views as a_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', index_page),
    path('<int:n1>/<int:n2>',addition_page),
    path('login/',a_views.user_login,name="login"),
    path('logout/',a_views.user_logout,name="logout"),
    path('signup/',a_views.register,name="register"),
    # path('home/delete/<id>',delete_query),
    # path('home/edit/<id>',edit_query),
    # path('home/create/',create_query),
    
]
