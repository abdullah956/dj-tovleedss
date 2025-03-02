from django.urls import path
from .views import  track_equipment,all_records_view ,track_operator,validate_now, certificate_form_view,login_view, logout_view

urlpatterns = [
    path('form/', certificate_form_view, name='certificate_form'),
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('validate-now', validate_now, name='validate-now'),
    path('track_operator/', track_operator, name='track_operator'),
    path('track_equipment/', track_equipment, name='track_equipment'),
    path("all/", all_records_view, name="all_records"),
]
