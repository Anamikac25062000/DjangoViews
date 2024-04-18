from django.db.models import fields
from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "title",
        ]

    def save(self):
        reg = Tag(title=self.validated_data["title"].title())
        reg.save()


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["text", "user_id", "time_stamp", "status"]

    def save(self):
        reg = Snippet(
            text=self.validated_data["text"],
            title=self.validated_data["title"].title(),
            user_id=self.validated_data["user_id"],
        )
        reg.save()


class SnippetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["text", "tag_id", "user_id", "time_stamp", "status"]

class SnippetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"

class SnippetDetailsSerializer(serializers.ModelSerializer):
    tag_id = TagsSerializer()
    class Meta:
        model = Snippet
        fields ="__all__"

class SnippetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields ="__all__"

class TagsSerializer(serializers.ModelField):
    class Meta:
        model = Tag
        fields = "__all__"