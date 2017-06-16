# coding:UTF-8
import datetime
import calendar
# 获取上月时间，作为查询统计条件
year = datetime.date.today().year  # 年
month = int(datetime.date.today().month) - 1  # 上月
mon_fist_day = datetime.date(year=year, month=month, day=1)  # 统计开始时间
first_day_week_day, month_range = calendar.monthrange(year, month)
# 统计月时间
mon_end_day = datetime.date(year=year, month=mon_fist_day.month, day=month_range)
# 统计结束时间【统计月下月第一天】
mon_last_day = mon_end_day + datetime.timedelta(days=1)
print mon_end_day
print mon_fist_day
print mon_last_day