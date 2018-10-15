

### [官方]("https://hub.docker.com/_/postgres/")

* start a postgres instance
    * $ docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
* connect to it from an application
    * $ docker run --name some-app --link some-postgres:postgres -d application-that-uses-postgres
    * Via psql 
        * $ docker run -it --rm --link some-postgres:postgres postgres psql -h postgres -U postgres
* Create by docke-compose 
-- stack.yml --
'''
# Use postgres/example user/password credentials
version: '3.1'
services:
  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: example
      POSTGRES_USER: postgres 
  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
'''
* 執行檔案
> $ docker stack deploy -c stack.yml postgres 
> $ docker-compose -f stack.yml up

------

# GET Image by Dockerfile
$ docker build -t howard:psql .
# Run Container 
$ docker run -itd --name psql howard/psql:0.0.1
# 進入容器的 bash
$ docker exec -it psql sh
$ docker exec -it psql /bin/bash