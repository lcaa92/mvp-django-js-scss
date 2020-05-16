from django.urls import path, include
from django.contrib.auth.decorators import login_required
from dashboard.views import financial, administration, data

from . import views

urlpatterns = [
    path('', login_required(views.index), name='dashboard_index'),
    path('data/', include([
        path('administration/', include([
            path('users', login_required(data.users), name='data_dashboard_administration_users'),
            path('groups', login_required(data.groups), name='data_dashboard_administration_groups'),
        ]))
    ])),
    path('financial/', include([
        path('panel', login_required(financial.panel), name='dashboard_financial_panel'),
        path('shares', login_required(financial.shares), name='dashboard_financial_shares'),
    ])),
    path('administration/', include([
        path('users', login_required(administration.users), name='dashboard_administration_users'),
        path('groups', login_required(administration.groups), name='dashboard_administration_groups'),
    ]))
]
