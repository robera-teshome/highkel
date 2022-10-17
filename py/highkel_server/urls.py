"""highkel_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from highkel_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('appointment', views.appointment, name='appointment'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('blog_sidebar', views.blog_sidebar, name='blog_sidebar'),
    path('contact', views.contact, name='contact'),
    path('error_404', views.error_404, name='error_404'),
    path('login', views.login, name='login'),
    path('portfolio_category', views.portfolio_category, name='portfolio_category'),
    path('portfolio_details', views.portfolio_details, name='portfolio_details'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('posts_by_author', views.posts_by_author, name='posts_by_author'),
    path('posts_by_date', views.posts_by_date, name='posts_by_date'),
    path('posts_by_tag', views.posts_by_tag, name='posts_by_tag'),
    path('pricing_plan', views.pricing_plan, name='pricing_plan'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('recover_password', views.recover_password, name='recover_password'),
    path('register', views.register, name='register'),
    path('service_details', views.service_details, name='service_details'),
    path('privacy_policy', views.portfolio_category, name='portfolio_category'),
    path('service_one', views.service_one, name='service_one'),
    path('service_two', views.service_two, name='service_two'),
    path('team', views.team, name='team'),
    path('terms_of_service', views.terms_of_service, name='terms_of_service'),
    path('testimonials', views.testimonials, name='testimonials'),

]
     
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)