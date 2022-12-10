from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

from budgetcategory.models import BudgetType
from budgetentry.forms import CreateEntryForm, EditEntryForm
from budgetentry.models import BudgetEntry


def homePageView(request):
    return render(request, "/home")


def viewDashboard(request):
    if not request.user.is_authenticated():
        return render(request, "/home")
    uid = request.user.id
    # request.session["uid"] = uid

    # cursor = connection.cursor()
    # cursor.execute("SET search_path TO postgres,public")
    # cursor.execute("SELECT * FROM BUDGET_CATEGORY WHERE UID = {};".format(uid))

    # budgetList = [1, 2]  # Budget Category IDs

    budgetList = BudgetType.objects.filter(userID=uid)

    result = {"budgetList": budgetList}

    return render(request, 'budgetentry/dashboard.html', result)


def viewEntries(request, type_ID):
    request.session['typeID'] = type_ID
    uid = request.user.id
    # uid = request.session['uid']

    # cursor = connection.cursor()
    # cursor.execute("SET search_path TO postgres,public")
    # cursor.execute("SELECT * FROM BUDGET_ENTRY WHERE UID = {} AND catID = {};".format(uid, typeID))

    # entryList = [1, 2]  # BudgetEntryData

    entryList = BudgetEntry.objects.filter(UID=uid, catID=type_ID)

    result = {"entryList": entryList, "typeID": type_ID}
    return render(request, "budgetentry/entrylist.html", result)


def viewEntryDetail(request, type_ID, entryID):
    uid = request.user.id
    # uid = request.session['uid']
    # typeID = request.session['typeID']

    data = BudgetEntry.objects.get(ID=entryID, UID=uid, catID=type_ID)
    result = {"entryID": entryID, "data": data, "type": BudgetType.objects.get(userID=uid, budgetTypeID=type_ID)}
    return render(request, "budgetentry/entrydetail.html", result)


def createEntry(request, type_ID):
    if request.method == 'POST':
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            # uid = request.session['uid']
            # catID = request.session['typeID']
            uid = request.user.id
            catID = type_ID
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


def editEntry(request, type_ID, entryID):
    uid = request.user.id
    # entryID = 1
    # uid = request.session['uid']
    # typeID = request.session['typeID']
    data = BudgetEntry.objects.get(ID=entryID, catID=type_ID)
    if data.UID != uid:
        return redirect("entries/")
    if request.method == 'POST':
        form = EditEntryForm(request.POST)
        if form.is_valid():
            Entry = BudgetEntry.objects.get(ID=entryID, UID=uid, catID=type_ID)
            Entry.targetValue = form.cleaned_data['balance']
            Entry.save()

    mode = "edit"

    target = {"mode": mode, "entryID": entryID, "data": data}
    return render(request, "budgetentry/entrycrud.html", target)


def deleteEntry(request, type_ID, entryID):  # Post
    # entryID = 1
    if request.user.is_authenticated():
        uid = request.user.id
        Entry = BudgetEntry.objects.get(ID=entryID, catID=type_ID)
        if Entry.UID == uid:
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
