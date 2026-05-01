from rest_framework import serializers
from django.conf import settings
from .models import Property, Reservation
from useraccount.serializers import UserDetailSerializer
class PropertiesListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'price_per_night',
            'image_url'
        )

    def get_image_url(self, obj):
        if obj.image:
            return f"{settings.WEBSITE_URL}{obj.image.url}"
        return ""
    

class PropertiesDetailSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    landlord = UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Property
        fields = (
            'id',
            'title',
            'description',
            'price_per_night',
            'image_url',
            'bedrooms',
            'bathrooms',
            'guests',
            'landlord'
        )
    def get_image_url(self, obj):
        if obj.image:
            return f"{settings.WEBSITE_URL}{obj.image.url}"
        return ""
    
class ReservationsListSerializer(serializers.ModelSerializer):
    property= PropertiesListSerializer(read_only=True, many=False)
    
    class Meta:
        model = Reservation 
        fields=(
            'id','start_date','end_date','number_of_nights','total_price','property'
        )