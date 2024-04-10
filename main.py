# Convert a string to a Class object in Python

import sys


class Employee():
    pass


def get_class(class_name):
    return getattr(sys.modules[__name__], class_name)


cls = get_class('Employee')
print(cls)  # 👉️ <class '__main__.Employee'>