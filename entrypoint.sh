#!/usr/bin/env python3

YONGHU=${YONGHU}
PW=${PW}
URL=${URL}
URL2=${URL2}

# 生成配置
sed -i "s#\${YONGHU}#$YONGHU#g" /main.py
sed -i "s#\${PW}#$PW#g" /main.py
sed -i "s#\${URL}#$URL#g" /main.py
sed -i "s#\${URL2}#$URL2#g" /main.py
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
