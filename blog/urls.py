from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import BlogCreateView, PostList, PostDeleteView, PostUpdateView, SignUpView, PasswordsChangeView


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('change_password/',   PasswordsChangeView.as_view(template_name='password_change.html',), name='change_password'),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='login.html'), name='change_password_done'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('new/', BlogCreateView.as_view(), name='post_new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/', views.add_comment, name='post_detail'),

]
