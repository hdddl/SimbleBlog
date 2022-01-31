from django.db import models


# Create your models here.

class blog(models.Model):
    # ���±���
    title = models.CharField(max_length=50, unique=True)
    # ��������
    author = models.CharField(max_length=50, default='Dongliu')
    # ���ʴ���
    visits = models.BigIntegerField(default=0)
    # ����ժҪ
    abstract = models.TextField(null=True)
    # ��������
    content = models.TextField()
    # ���·���ʱ��
    pubdate = models.DateTimeField()
    # �����޸�ʱ��
    modify_date = models.DateTimeField()
    # ���·���
    category = models.CharField(max_length=50, null=True)
    # ���±�ǩ
    tags = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


class micro_blog(models.Model):
    # ����ʱ��
    pubdate = models.DateField()
    # ��������
    content = models.TextField()

    def __str__(self):
        return self.pubdate
