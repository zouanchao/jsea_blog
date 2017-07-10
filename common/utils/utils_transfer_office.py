# coding:UTF-8
from win32com import client as wc
import os
import time
import random
import MySQLdb
import re
from utils_log import log


def word_to_html(dir):
    """
    批量把文件夹的word文档转换成html文件
    金山WPS调用，抢先版的用KWPS，正式版WPS
    :param dir: 
    :return: 
    """
    word = wc.Dispatch('KWPS.Application')
    print("******************** Info: 开始转换！%s********************" % word)
    log.info("******************** Info: 开始转换！%s********************" % word)
    for path, subdirs, files in os.walk(dir):
        for word_file in files:
            word_full_name = os.path.join(path, word_file)
            log.info(">>>>>>>>>>>>>>>>>>> wordFile %s >>>>>>>>" % word_full_name)
            doc = word.Documents.Open(word_full_name)
            word_file2 = unicode(word_file, "gbk")
            dot_index = word_file2.rfind(".")
            if(dot_index == -1):
                print("******************** ERROR: 未取得后缀名！********************")
                log.info("******************** ERROR: 未取得后缀名！********************")
            file_suffix = word_file2[(dot_index + 1):]
            if (file_suffix == "doc" or file_suffix == "docx"):
                fileName = word_file2[: dot_index]
                htmlName = fileName + ".html"
                htmlFullName = os.path.join(unicode(path, "UTF-8"), htmlName)
                print u'生成了html文件：' + htmlFullName
                doc.SaveAs(htmlFullName, 8)
                doc.Close()
    word.Quit()
    print("******************** Info: 转换完成！********************")
    log.info("******************** Info: 转换完成！********************")


if __name__ == '__main__':
    try:
        word_to_html('d:/word')
    except Exception, e:
        print("****************** Error:%s **************" % e)
        log.error("****************** Error:%s **************" % e)