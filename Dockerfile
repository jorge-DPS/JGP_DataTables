FROM python:3.8-slim as image_base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDEBUG 1

RUN apt-get update \
  && apt-get install -y default-libmysqlclient-dev build-essential \
  && apt-get install -y libmariadb-dev-compat libmariadb-dev \
  #&& apt-get install -y libmariadbclient-dev \
  && apt install -y mariadb-server \
  && apt-get remove -y default-libmysqlclient-dev build-essential \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext bash \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && rm ~/.cache/pip -rf

#libreria de datatables 
RUN pip install djangorestframework-datatables
#libreria para excel
RUN pip install pandas openpyxl


#sudo apt-get install python3-dev

#RUN apt-get install -y libmysqlclient-dev
RUN apt-get install gcc

#COPY ./requirements /requirements
#RUN pip install --no-cache-dir -r /requirements/common.txt

COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/common.txt

COPY compose/post-build /post-build
RUN sed -i 's/\r//' /post-build
RUN chmod +x /post-build

EXPOSE 8000
WORKDIR /app

#
#  D E V E L O P M E N T
#
FROM image_base as development

RUN pip install -r /requirements/testing.txt
RUN pip install -r /requirements/develop.txt


#COPY compose/entrypoint /entrypoint
#RUN sed -i 's/\r//' /entrypoint
#RUN chmod +x /entrypoint


COPY compose/start-dev /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

# C E L E R Y

COPY compose/celery/dev/start-celeryworker /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY compose/celery/dev/start-celerybeat /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY compose/celery/dev/start-flower /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


#ENTRYPOINT ["/entrypoint"]

#
#  C I / C D
#
FROM development as ci_cd

RUN apk add make build-base
RUN pip install docker-compose awscli

# VER DATABASE
# docker exec -it simicrofin_db_1 mysql -uevillanueva -p
