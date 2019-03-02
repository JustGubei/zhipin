from django.shortcuts import render
import pymongo
from django.core.paginator import Paginator


def zhaopin(request):
    client = pymongo.MongoClient()
    db = client['BOSS']
    info = db.boss.find()


    info1 = []
    for i in info:
        info1.append(i)
        # info.append(i)
    # print(info1)
    limit = 30
    paginator = Paginator(info1, limit)
    page_num = request.GET.get('page', 1)  # 从url中获取页码参数
    loaded = paginator.page(page_num)


    return render(request,'zp_info.html',{'info1':loaded})