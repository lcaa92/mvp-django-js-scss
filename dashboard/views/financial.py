from django.shortcuts import reverse, render


# Create your views here.
def panel(request):
    ctx = {
        'ctx_js': {
            'table_id': 'tablePanel',
            'data_url': reverse('data_dashboard_financial_users')
        }
    }
    return render(request, 'dashboard/financial/panel.html', ctx)


def shares(request):
    ctx = {
        'ctx_js': {
            'datatable': {
                'table_shares': {
                    'data_url': reverse('data_dashboard_financial_users'),
                    'columnsTitle': ['Código', 'Empresa', 'Valor Atual'],
                    'columnsValue': ['code', 'company', 'price'],
                },
            }
        }
    }
    return render(request, 'dashboard/financial/shares.html', ctx)
