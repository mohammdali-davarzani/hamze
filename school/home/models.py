from django.db import models
from django.contrib.auth.models import User


class TopStudents(models.Model):
    GRADE_CHOICES = (
        (0, 'دهم'),
        (1, 'یازدهم'),
        (2, 'داوزدهم')
    )
    firstName = models.CharField(verbose_name="نام", max_length=200, null=False, blank=False)
    lastName = models.CharField(verbose_name="نام خانوادگی", max_length=200, null=False, blank=False)
    grade = models.SmallIntegerField(choices=GRADE_CHOICES, verbose_name="پایه تحصیلی", max_length=1, null=False, blank=False)
    rank = models.CharField(verbose_name="رتبه", max_length=200, null=False, blank=False)


class Post(models.Model):
    STATUS = (
        (0,"Draft"),
        (1,"Publish")
    )
    title = models.CharField(verbose_name="عنوان", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="slug", max_length=200, unique=True)
    author = models.ForeignKey(User, verbose_name="نویسنده", on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(verbose_name="تاریخ آخرین آپدیت", auto_now= True)
    content = models.TextField(verbose_name="محتوا")
    created_on = models.DateTimeField(verbose_name="تاریخ ساخت", auto_now_add=True)
    status = models.IntegerField(verbose_name="وضعیت", choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title