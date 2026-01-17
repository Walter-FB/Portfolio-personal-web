from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views

from django.conf import settings

urlpatterns = [
    # Páginas core
    path('', core_views.home, name="home"),
    path('about-me/', core_views.about, name="about"),
    path('contact/', core_views.contact, name="contact"),

    # Portfolio
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),

    # Comparador de Café (Railway)
    path('chequear/', core_views.test_conexion, name="chequear"),

    # Admin
    path('admin/', admin.site.urls),
]

# Para servir media en modo debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
