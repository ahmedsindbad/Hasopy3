# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Poet, MyDate, Purpose, Sea, Poem, Verse, Publisher
# Register your models here.
admin.site.register(Poet)
admin.site.register(MyDate)
admin.site.register(Purpose)
admin.site.register(Sea)
admin.site.register(Poem)
admin.site.register(Verse)
admin.site.register(Publisher)
