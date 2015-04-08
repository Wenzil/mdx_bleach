# -*- coding: utf-8 -*-
from mdx_bleach.extension import BleachExtension


VERSION = '0.0.2'


def makeExtension(**kwargs):
    return BleachExtension(**kwargs)
