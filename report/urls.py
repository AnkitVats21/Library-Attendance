from django.urls import re_path


from .views import AdminView, MonthlyReportFormView, TrueReaderFormView, TrueReadeDetailView

urlpatterns = [
    re_path(r'^report/', AdminView.as_view(), name='report-admin'),
    re_path(r'^monthly-report/$', MonthlyReportFormView.as_view(),
        name='monthly-report'),
    re_path(r'^true-reader-report/$', TrueReaderFormView.as_view(),
        name='true-reader-report'),
    re_path(r'^true-reader-detail/$', TrueReadeDetailView.as_view(),
        name='true-reader-detail'),
]