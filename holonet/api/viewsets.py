from celery import result as celery_result
from celery import states
from celery.registry import tasks
from celery.utils import get_full_cls_name
from celery.utils.encoding import safe_repr
from django.conf import settings
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from holonet.domains.models import Domain


class InformationViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        return Response({
            'domains': Domain.list_domains(),
            'server_email': settings.SERVER_EMAIL,
            'restricted_endpoint': '%s@%s' % (settings.RESTRICTED_PREFIX, settings.MASTER_DOMAIN),
            'system_aliases': settings.SYSTEM_ALIASES,
            'admins': settings.ADMINS,
            'system_owner': settings.SYSTEM_OWNER,
            'sender_whitelist': settings.SENDER_WHITELIST_ENABLED,
            'domain_whitelist': settings.DOMAIN_WHITELIST_ENABLED,
        })


class TaskViewSet(ViewSet):

    def list(self, *args, **kwargs):
        return Response({
            'regular': tasks.regular().keys(),
            'periodic': tasks.periodic().keys()
        })

    def create(self, *args, **kwargs):
        task_id = kwargs.get('pk')
        result = celery_result.AsyncResult(task_id)
        state, retval = result.state, result.result
        response_data = dict(id=task_id, status=state, result=retval)
        if state in states.EXCEPTION_STATES:
            traceback = result.traceback
            response_data.update({'result': safe_repr(retval),
                                  'exc': get_full_cls_name(retval.__class__),
                                  'traceback': traceback})

        return Response(response_data)
