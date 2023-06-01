#!/usr/bin/env python3

import os
import subprocess

YONGHU = os.environ.get('YONGHU', '')
PW = os.environ.get('PW', '')
URL = os.environ.get('URL', '')
URL2 = os.environ.get('URL2', '')


# 生成配置
with open('/main.py', 'r') as f:
    content = f.read()
content = content.replace('${YONGHU}', YONGHU)
content = content.replace('${PW}', PW)
content = content.replace('${URL}', URL)
content = content.replace('${URL2}', URL2)
with open('/main.py', 'w') as f:
    f.write(content)
os.chmod('/main.py', 0o755)
with open('/main.py', 'r') as f:
    print(f.read())

# 循环执行脚本
a = 1
while True:
    print(f'第{a}轮保活开始！===')
    subprocess.run(['python3', '/main.py'])
    print(f'第{a}轮保活结束！')
    a += 1
    time.sleep(10)
