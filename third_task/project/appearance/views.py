from rest_framework.response import Response
from rest_framework.views import APIView

from appearance import logic


class AppearanceView(APIView):
    def post(self, request):
        data = request.data
        total_time = logic.appearance(data)
        return Response({"total_time": total_time})
