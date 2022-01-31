from django.shortcuts import render
from django.http import JsonResponse
from article.models import blog, micro_blog


# ��վ��ҳ
def index(request):
    return render(request, "index.html")


# ��ȡ����Ŀ¼��Ĭ��һҳΪ10����
def api_content(request):
    # ��ȡ�������ͣ����ͻ�����΢��
    content_type = request.GET.get("type")
    # ��ȡҳ�棬Ĭ��һҳ10��
    page = request.GET.get("page")
    # ������ӦJSON
    response_data = {
        "status": False,
        "msg": "",
        "data": []
    }
    # ��֤���Ͳ����Ƿ���ȷ
    if content_type != "blog" and content_type != "micro_blog":
        response_data['msg'] = "parameter type worry"
        return JsonResponse(response_data)
    # ��֤pageҳ������Ƿ����
    if page.isdigit() and int(page) > 0:
        page = int(page)
    else:
        response_data['msg'] = "parameter page worry"
        return JsonResponse(response_data)
    # �޸���Ӧ״̬
    response_data['status'] = True
    if content_type == "blog":
        items = blog.objects.values_list("title", "pubdate", "abstract")
        # �ض��ķ���
        category = request.GET.get("category")
        # �ض��ı�ǩ
        tags = request.GET.get("tag")
        # ����
        if category:
            items = items.filter(category=category)
        if tags:
            items = items.filter(tags=tags)
        # ��������
        items = items[(page - 1) * 10: 10 * page]
        for i in items:
            title, date, text = i
            response_data['data'].append(
                {"title": title, "date": date, "text": text}
            )
        return JsonResponse(response_data)
    else:
        items = micro_blog.objects.values_list("pubdate", "content")[(page - 1) * 15: 10 * page]
        for i in items:
            date, text = i
            response_data['data'].append(
                {"date": date, "text": text}
            )
        return JsonResponse(response_data)


# ��ȡ��������API
def api_blog(request):
    # ��ȡ���±���
    title = request.GET.get("title")
    # ������ӦJSON
    response_data = {
        "status": False,
        "msg": "",
        "data": []
    }
    item = blog.objects.values_list("content").filter(title=title)
    if item.exists():
        response_data['status'] = True
        response_data['data'].append({"text": item[0][0]})
        return JsonResponse(response_data)
    else:
        response_data['msg'] = "article is not find"
        return JsonResponse(response_data)


# ��ȡcategories
def api_categories(request):
    # ������ӦJSON
    response_data = {
        "status": True,
        "msg": "",
        "data": [],
    }
    categories = blog.objects.values("category")
    for i in categories:
        i = i['category']
        if i not in response_data['data']:
            response_data['data'].append(i)
    return JsonResponse(response_data)


# ��ȡtags
def api_tags(request):
    # ������ӦJSON
    response_data = {
        "status": True,
        "msg": "",
        "data": [],
    }
    tags = blog.objects.values("tags")
    for i in tags:
        i = i['tags'].split(',')
        for j in i:
            if j not in response_data['data']:
                response_data['data'].append(j)
    return JsonResponse(response_data)
