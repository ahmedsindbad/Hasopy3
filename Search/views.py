# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.utils.encoding import python_2_unicode_compatible
import os
from .forms import VerseForm
import sqlite3


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.htm'


class AboutPageView(TemplateView):
    template_name = 'about.htm'


class SearchPageView(TemplateView):
    template_name = 'search.htm'

    class PoertyPageView(TemplateView):
        template_name = 'poetry.htm'


class TestPageView(TemplateView):
    template_name = 'testform.htm'

def varse(request):
    form = VerseForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'index.htm', context)

def tosearchpage(request):
    searchWord = request.POST.get('text', '')
    try:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
        c = conn.cursor()
        c.execute(
            "SELECT * FROM Search_poem "
            "LEFT OUTER JOIN Search_verse ON (Search_poem.id = Search_verse.poem_id) "
            "LEFT OUTER JOIN Search_poet ON (Search_poem.poet_id = Search_poet.id) "
            "WHERE (Search_verse.text like '%" + searchWord + "%') group by text", )
        result = list(c)
        conn.commit()
        conn.close()
    except ValueError:
        print("Oops!  That was no valid Data.  Try again...")
    context = {
        'searchWord': searchWord,
        'result': result,
    }
    return render(request, 'Search.htm', context)

def poetryshow(request,poet_id):
    try:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
        c = conn.cursor()
        c.execute(
            "select text from Search_verse where  poem_id =" + poet_id + ";", )
        result = list(c)
        conn.commit()
        # for w in result:
        #     print(w[0])
        conn.close()
    except ValueError:
        print("Oops!  That was no valid Data.  Try again...")
    context = {
        'result': result,
    }
    return render(request, 'poetry.htm', context)

def getalldata(p_id = '1'):
    try:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
        c = conn.cursor()
        c.execute(
            "SELECT Search_poem.id, Search_poem.title, Search_poet.name, Search_poet.picture "
            "FROM Search_poem LEFT OUTER JOIN Search_poet ON (Search_poet.id = Search_poem.poet_id) "
            "WHERE (Search_poem.id = " + p_id + ");", )
        result = list(c)
        conn.commit()
        # print(result)
        conn.close()
    except ValueError:
        print("Oops!  That was no valid Data.  Try again...")
    return result

# def varse(request):
#     form = VerseForm(request.POST or None)
#     value = str()
#     try:
#         if form.is_valid():
#             for key, value in form.cleaned_data.items():
#                 print(key, value)
#         conn = sqlite3.connect(
#             os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
#         c = conn.cursor()
#         c.execute("select text from Search_verse where text like '%" + value + "%';", )
#         result = list(c)
#         conn.commit()
#         for w in result:
#             print(w[0])
#         conn.close()
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#     context = {
#         "form": form,
#         "result": result,
#     }
#     return render(request, 'index.htm', context)