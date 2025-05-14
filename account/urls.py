from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns=[
    #previous login
    #path('login/',views.user_login,name='login'),

    #login and logout urls 
    
    #'password-change/',
        #auth_views.PasswordChangeView.as_view(),
       # name='password_change'
    #),
    #path(
       # 'password-change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'
    
    #),
    ##path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    #path('password-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(),name='passwword_reset_complete')


    path('',views.dashboard,name='dashboard'),
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('login/', views.user_login, name='login'),
    path('edit/',views.edit,name='edit'),

]