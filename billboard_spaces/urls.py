"""
URL configuration for billboard_spaces project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from utils.views import docs_schema_view, index_view

handler400 = 'utils.views.handler_400'
handler404 = 'utils.views.handler_404'
handler500 = 'utils.views.handler_500'

# change admin site header
admin.site.site_header = "BillBoard Spaces Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('apps.accounts.urls')),
    path('billboards/', include('apps.billboards.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('posts/', include('apps.posts.urls')),
    path('billboard-bookings/', include('apps.bookings.urls')),
    path('requirements/', include('apps.requirements.urls')),
    path('maintenance/', include('apps.maintenance.urls')),
    path('events/', include('apps.events.urls')),
    path('subscriptions/', include('apps.subscriptions.urls')),
    path('social-auth/', include('drf_social_oauth2.urls', namespace='drf')),

    path('', index_view, name='index-view'),
    path('docs/', docs_schema_view.with_ui('swagger', cache_timeout=0)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
