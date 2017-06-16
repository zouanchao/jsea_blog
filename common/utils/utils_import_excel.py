# coding: UTF-8
import os
import django
import xlrd
from common.utils.utils_log import log
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jsea_admin.settings")  # project_name 项目名称
django.setup()


def import_excel_util(file_path, obj_dict):
    """
    Excel 导入工具类
    :param file_path: excel文件对象访问路径地址
    :param obj_dict:  要存入的model对象属性
    :return: 
    """
    try:
        excel_data = xlrd.open_workbook(file_path)  # 读取Excel文件对象
        excel_sheet = excel_data.sheet_by_name(u'Sheet1')  # 根据sheet名称获取工作表
        # row_values = excel_sheet.row_values(0)   # 读取第一行数据【表头标题】【数组长度等于总列数】
        # col_values = excel_sheet.col_values(0)   # 读取第一列数据
        # th_valus = [{index: val} for index, val in enumerate(row_values)] # 表头数据
        row_count = excel_sheet.nrows  # 读取所有行数
        col_count = excel_sheet.ncols  # 读取列数
        model_list = []  # 将excel数据封装成list
        for row_n in range(1, row_count):  # 循环1到总行数
            model_dict = {}  # 将单行数据封装成一个数据字典
            for col_n in range(0, col_count):  # 循环0到总列数
                row_col_data = excel_sheet.cell(row_n, col_n).value  # 读取列数据
                model_dict[obj_dict[col_n]] = row_col_data  # 字典封装
            model_list.append(model_dict)  # 将单行数据封装到list中作为返回值范围
        return model_list
    except Exception, e:
        log.exception(e)
    return None
