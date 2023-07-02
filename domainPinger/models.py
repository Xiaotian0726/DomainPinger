from django.db import models


class Domain(models.Model):
    domain_url = models.CharField(max_length=255, verbose_name="域名")
    ping_ret = models.CharField(max_length=255, verbose_name="ping返回值")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        verbose_name = verbose_name_plural = 'tb_domain'
