# Image python3.7
FROM python:3.7
# 環境更新並安裝 netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean
# 設定工作路徑
WORKDIR /usr/src/app
# dev install
COPY ./requirements.txt /usr/src/app/requirements.txt
# 更新 pip 並安裝 插件
Run pip install --upgrade pip && \
    pip install -r requirements.txt
# 複製 entrypoint.sh 到 workdir
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
# 更新權限
RUN chmod +x /usr/src/app/entrypoint.sh
# 複製 app -> workdir
COPY . /usr/src/app

EXPOSE 8080

# entrypoint 
CMD ["/usr/src/app/entrypoint.sh"]
