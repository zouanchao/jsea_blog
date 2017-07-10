# coding:UTF-8

from django.test import TestCase

from slugify import slugify

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

print slugify("测试").replace("-", "")
