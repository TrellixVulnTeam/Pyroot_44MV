# file meant for converting the models data into json format

from .models import Task   # importing the table
from rest_framework import serializers  # import serializers
from django.contrib.auth import get_user_model  # user model for creating the user


class UserSerializers(serializers.ModelSerializer):  # class for the user
    password = serializers.CharField(write_only=True)   # password field - write only

    def create(self, validated_data):     # user method to validate
        user = get_user_model().objects.create(   # creates the user
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # sets and validates

        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class TaskSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:   # class meant for linking the table and attributes needed to be in json output
        model = Task
        fields = ('id', 'task_name', 'task_description', 'date_created', 'completed', 'image')   # id refers to the primary key



