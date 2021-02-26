# -*- coding:utf-8 -*-

# 9-11:导入Admin类

from user import Admin

admin = Admin('tom', 'jerry')
admin.describe()
admin.privileges.show_privileges()
