# coding=utf-8
from django import template
from dateutil.relativedelta import *
from datetime import *

register = template.Library()


@register.filter(name='todate')
def todate(value):
    td = date.today()
    dif = (value - td).days
    rl = relativedelta(td, value)
    if dif >= 0:
        ret = u'Còn lại '
        if rl.years:
            ret += str(-rl.years) + u' năm '
        if rl.months:
            ret += str(-rl.months) + u' tháng '
        if rl.days:
            ret += str(-rl.days) + u' ngày'
    else:
        ret = u'Quá hạn '
        if rl.years:
            ret += str(rl.years) + u' năm '
        if rl.months:
            ret += str(rl.months) + u' tháng '
        if rl.days:
            ret += str(rl.days) + u' ngày'
    return ret


@register.filter(name='tocolor')
def tocolor(value):
    td = date.today()
    dif = (value - td).days
    if dif >= 0:
        return u'green'
    else:
        return u'red'


@register.filter(name='tonum')
def tonum(value):
    td = date.today()
    dif = (value - td).days
    return dif
