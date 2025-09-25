from django.urls import path
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog', views.blog, name="blog"),
    path('blog/<int:pk>/',views.posting, name="posting"),
    path('blog/new_post/', views.new_post, name = "new_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)