"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home',views.index),
    path('service',views.service),
    path('service1', views.service1),
    path('contact',views.contact),
    path('gallery', views.gallery),
    path('about', views.about),
    path('about1', views.about1),
    path('portfolio', views.portfolio),
    path('success', views.success, name='success'),
    # path('success_page', views.success_page),
    path('login_view', views.login_view),
    path('user_dashboard', views.user_dashboard),

    path('admin_view_photographer', views.admin_view_photographer),
    path('photographer_dashboard', views.photographer_dashboard),
    # path('update/<int:d>',views.update),
    path('cameraman_profile',views.cameraman_profile),
    path('cameraman_update_profile/', views.cameraman_update_profile),
    # path('accept_photographer/<int:d>',views.accept_photographer,name='accept_photographer'),
    path('reg', views.reg),
    path('view_user', views.view_user),
    path('confirm_accept/<int:photographer_id>', views.accept_photographer),
    path('confirm_reject/<int:photographer_id>', views.reject_photographer),
    path('user_profile/', views.user_profile),
    path('update_userprofile/', views.update_userprofile),
    path('show_images', views.show_images),
    path('show_imagess', views.show_imagess),
    path('upload_image/', views.upload_image),
    path('add_photographer', views.add_photographer),
    # path('uregister/<i>/<int:Photographer_id>', views.uregister),
    path('uregister/<str:i>/<int:Photographer_id>/', views.uregister, name='uregister'),


    # path('approve_booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('show_photographer', views.show_photographer),
    # path('savebooking', views.save_booking),

    # path('save_booking', views.save_booking),
    path('logout',views.logout),
    path('sg', views.sg),
    # path('payment/<i>', views.payment),
    path('payment/<str:i>/', views.payment, name='payment'),
    path('view_portfolio/<int:i>', views.view_portfolio),
    # path('payment_success', views.payment_success),
    # path('success_page1', views.success_page1),
    # path('product', views.product),
    path('product', views.product),
    # path('product_display',views.display),
    path('product_display', views.product_display, name='product_display'),
    # path('update/<int:d>', views.update),
    path('update/<int:d>/', views.update, name='update_product'),
    path('delete_product/<int:d>', views.delete_product),
    path('viewproduct', views.viewproduct),
    path('add_to_cart/<int:d>', views.add_to_cart),
    path('carts', views.carts),
    path('forgot_pswd', views.forgot_password),
    # path('reset/<token>', views.reset_password),
    path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
    path('accept_booking', views.accept_booking, name='accept_booking'),
    path('approve_booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('photographer_aproval/', views.photographer_aproval, name='photographer_aproval'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback_thank_you', views.feedback_thank_you),
    path('admin_feedback_view/', views.admin_feedback_view, name='admin_feedback_view'),
    path('delete_feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('all_photographers_images/', views.show_all_photographers_images, name='all_photographers_images'),
    path('all_photographers_imagess/', views.show_all_photographers_imagess, name='all_photographers_imagess'),
    path('mark_work_completed/', views.mark_work_completed, name='mark_work_completed'),
    path('admin_notification/', views.admin_notification, name='admin_notification'),
    path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    # path('admin_dashboard', views.admin_dashboard),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)