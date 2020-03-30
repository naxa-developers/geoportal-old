from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response


class InterestsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Requests:
        GET : list of interests

    Url Parameters:
        None

    Query Parameters:
        lang_code (str): Language code, eg eng, ar-dz

    Body Parameters:
        None

    Returns:
        list of interests
    """
    serializer_class = InterestsSerializer
    queryset = Interest.objects.all()

    def get_queryset(self):
        lang_code = self.request.query_params.get('lang_code')
        activate_language(lang_code)
        return self.queryset


