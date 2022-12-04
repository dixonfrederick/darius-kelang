from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

from budgetcategory.models import BudgetType
from budgetentry.forms import CreateEntryForm, EditEntryForm
from budgetentry.models import BudgetEntry


def homePageView(request):
    return render(request, "/home")


def viewDashboard(request):
    uid = 1

    request.session["uid"] = uid

    # cursor = connection.cursor()
    # cursor.execute("SET search_path TO postgres,public")
    # cursor.execute("SELECT * FROM BUDGET_CATEGORY WHERE UID = {};".format(uid))

    # budgetList = [1, 2]  # Budget Category IDs

    budgetList = BudgetType.objects.filter(UID=uid)

    result = {"budgetList": budgetList}

    return render(request, 'budgetentry/dashboard.html', result)


def viewEntries(request):
    typeID = 1

    request.session['typeID'] = typeID
    uid = request.session['uid']

    # cursor = connection.cursor()
    # cursor.execute("SET search_path TO postgres,public")
    # cursor.execute("SELECT * FROM BUDGET_ENTRY WHERE UID = {} AND catID = {};".format(uid, typeID))

    # entryList = [1, 2]  # BudgetEntryData

    entryList = BudgetEntry.objects.filter(UID=uid, catID=typeID)

    result = {"entryList": entryList}
    return render(request, "budgetentry/entrylist.html", result)


def viewEntryDetail(request):
    entryID = 1

    uid = request.session['uid']
    typeID = request.session['typeID']

    data = BudgetEntry.objects.get(ID=entryID, UID=uid, catID=typeID)
    result = {"entryID": entryID, "data": data}
    return render(request, "budgetentry/entrydetail.html", result)


def createEntry(request):
    if request.method == 'POST':
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            uid = request.session['uid']
            catID = request.session['typeID']
            name = form.cleaned_data['name']
            date = form.cleaned_data['setDate']
            targetValue = form.cleaned_data['balance']
            cat = BudgetType.objects.filter(UID=uid)
            newEntry = BudgetEntry(uid, catID, cat, name, date, targetValue)
            newEntry.save()
        return redirect("entries/")

    mode = "create"
    form = CreateEntryForm()
    target = {"mode": mode, "form": form}
    return render(request, "budgetentry/entrycrud.html", target)


def editEntry(request):
    entryID = 1

    uid = request.session['uid']
    typeID = request.session['typeID']

    if request.method == 'POST':
        form = EditEntryForm(request.POST)
        if form.is_valid():
            Entry = BudgetEntry.objects.get(ID=entryID, UID=uid, catID=typeID)
            Entry.targetValue = form.cleaned_data['balance']
            Entry.save()

    mode = "edit"
    data = BudgetEntry.objects.get(ID=entryID)
    target = {"mode": mode, "entryID": entryID, "data": data}
    return render(request, "budgetentry/entrycrud.html", target)


def deleteEntry(request):  # Post
    entryID = 1
    Entry = BudgetEntry.objects.get(ID=entryID)
    Entry.delete()
    return redirect("entries/")


# def getEntry(entryID):
#     # cursor = connection.cursor()
#     # cursor.execute("SET search_path TO postgres,public")
#     # cursor.execute("SELECT * FROM BUDGET_ENTRY WHERE id = {};".format(entryID))
#     # entryData = {"id": 1, "uid": 1, "typeID": 1, "name": "A", "date": "now", "targetValue": 100000,
#     #         "created": "yesterday", "edited": "earlier"}
#     entryData = BudgetEntry.objects.get(ID=entryID)
#     return entryData
