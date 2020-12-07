from .models import employee
from rest_framework import serializers

class employeeSerializer(serializers.ModelSerializer):
    

    class Meta():
        model=employee
       # fields='all' fields = ('request_id', 'last_seed', 'available_flights')
        fields=('id','username')
