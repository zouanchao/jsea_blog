# coding:UTF-8
from common.utils.utils_log import log
from django.conf import settings
import uuid
import os


def upload_file(up_file, file_path):
    """
        @description 上传文件
        @param up_file: 待上传文件
        @param file_path: 文件存储路径
    """
    try:
        # 拼接文件存放路径
        roll_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
        # 获取文件名后缀
        file_type = up_file.name.split(".")[-1]
        # 生成随机字符串加后缀的文件名【新的文件名】
        filename = str(uuid.uuid1()) + '.' + file_type
        # 文件最终存放路径
        file_path = roll_file_path + filename
        # 打开文件流
        of = open(file_path, 'wb+')
        # 向指定路径写入文件
        for chunk in up_file.chunks():
            of.write(chunk)  # 写入内容
        of.close()  # 关闭连接
        # 返回文件上传后存放的路径
        return file_path
    except Exception, e:
        log.error(">>>>>>>>>>>>>>> 文件上传失败,原因：%s >>>>>>>>>>>>>>>>>>" % e)
    return None
