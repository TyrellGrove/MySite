
from django.urls import path
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', MySite.views.home, name='home'),
    # url(r'^MySite/', include('MySite.MySite.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),    
]