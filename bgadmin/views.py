# coding:UTF-8
from django.shortcuts import render
from django.http import JsonResponse
from bgadmin.models import TestUser
from common.utils.utils_log import log
import uuid
import os
from django.conf import settings
from django.db import transaction
from common.utils.utils_import_excel import import_excel_util
from common.utils.utils_file_download import big_file_download
from common.utils.utils_file_upload import upload_file
from slugify import slugify

# Create your views here.


def bgadmin_home(request):
    """跳转到后台首页"""
    return render(request, "bgadmin/index.html", {})


def import_excel(request):
    """Excel导入"""
    try:
        if request.method == "POST":
            excel_file = request.FILES.get("excel_file", None)
            if excel_file:
                # 自定义存储路径
                rollfileName = "uploadfile/"
                rollfilePath = os.path.join(settings.MEDIA_ROOT, rollfileName)
                # 获取文件名后缀
                filetype = excel_file.name.split(".")[-1]
                # 生成随机字符串加后缀的文件名
                filename = str(uuid.uuid1()) + '.' + filetype
                file_path = rollfilePath + filename
                # 打开文件存储路径
                of = open(file_path, 'wb+')
                # 向指定路径写入文件
                for chunk in excel_file.chunks():
                    of.write(chunk)  # 写入内容
                of.close()  # 关闭连接
                log.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> start import excel >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                obj_dict = {0: "name", 1: "name_cn", 2: "position", 3: "qq", 4: "phone", 5: "tel"}
                obj_list = import_excel_util(file_path, obj_dict)
                os.remove(file_path)  # 读取完成后，删除文件
                with transaction.atomic():
                    count = 0
                    for obj in obj_list:
                       user_tmp = TestUser.objects.filter(name=obj['name'])
                       if user_tmp:
                           log.info("obj is exist")
                           continue
                       else:
                           TestUser.objects.create(
                               name=obj['name'],
                               password="ps123456",
                               name_cn=obj['name_cn'],
                               position=obj['position'],
                               qq=obj['qq'],
                               phone=obj['phone'],
                               tel=obj['tel']
                           )
                           count+=1
                    log.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> insert successful ,insert %s data >>>>>>>>" % count)
                log.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> end import excel >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                result = {"status": 1, "msg": "成功"}
            else:
                raise Exception("文件不存在")
        elif request.method == "GET":
            return render(request, "bgadmin/import_Excel.html", {})
        else:
            raise Exception("请求异常")
    except Exception, e:
        log.exception("import_excel %s" % e)
        result = {"status": 0, "msg": "fail"}
    return JsonResponse(result)


def down_loda_templates(request):
    """模板下载"""
    templates_file = os.path.join(settings.MEDIA_ROOT, "template_file/data_template.xls")
    return big_file_download(templates_file, "data_template1.xls")


def import_psuser_roster(request):
    """
        @description 花名冊导入功能
        @param request: 请求
    """
    try:
        if request.method == "POST":
            # 第一步：获取文件导入文件，将导入文件上传到服务器临时目录
            excel_file = request.FILES.get("excel_file", None)
            # 第二步：判断请求中是否存在待上传文件，存在则将文件上传到服务临时目录
            if excel_file:
                file_path = upload_file("temp_file/",excel_file)
                # 第三步：文件上传成功后先将Excel数据解析
                if file_path:
                    log.info(">>>>>>>>>>>>>>>>>> start import excel data >>>>>>>>>>>>")
                    # 姓名、部门、岗位、职级、出生日期、性别、入职日期、转正日期、合同到期日期、离职日期
                    obj_dict = {0: "name", 1: "dept", 2: "position", 3: "qq", 4: "phone", 5: "tel"}
                    obj_list = import_excel_util(file_path, obj_dict)
                else:
                    log.info(">>>>>>>>>>>>>>>>> 导入文件%s上传失败 >>>>>" % excel_file.name)
                    raise Exception("网络异常，请稍后重试")
            else:
                raise Exception("文件不存在")
    except Exception, e:
        log.exception(">>>>>>>>>>>>>>> import_psuser_roster raise >>>>>>>>>>>>>>>>>>>>>")
        result = {"status": 0, "msg": "fail"}
    return JsonResponse(result)


def pdf_preview(request):
    return render(request, "bgadmin/pdf-pre/demo.html")