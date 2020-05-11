from django.urls import path, include
from django.contrib.auth.decorators import login_required
from dashboard.views import financial, administration

from . import views

urlpatterns = [
    path('', login_required(views.index), name='dashboard_index'),
    path('financial/', include([
        path('shares', login_required(financial.shares), name='dashboard_financial_shares'),
    ])),
    path('administration/', include([
        path('users', login_required(administration.users), name='dashboard_administration_users'),
        path('groups', login_required(administration.groups), name='dashboard_administration_groups'),
    ]))
]
