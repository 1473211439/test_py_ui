#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 17:38
# @Author  : jing.yang

import  requests

if __name__ == "__main__":
    r = requests.get("https://www.baidu.com/")
    print(r.text)