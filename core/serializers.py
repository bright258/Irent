# rest framework dependencies
from rest_framework import serializers

# from rest_framework.parsers import MultiPartParser


# models
from .models import (
    House
)

# serializers
class HouseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    image_url = serializers.ReadOnlyField()
    video_url = serializers.ReadOnlyField()
    video = serializers.FileField()

    
   
    class Meta:
        model = House
        fields = '__all__'
        
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('video_url')
        representation.pop('image_url')
        # representation.append('image_url')
        return representation

    
    


        
