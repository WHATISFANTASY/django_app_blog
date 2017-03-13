from django.db import models
from django.contrib import admin  # 定义默认的admin站点


class Article(models.Model):
    STATUS_CHOICES = (('d', 'Draft'), ('p', 'Published'),)

    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, help_text="可选，如果为空则摘取正文的前54个字符")

    views = models.PositiveIntegerField('浏览量', default=0)
    views = models.PositiveIntegerField('点赞数', default=0)

    topped = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)

    # 文章的分类，ForeignKey即数据库中的外键。外键的定义是：如果数据库中某个表的列的值是另外一个表的主键。
    # 外键定义了一个一对多的关系，这里即一篇文章对应一个分类，而一个分类下可能有多篇文章。
    # on_delete=models.SET_NULL表示删除某个分类（category）后该分类下所有的Article的外键设为null（空）

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    name = models.CharField('分类', max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)

    def __str__(self):
        return self.name



