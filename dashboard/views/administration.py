from django.shortcuts import reverse, render
from django.http import HttpResponseRedirect


# Create your views here.
def users(request):
    print('users')
    return render(request, 'dashboard/administration/users.html')


def groups(request):
    print('groups')
    return HttpResponseRedirect(reverse('dashboard_index'))
