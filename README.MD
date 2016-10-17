** Instalation

- Install Redis on your machine
- Create virtual environment using Python 2.7
- pip install -r requirements/base.txt

- redis-server /usr/local/etc/redis.conf
- celery -A zapping worker -B -l info