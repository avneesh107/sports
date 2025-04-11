from django.urls import path
from . import views


urlpatterns=[
    path("",views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
     path('events/', views.event_list, name='event_list'),
    path('join-event/<int:event_id>/', views.join_event, name='join_event'),
    path('register/', views.register, name='register'),
    path("logout",views.logout_view),
    path("team/",views.team_list,name='team'),
    path("result/",views.result,name='result'),
    path("match/",views.Matches,name='match'),
    path("college/<int:college_id>/participants/", views.college_participants_view, name="college_participants"),
    path("contest/<int:pk>",views.cont_team,name='contest_team'),
    path('team/<int:pk>/members/', views.team_members, name='team_members'),
    path("Matches/",views.User_Matches,name='User_Matches'),
    path("results_view/",views.user_results_view,name='user_results_view'),
    path("upload/", views.bulk_match_upload_view, name="upload_matches"),
]
