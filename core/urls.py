from django.contrib import admin
from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('berita/', views.berita_list, name='berita_list'),
    path('berita/<int:id>/', views.detail_berita, name='detail_berita'),
    path('dosen/', views.dosen_list, name='dosen_list'),
    path('akademik/', views.akademik, name='akademik'),
    path('akademik/<slug:slug>/', views.akademik_detail, name='akademik_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)