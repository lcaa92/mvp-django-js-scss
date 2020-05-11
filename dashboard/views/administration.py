from django.shortcuts import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def users(request):
    print('users')
    return HttpResponseRedirect(reverse('dashboard_index'))


def groups(request):
    print('groups')
    return HttpResponseRedirect(reverse('dashboard_index'))
