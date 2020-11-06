from django.db import models

# Create your models here.
from django.db import models
# 导入内建的用户模型
from django.contrib.auth.models import User
# 用于处理时间相关事务
from django.utils import timezone
from django.urls import reverse

# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveBigIntegerField(default=0)
    # 内部类 class Meta 用于给 model 定义元数据

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

