# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.utils.encoding import python_2_unicode_compatible
import os
from .forms import VerseForm
import sqlite3
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    poet = combo_fil('Search_poet')
    mydate = combo_fil('Search_mydate')
    purpose = combo_fil('Search_purpose')
    publisher = combo_fil('Search_publisher')
    sea = combo_fil('Search_sea')
    poem = combo_fil('Search_poem')
    test = 'opps'
    context = {
        "form": form, 'poet': poet, 'mydate': mydate, 'poem': poem, 'purpose': purpose, 'sea': sea, 'publisher': publisher ,
    }
    return render(request, 'index.htm', context)


def combo_fil(table):
    try:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
        c = conn.cursor()
        c.execute("SELECT * FROM "+table,)
        result = list(c)
        #poet.execute("SELECT * FROM Search_mydate ",)
        #result = list(poet)
        conn.commit()
        conn.close()
        return result
    except ValueError:
        print("Oops!  That was no valid Data.  Try again...")

result = [1]

def tosearchpage(request):
    global result
    form = VerseForm(request.POST or None)
    if form.is_valid():
        searchWord = request.POST.get('text', '').replace("'", '')
        request.session['Sword'] = searchWord
    searchWord1 = request.session.get('Sword')
    try:
        if request.POST.get('search_method', '') != 'advanced':
            conn = sqlite3.connect(
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
            c = conn.cursor()
            c.execute(
                "SELECT * FROM Search_poem "
                "LEFT OUTER JOIN Search_verse ON (Search_poem.id = Search_verse.poem_id) "
                "LEFT OUTER JOIN Search_poet ON (Search_poem.poet_id = Search_poet.id) "
                "WHERE (Search_verse.text like '%" + searchWord1 + "%') ", )
            result_list = list(c)
            conn.commit()
            conn.close()

            page = request.GET.get('page', 1)

            paginator = Paginator(result_list, 5)
            result = paginator.page(page)
        else:
            result = tosearch_advance(request, searchWord1)
    except ValueError:
        print("Oops!  That was no valid Data.  Try again...")
    context = {
        'searchWord': searchWord1,
        'result': result,
        'form': form,
    }
    return render(request, 'Search.htm', context)



def tosearch_advance(request, Searchword):
    global result
    if request.method == "POST":
        myDate_id = request.POST.get('xmydate', '')
        poet_id = request.POST.get('xpoet', '')
        poem_id = request.POST.get('xpoem','')
        purpose_id = request.POST.get('xpurpose', '')
        sea_id = request.POST.get('xsea', '')
        publisher_id = request.POST.get('xpublisher', '')
        try:
            conn = sqlite3.connect(
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
            c = conn.cursor()
            c.execute(
                "SELECT * FROM Search_poem " \
                "LEFT OUTER JOIN Search_verse ON (Search_poem.id = Search_verse.poem_id) " \
                "LEFT OUTER JOIN Search_poet ON (Search_poem.poet_id = Search_poet.id) " \
                "WHERE " \
                "(Search_poem.publisher_id = '" + publisher_id + "') AND " \
                "(Search_poem.sea_id = '" + sea_id + "') AND " \
                "(Search_poem.purpose_id = '" + purpose_id + "') AND " \
                "(Search_poem.id = '" + poem_id + "') AND " \
                "(Search_poem.poet_id = '" + poet_id + "') AND " \
                "(Search_poem.myDate_id = '" + myDate_id + "') AND    " \
                "(Search_verse.text like '%" + Searchword + "%')", )
            result = list(c)
            conn.commit()
            conn.close()

        except ValueError:
            print("Oops!  That was no valid Data.  Try again...")
    return result


def poetryshow(request, poet_id):
    searchWord = request.session.get('Sword')
    try:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
        c = conn.cursor()
        c.execute(
            "select text from Search_verse where poem_id =" + poet_id + ";", )
        result = list(c)
        conn.commit()
        # for w in result:
        #     print(w[0])
        conn.close()
        fresult = getalldata(poet_id)
    except ValueError:
        print("Oops!  That was no valid Data.  Try again...")
    context = {
        'result': result,
        'fresult': fresult,
        'searchWord': searchWord,
    }
    return render(request, 'poetry.htm', context)


def getalldata(p_id='1'):
    try:
        conn = sqlite3.connect(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/" + "db.sqlite3"))
        c = conn.cursor()
        c.execute(
            "SELECT Search_poem.id, Search_poem.title, Search_poet.name, Search_poet.picture ,Search_purpose.purpose, Search_sea.sea , Search_mydate.myDate, Search_publisher.name FROM Search_poem LEFT OUTER JOIN Search_poet ON (Search_poet.id = Search_poem.poet_id) LEFT OUTER JOIN Search_purpose ON (Search_purpose.id = Search_poem.purpose_id) LEFT OUTER JOIN Search_sea ON (Search_sea.id = Search_poem.sea_id) LEFT OUTER JOIN Search_mydate ON (Search_mydate.id = Search_poem.myDate_id) LEFT OUTER JOIN Search_publisher ON (Search_publisher.id = Search_poem.publisher_id) WHERE (Search_poem.id = " + p_id + ")", )
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


# var = "SELECT * FROM Search_poem " \
#       "LEFT OUTER JOIN Search_verse ON (Search_poem.id = Search_verse.poem_id) " \
#       "LEFT OUTER JOIN Search_poet ON (Search_poem.poet_id = Search_poet.id) " \
#       "WHERE " \
#       "(Search_poem.publisher_id = '"+ publisher_id +"') AND " \
#       "(Search_poem.sea_id = '"+ sea_id +"') AND " \
#       "(Search_poem.purpose_id = '"+ purpose_id +"') AND " \
#       "(Search_poem.id = '"+ id +"') AND " \
#       "(Search_poem.poet_id = '"+ poet_id +"') AND " \
#       "(Search_poem.myDate_id = '"+ myDate_id +"') AND    " \
#       "(Search_verse.text like '%"+ Searchword +"%')"
