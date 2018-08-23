# coding=utf-8
import tempfile

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from elasticsearch import Elasticsearch
from emails.models import EMailPost
import zipfile
from wsgiref.util import FileWrapper

HOST = '127.0.0.1'
PORT = '9200'

def email_view(request):
    # form = EMailIndexSearchForm(request.GET)
    # emails = form.search()
    q = request.GET.get('q')
    emails = []
    query = {
        "query": {
            "bool": {
                "must": {
                    "query_string": {
                        "fields": ["text", "description"],
                        "query": q,
                        "default_operator": "AND"
                    }
                },
            },
        },
        "fields": ["id", "sender", "created", "text", "description"],
        "highlight": {
            "fields": {
                "_all": {
                    "pre_tags": ["<em>"],
                    "post_tags": ["</em>"],
                },
                "text": {"number_of_fragments": 0},
                "description": {"number_of_fragments": 0}
            },
        }
    }
    es = Elasticsearch()
    if q:
        result = es.search(body=query, index='email')
        for email in result['hits']['hits']:
            email_obj = {
                'created': email['fields']['created'][0],
                'text': email['fields']['text'][0],
                'description': email['fields']['description'][0],
                'sender': email['fields']['sender'][0],
                'id': email['_id'],
            }
            highlight = email.get('highlight')
            if highlight:
                for key in highlight:
                    email_key = email_obj[key]
                    for new_key in highlight[key]:
                        email_key = email_key.replace(new_key.replace('<em>', '').replace('</em>', ''), new_key)
                    email_obj[key] = email_key
            emails.append(email_obj)

    return render_to_response('email.html', {'emails': emails})

def index(request):
    return HttpResponse("Hello, World!")

@csrf_exempt
def zip_ajax(request):
    ids = request.GET.getlist('ids[]') or request.GET.getlist('ids')
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for model in EMailPost.objects.filter(id__in=ids):
        name = '%s, %s %s.html' %(model.description, model.sender, model.created)
        f = open(name, 'w')
        f.write(model.text)
        f.close()
        archive.write(name, name)
    archive.close()
    lens = temp.tell()
    temp.seek(0)
    wrapper = FileWrapper(temp)
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=test.zip'
    response['Content-Length'] = lens
    return response
