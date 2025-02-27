from django.urls import path
from .views import certificate_detail,certificate_form_view, certificate_list_view, download_certificate_pdf,login_view, signup_view, logout_view

urlpatterns = [
    path('', certificate_form_view, name='certificate_form'),
    path('certificates/', certificate_list_view, name='certificate_list'),
    path('download/<int:pk>/', download_certificate_pdf, name='download_certificate_pdf'),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path('certificates/<int:id>/', certificate_detail, name='certificate_detail'),
]
