# in built django dependencies
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# views
from .views import (
    HouseList,
    RetrieveHouse,
    UpdateHouse,
    CreateHouse,
    DeleteHouse
)

# urls
urlpatterns = [ 
    path('list/house/', HouseList.as_view()),
    path('house/<int:pk>/', RetrieveHouse.as_view()),
    path('update/house/<int:pk>/', UpdateHouse.as_view()),
    path('create/house/', CreateHouse.as_view()),
    path('delete/house/<int:pk>/', DeleteHouse.as_view())

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)