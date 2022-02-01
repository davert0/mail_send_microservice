from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import MailSerializer
import mail.services as services

MAIL_RESPONSES = {
    '200': 'Mail sent successfully.',
    '400': 'Incorrect request format.',
    '500': 'An error occurred, could not send email.' 
}



class SendMail(APIView):

    @swagger_auto_schema(
        request_body=MailSerializer,
        operation_description="Sends email.",
        responses=MAIL_RESPONSES
    )
    def post(self, request):
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            smpt_server = serializer.validated_data['smtp_server']
            port = serializer.validated_data['port']
            server_login = serializer.validated_data['server_login']
            server_password = serializer.validated_data['server_password']
            sender = serializer.validated_data['sender']
            recipient = serializer.validated_data['recipient']
            subject = serializer.validated_data['subject']
            body = serializer.validated_data['body']

            server = services.MailServer(smpt_server, port)
            server.authenticate(server_login, server_password)

            try:
                server.send_mail(sender, recipient, subject, body)
                return Response({
                    'status': 'success',
                    'data': { 'message': 'Mail sent successfully.'}
                }, status=status.HTTP_200_OK)
            except:
                return Response({
                    'status': 'failure',
                    'data': { 'message': 'An error occurred, could not send email.'}
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response({
                'status': 'failure',
                'data': { 'message': 'Incorrect request format.', 'errors': serializer.errors}
            }, status=status.HTTP_400_BAD_REQUEST)


    
