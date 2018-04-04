# -*- coding: utf-8 -*-
from urllib.parse import quote;
import string;

# 定义一个常量类
class _constant:
    class ConstError(TypeError):pass;
    class ConstCaseError(ConstError):pass;

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("can't change const %s" % key);
        if not key.isupper():
            raise self.ConstCaseError("const name '%s' is not all uppercase " % key);
        self.__dict__[key] = value;

const = _constant
const.URL = "http://baike.baidu.com"

class IllegalException(Exception):
    def __init__(self, parameter, para_value):
        err = 'The parameter "{0}" is not legal:"{1}"'.format(parameter,para_value)
        Exception.__init__(self, err)
        self.parameter = parameter
        self.para_value = para_value

def function_parse_url_utf8(url):
    return quote(url,safe=string.printable,encoding='utf-8');


def baidubaike_paging_url(limit,index):
    #百度百科的分页
    #?limit = 1200 & index = 1 & offset = 0  # gotoList
    if limit <= 0 or index <= 0:
        raise IllegalException('limit,index',str(limit)+','+str(index));
    offset = (index - 1)*limit;
    var = '?limit='+str(limit)+'&index='+str(index)+'$offset='+str(offset)+'#gotoList'
    return var;












