# 离线脚本 做完最好注释，防止重复运行
import os.path
import sys

import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order.settings')  # manage.py文件中有
django.setup()  # 伪造让django启动

from web import models
from utils.encrypt import md5

# models.Administrator.objects.create(
#     username='zhangsan',
#     password=md5("zhangsan"),
#     mobile="13646285916",
# )
#
# #创建级别
# level_object = models.Level.objects.create(title="VIP", percent=90)
#
# models.Customer.objects.create(
#     username='lisi',
#     password=md5("lisi"),
#     mobile="15850791986",
#     level=level_object,
#     creator_id="1",
# )
for i in range(1, 302):
    models.Customer.objects.create(
        username='lisi-{}'.format(i),
        password=md5("lisi-{}".format(i)),
        mobile="18888888888",
        level_id=4,
        creator_id="1",
    )
