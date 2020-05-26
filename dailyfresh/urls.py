"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from apps.user import urls as user_urls
from apps.cart import urls as cart_urls
from apps.order import urls as order_urls
from apps.goods import urls as goods_urls

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^user/', include(user_urls), name='user'),  # 用户模块
    re_path(r'^cart/', include(cart_urls), name='cart'),  # 购物车模块
    re_path(r'^order/', include(order_urls), name='order'),  # 订单模块
    re_path(r'^', include(goods_urls), name='goods')  # 用户模块
]
