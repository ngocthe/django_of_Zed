# myapp/urls.py
from django.urls import path
from . import views_user, views_login, views_filesharing
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),

                  # login urls
                  path('', views_login.login_view, name='login'),
                  path('test/', views_login.test_view, name='test'),
                  path('logout/', views_login.logout_view, name='logout'),
                  path('home/', views_login.home_view, name='home'),

                  # filesharing urls
                  path('file_list/', views_filesharing.file_list_view, name='file_list'),
                  path('upload/', views_filesharing.upload_file_view, name='upload_file'),
                  path('download/<int:file_id>/', views_filesharing.DownloadFileView.as_view(), name='download_file'),
                  path('delete/<int:file_id>/', views_filesharing.DeleteFileView.as_view(), name='delete_file'),

                  # user urls
                  path('sw_list/', views_user.sw_list, name='sw_list'),
                  path('add_new_member/', views_user.add_new_member, name='add_new_member'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
