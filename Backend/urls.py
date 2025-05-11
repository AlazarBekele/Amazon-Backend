from django.urls import path
from .views import (
    index,
    sell_index,
    login_here,
    SignForm
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ('', index, name='index'),
    path ('sell/', sell_index, name='sell'),
    path ('login/', login_here, name='login'),
    path ('signin/', SignForm, name='SignIn')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)