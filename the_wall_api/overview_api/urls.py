from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('profiles/', views.ProfilesView.as_view()),
    re_path('profiles/(?P<prof_number>\d+)/days/(?P<day>\d+)', views.IcePerProfilePerDayView.as_view()),
    re_path('profiles/(?P<prof_number>\d+)/overview/(?P<day>\d+)', views.CostPerProfilePerDay.as_view()),
    re_path('profiles/overview/(?P<day>\d+)', views.TotalCostPerDayView.as_view()),
    re_path('profiles/overview/', views.TotalCostView.as_view()),
]
