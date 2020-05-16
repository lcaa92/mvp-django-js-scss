import json
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User, Group


# Create your views here.
def users(request):
    users = User.objects.all()
    dataUsers = [{
        'id': user.id,
        'username': user.username,
        'superuser': user.is_superuser,
        'active': user.is_active,
    } for user in users]

    data = {
        "data": dataUsers
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def groups(request):
    groups = Group.objects.all()

    dataGroups = [{
        'id': group.id,
        'name': group.name,
        'count_users': group.user_set.count(),
    } for group in groups]

    data = {
        "data": dataGroups
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def shares(request):
    data = {
        'msg': 'Sucesso!'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
