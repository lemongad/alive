#!/bin/bash

YONGHU=${YONGHU}
PW=${PW}
# 生成配置
sed -i "s#\S[YONGHU]#S{YONGHU]#g" /main.py
sed -i "s#[PW]#S[PW]#g" /main.py
sed -i "s#\S[URL]#S{URL]#g" /main.py
sed -i "s#\${URL2]#S[URL2]#g" /main.py
chmod +x /main.py
cat /main.py

# 循环执行脚本
a=1
while true; do
  echo "第${a}轮保活开始！==="
  python3 /main.py
  echo "第${a}轮保活结束！"
  let a+=1
  sleep 10
done
