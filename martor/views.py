import json
import os
import uuid
from django.conf import settings
from django.http import HttpResponse
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from martor.utils import LazyEncoder
from .api import imgur_uploader
from .settings import MARTOR_MARKDOWNIFY_FUNCTION
from .utils import LazyEncoder

def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif'
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Bad image format.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            if image._size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps({
                    'status': 405,
                    'error': _('Maximum image file is %(size) MB.') % {'size': to_MB}
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(settings.MEDIA_URL, def_path)

            data = json.dumps({
                'status': 200,
                'link': img_url,
                'name': image.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))

def markdownfy_view(request):
    if request.method == 'POST':
        markdownify = import_string(MARTOR_MARKDOWNIFY_FUNCTION)
        return HttpResponse(markdownify(request.POST['content']))
    return HttpResponse(_('Invalid request!'))


@login_required
def markdown_imgur_uploader(request):
    """
    Makdown image upload for uploading to imgur.com
    and represent as json to markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            data = imgur_uploader(image)
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))


@login_required
def markdown_search_user(request):
    """
    Json usernames of the users registered & actived.

    url(method=get):
        /martor/search-user/?username={username}

    Response:
        error:
            - `status` is status code (204)
            - `error` is error message.
        success:
            - `status` is status code (204)
            - `data` is list dict of usernames.
                { 'status': 200,
                  'data': [
                    {'usernane': 'john'},
                    {'usernane': 'albert'}]
                }
    """
    data = {}
    username = request.GET.get('username')
    if username is not None \
            and username != '' \
            and ' ' not in username:
        users = User.objects.filter(
            Q(username__icontains=username)
        ).filter(is_active=True)
        if users.exists():
            data.update({
                'status': 200,
                'data': [{'username': u.username} for u in users]
            })
            return HttpResponse(
                json.dumps(data, cls=LazyEncoder),
                content_type='application/json')
        data.update({
            'status': 204,
            'error': _('No users registered as `%(username)s` '
                       'or user is unactived.') % {'username': username}
        })
    else:
        data.update({
            'status': 204,
            'error': _('Validation Failed for field `username`')
        })
    return HttpResponse(
        json.dumps(data, cls=LazyEncoder),
        content_type='application/json')
