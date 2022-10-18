from ExTime.models import *
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games

        fields = ["pk", "game_name", "developer_id", "icon"]

class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer

        fields = ["pk", "dev_name", "description", "icon"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ["pk", "user_name","icon" ,"email", "password","is_seller"]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service

        fields = ["pk", "gameid", "service_name", "user_id","amount","price","description","type_id"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews

        fields = ["pk", "serviceid", "user_id","theme","review_text","rating",]

class RScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewscreenshot

        fields = ["pk", "reviewid", "pic_name"]

class SScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicescreenshot

        fields = ["pk", "serviceid", "pic_name"]

class STypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicetype

        fields = ["pk", "typename"]