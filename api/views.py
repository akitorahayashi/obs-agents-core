from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def health_check(request):
    """Simple health check endpoint."""
    return JsonResponse({"status": "ok"})


@api_view(["GET"])
def api_root(request):
    """Root API endpoint."""
    return Response({"message": "Welcome to obs-agents-core API"})
