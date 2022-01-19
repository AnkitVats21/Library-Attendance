from django.urls import re_path

from .views import LoginView, AttendanceView, LogoutView, ExitAllView

urlpatterns = [
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^$', AttendanceView.as_view(), name='attendance'),
    re_path(r'^exit_all$', ExitAllView.as_view(), name='exit_all')
]
