from rest_framework import serializers

class MailSerializer(serializers.Serializer):
    smtp_server = serializers.CharField()
    port = serializers.IntegerField()
    server_login = serializers.CharField()
    server_password = serializers.CharField()
    sender = serializers.EmailField()
    recipient = serializers.EmailField()
    subject = serializers.CharField()
    body = serializers.CharField()
