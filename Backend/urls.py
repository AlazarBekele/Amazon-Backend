from django.urls import path
from .views import (
    index,
    sell_index,
    login_here,
    SignForm,
    card_one,
    Seller_account
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ('', index, name='index'),
    path ('sell/', sell_index, name='sell'),
    path ('login/', login_here, name='login'),
    path ('signin/', SignForm, name='SignIn'),
    path ('gaming_accessories/', card_one, name='gaming_accessories'),
    path ('Seller/<int:id>/', Seller_account, name='seller')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)