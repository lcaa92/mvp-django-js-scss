from django.shortcuts import reverse, render
from django.http import HttpResponseRedirect


# Create your views here.
def users(request):
    ctx = {
        'ctx_js': {
            'data_url': reverse('data_dashboard_administration_users')
        }
    }
    return render(request, 'dashboard/administration/users.html', ctx)


def groups(request):
    ctx = {
        'ctx_js': {
            'data_url': reverse('data_dashboard_administration_groups')
        }
    }
    return render(request, 'dashboard/administration/groups.html', ctx)
