from django.urls import path
from . import views


urlpatterns = [
    path('form/', views.form, name='form'),
    path('table/', views.table, name='table'),
    path('e_otp/', views.e_otp, name='e_otp'),
    path('ph_otp/', views.ph_otp, name='ph_otp'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('loginform/', views.loginform, name='loginform'),
    path('view/<int:id>/', views.view, name='view'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('email/', views.email, name='email'),
    path('logout/', views.logout_view, name='logout'),
]



# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)