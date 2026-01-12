from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from core.selectors import IncidentSelector
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
@require_http_methods(["GET"])
def list_incidents(request):
    """View to display all incidents."""
    incidents = IncidentSelector.get_all_incidents()
    context = {
        'incidents': incidents,
    }
    return render(request, 'list_incidents.html', context)
