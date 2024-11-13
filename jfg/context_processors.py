from django.conf import settings

def global_settings(request):

    """
    Inject global settings variables into the context.
    """

    return {
        'COMPANY_NAME': settings.COMPANY_NAME
    }