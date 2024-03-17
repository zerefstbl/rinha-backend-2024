from rest_framework.exceptions import APIException

from rest_framework import status

from django.utils.translation import gettext_lazy as _

class InsufficientLimit(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __init__(self):
        self.detail = {
            'error': _("Limite Insuficiente."),
        }
