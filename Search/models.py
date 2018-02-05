# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
# Create your models here.
class Poet(models.Model):
    picture = models.CharField(max_length=200, verbose_name="عنوان الصورة")
    name = models.CharField(max_length=200, verbose_name="الشاعر")

    class Meta:
        verbose_name_plural = "الشاعر"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class MyDate(models.Model):
    myDate = models.CharField(max_length=200, verbose_name="العصر")

    class Meta:
        verbose_name_plural = "العصر"

    def __str__(self):
        return self.myDate


@python_2_unicode_compatible
class Purpose(models.Model):
    purpose = models.CharField(max_length=200, verbose_name="الغرض")

    class Meta:
        verbose_name_plural = "الغرض"

    def __str__(self):
        return self.purpose


@python_2_unicode_compatible
class Sea(models.Model):
    sea = models.CharField(max_length=200, verbose_name="البحر")

    class Meta:
        verbose_name_plural = "بحر القصيدة"

    def __str__(self):
        return self.sea


@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=200, verbose_name="دار النشر")

    class Meta:
        verbose_name_plural = "دار النشر"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Poem(models.Model):
    poet = models.ForeignKey(Poet, on_delete=models.CASCADE, verbose_name="الشاعر")
    myDate = models.ForeignKey(MyDate, on_delete=models.CASCADE, verbose_name="العصر")
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE, verbose_name="الغرض")
    sea = models.ForeignKey(Sea, on_delete=models.CASCADE, verbose_name="البحر")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="دار النشر")
    title = models.CharField(max_length=200, verbose_name="عنوان القصيدة")

    class Meta:
        verbose_name_plural = "القصيدة"

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Verse(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, verbose_name="عنوان القصيدة")
    text = models.CharField(max_length=200, verbose_name="البيت")

    class Meta:
        verbose_name_plural = "بيت القصيدة"

    def __str__(self):
        return self.text
