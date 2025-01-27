from rest_framework import serializers
from apps.user.models import User

class CoinInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'balance','wallet']
        read_only_fields = [ 'balance']
