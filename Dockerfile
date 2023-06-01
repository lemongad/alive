FROM mcr.microsoft.com/playwright/python:v1.33.0-jammy


# 复制文件

COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py
# 设置权限
RUN chmod a+x /entrypoint.sh /main.py
# 设置端口
EXPOSE 80

# 运行脚本
CMD ["/entrypoint.sh"]
