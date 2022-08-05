# in built django dependencies
from django.contrib import admin

# others
from .models import (

    Country,
    State,
    City,
    House,
    CustomUser,
    # ImageAlbum,
    # Image
)

# admin
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(House)
admin.site.register(CustomUser)
# admin.site.register(ImageAlbum)
# admin.site.register(Image)

