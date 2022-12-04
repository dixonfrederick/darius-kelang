from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection


def homePageView(request):
    return render(request, "/home")


def viewDashboard(request):
    uid = 1
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT * FROM BUDGETCATEGORY;""")  # TODO: select only where uid
    budgetList = [1, 2]  # Budget Category IDs
    result = {"uid": uid, "budgetList": budgetList}

    return render(request, 'budgetentry/dashboard.html', result)


def viewEntries(request):
    uid = 1
    typeID = 1
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT * FROM BUDGETENTRY;""")  # TODO: select only where uid, typeID
    entryList = [1, 2]  # BudgetEntryData
    result = {"uid": uid, "typeID": typeID, "entryList": entryList}
    return render(request, "budgetentry/entrylist.html", result)


def viewEntryDetail(request):
    uid = 1
    typeID = 1
    entryID = 1
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT * FROM BUDGETENTRY;""")  # TODO: Get details
    entryDetail = {"id": 1, "uid": 1, "typeID": 1, "name": "A", "date": "now", "targetValue": 100000,
                   "created": "yesterday", "edited": "earlier"}
    return render(request, "budgetentry/entrydetail.html", entryDetail)


def createEntry(request):
    uid = 1
    typeID = 1
    mode = "create"
    target = {"uid": uid, "typeID": typeID, "mode": mode}
    return render(request, "budgetentry/entrycrud.html", target)


def editEntry(request):
    uid = 1
    typeID = 1
    entryID = 1
    mode = "edit"
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT * FROM BUDGETENTRY;""")  # TODO: Get details
    entryDetail = {"id": 1, "uid": 1, "typeID": 1, "name": "A", "date": "now", "targetValue": 100000,
                   "created": "yesterday", "edited": "earlier"}
    target = {"uid": uid, "typeID": typeID, "mode": mode, "data": entryDetail}
    return render(request, "budgetentry/entrycrud.html", target)


# def editEntry(request): # Post
#     return render(request, "")


# def deleteEntry(request): # Post
#     return render(request, "")