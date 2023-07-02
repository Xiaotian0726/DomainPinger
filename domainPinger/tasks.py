import requests
import schedule
import time

from domainPinger import models


def update():
    # 获取所有网站对象
    domains = models.Domain.objects.all()

    # 对于每个网站，进行 ping 测试并更新数据库
    for domain in domains:
        # 使用 requests 库进行 ping 测试
        try:
            response = requests.get(domain.domain_url)
            ping_ret = response.status_code
            print('Get valid ping_ret:', ping_ret)
        except requests.exceptions.RequestException:
            ping_ret = 'RequestException'
            print('Catch exception!')

        # 更新数据库中的 ping_ret 字段
        domain.ping_ret = ping_ret
        domain.save()


schedule.every().minute.do(update)

while True:
    schedule.run_pending()
    time.sleep(1)  # 每隔一秒检查队列里是否有待执行任务
