# vim:ts=4:sts=4:sw=4:expandtab

import json

import django.conf
from django.db import transaction
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie

from kolejka.common import KolejkaLimits
from kolejka.server.task.models import Task

@transaction.atomic
def dequeue(request):
    if request.method == 'POST':
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
#TODO: Check that user can get tasks
        tasks = list()
        params = json.loads(str(request.read(), request.encoding or 'utf-8')) 
        concurency = params.get('concurency', 1)
        limits = KolejkaLimits()
        limits.load(params.get('limits', dict()))
        tags = set(params.get('tags', list()))
        resources = KolejkaLimits()
        resources.update(limits)
        image_usage = dict()

        available_tasks = Task.objects.filter(assignee=None).order_by('time_create')[0:100]
        for t in available_tasks:
            if len(tasks) > concurency:
                break
            tt = t.task()
            if len(tasks) > 0 and tt.exclusive:
                continue
            if not set(tt.requires).issubset(tags):
                continue
            if resources.cpus is not None and (tt.limits.cpus is None or tt.limits.cpus > resources.cpus):
                continue
            if resources.memory is not None and (tt.limits.memory is None or tt.limits.memory > resources.memory):
                continue
            if resources.swap is not None and (tt.limits.swap is None or tt.limits.swap > resources.swap):
                continue
            if resources.pids is not None and (tt.limits.pids is None or tt.limits.pids > resources.pids):
                continue
            if resources.storage is not None and (tt.limits.storage is None or tt.limits.storage > resources.storage):
                continue
            if resources.image is not None:
                if tt.limits.image is None:
                    continue
                image_usage_add = max(image_usage.get(tt.image, 0), tt.limits.image) - image_usage.get(tt.image, 0)
                if image_usage_add > resources.image:
                    continue
            if resources.workspace is not None and (tt.limits.workspace is None or tt.limits.workspace > resources.workspace):
                continue
            if resources.network is not None and (tt.limits.network is None or tt.limits.network and not resources.network):
                continue
            if resources.time is not None and (tt.limits.time is None or tt.limits.time > resources.time):
                continue

            tasks.append(tt.dump())
            t.assignee = request.user
            t.save()
            if resources.cpus is not None:
                resources.cpus -= tt.limits.cpus
            if resources.memory is not None:
                resources.memory -= tt.limits.memory
            if resources.swap is not None:
                resources.swap -= tt.limits.swap
            if resources.pids is not None:
                resources.pids -= tt.limits.pids
            if resources.storage is not None:
                resources.storage -= tt.limits.storage
            if resources.image is not None:
                resources.image -= image_usage_add
                image_usage[tt.image] = max(image_usage.get(tt.image, 0), tt.limits.image)
            if resources.workspace is not None:
                resources.workspace -= tt.limits.workspace
            if tt.exclusive:
                break

        response = dict()
        response['tasks'] = tasks
        return JsonResponse(response)
    return HttpResponseNotAllowed(['POST'])
