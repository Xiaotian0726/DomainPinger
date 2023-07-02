# DomainPinger

## 环境配置
- Windows
- Python 3.6
```shell
# Python 依赖
pip install -r requirements.txt

# 数据库
python manage.py makemigrations
python manage.py migrate

# 创建管理员账户
python manage.py createsuperuser
```

## 启动
终端一启动 Django 服务器：
```shell
python manage.py runserver
```

终端二启动定时 ping 任务：
```shell
python manage.py runscript -v3 domainPinger.tasks
```

## 访问
管理后台：
```
localhost:8000/admin/
```

域名列表：
```
localhost:8000/domains/
```