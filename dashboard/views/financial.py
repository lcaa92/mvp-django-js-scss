from django.shortcuts import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def shares(request):
    print('shares')
    return HttpResponseRedirect(reverse('dashboard_index'))
