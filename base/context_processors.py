from django.contrib.auth.models import User
from auditlog.models import LogEntry


def add_log_entries(request):
    if request.user and not request.user.is_anonymous:
        return {'log_entries': LogEntry.objects.filter(actor=request.user).order_by('-timestamp')[:5]}
    return {}
