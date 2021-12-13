from .models import Profile,Project
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =('prof_photo','bio','phone_number')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields = ('')