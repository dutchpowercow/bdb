from rest_framework import serializers
from cp.pdns_models import Domains


class DomainSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    linenos = serializers.BooleanField(required=False)


    def create(self, validated_data):
        """
        Create and return a new `domain` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `domain` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
        


class RecordSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    type = serializers.CharField(required=True, allow_blank=False, max_length=100)
    content = serializers.CharField(required=True, allow_blank=False, max_length=100)
    ttl = serializers.CharField(required=False, allow_blank=True)
    prio = serializers.CharField(required=False, allow_blank=True)
    


    def create(self, validated_data):
        """
        Create and return a new `domain` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `domain` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.content = validated_data.get('content', instance.content)
        instance.ttl = validated_data.get('ttl', instance.ttl)
        instance.prio = validated_data.get('prio', instance.prio)
        instance.save()
        return instance
