from django.shortcuts import reverse, render


# Create your views here.
def panel(request):
    ctx = {}
    return render(request, 'dashboard/financial/panel.html', ctx)


def shares(request):
    ctx = {
        'ctx_js': {
            'data_url': reverse('data_dashboard_administration_groups')
        }
    }
    return render(request, 'dashboard/financial/shares.html', ctx)
