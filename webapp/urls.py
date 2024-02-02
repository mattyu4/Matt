from django.urls import path
from . import views
from .views import create_member, edit_member, delete_member

urlpatterns = [
    path ('', views.index, name="home_page"),
    path ('about/', views.aboutPage, name="about_page"),
    path ('login/', views.login, name="login_page"),
    path ('program/', views.program, name="program_page"),
    path('program/create/', views.program_create, name="program_create"),
    path('program/edit/<int:programID>', views.program_edit, name="program_edit"),
    path('program/delete/<int:programID>', views.program_delete, name="program_delete"),
    path ('member/', views.member, name="member_page"),
    path ('programmemberslist/', views.programmemberslist, name="programmemberslist_page"),
    path ('userslist/', views.userslist, name="userslist_page"),
    path('create-member/', create_member, name='create_member'),
    path('edit-member/<int:membership_number>/', edit_member, name='edit_member'),
    path('delete-member/<int:membership_number>/', delete_member, name='delete_member'),
]