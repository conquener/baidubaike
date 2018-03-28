# -*- coding: utf-8 -*-

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







