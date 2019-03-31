import json


def get_param(request):
    try:
        return json.loads(request.body)
    except Exception as e:
        if request.method == 'GET':  # pragma: no cover
            return request.GET.dict()
        return request.POST.dict()
