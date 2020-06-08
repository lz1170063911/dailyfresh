from apps.user.views import RegisterView, ActiveView, LoginView, LoginoutView, UserInfoView, UserOrderView, AddressView
from django.urls import re_path

urlpatterns = [
    re_path(r'^register$', RegisterView.as_view(), name='register'),  # 注册
    re_path(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 用户激活
    re_path(r'^login$', LoginView.as_view(), name='login'),  # 登录
    re_path(r'^loginout$', LoginoutView.as_view(), name='loginout'),  # 注销登录
    re_path(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    re_path(r'^$', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    re_path(r'^$', AddressView.as_view(), name='address'),  # 用户中心-地址页
]
