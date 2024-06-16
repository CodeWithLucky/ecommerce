from django.shortcuts import render
from . models import Maintenance

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        maintenance = Maintenance.objects.first()
        if maintenance and maintenance.is_under_maintenance and not request.user.is_staff:
            return render(request, 'maintenance.html')
        response = self.get_response(request)
        return response
