from rest_framework import serializers
from .models import Course, User, Teacher, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'user_telegram_id']

class TeacherSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Teacher

class StudentSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'subject', 'complexity', 'theory_practice_ratio']
