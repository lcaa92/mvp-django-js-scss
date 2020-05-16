from django.shortcuts import reverse, render


# Create your views here.
def panel(request):
    ctx = {
        'ctx_js': {
            'data_url': reverse('data_dashboard_financial_users')
        }
    }
    return render(request, 'dashboard/financial/panel.html', ctx)


def shares(request):
    ctx = {
        'ctx_js': {
            'data_url': reverse('data_dashboard_financial_users')
        }
    }
    return render(request, 'dashboard/financial/shares.html', ctx)
