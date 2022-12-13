import csv
import xlsxwriter
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.db import connection
from wallet.views import namedtuplefetchall


def export(request):
    if request.method == 'POST':
        res = request.POST
        tipe = res.get('type')
        if tipe == "csv":
            return download_csv(request)
        elif tipe == "xlsx":
            return download_xlsx(request)
        elif tipe == "json":
            return download_json(request)
        else:
            return HttpResponseBadRequest()

    return render(request, 'export/exportpage.html')


def get_user_id(username):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(f"""SELECT id FROM authuser_user WHERE username='{username}';""")
    result = namedtuplefetchall(cursor)

    return result[0].id


def download_csv(request):
    username = request.user.username
    user_id = get_user_id(username)

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="export.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['name', 'date', 'targetvalue'])
    budget = fetch_budget(user_id)
    for row in budget:
        writer.writerow(row)

    writer.writerow(['jenisTransaksi', 'nominal', 'tanggalTransaksi'])
    transaksi = fetch_transaksi(user_id)
    for row in transaksi:
        writer.writerow(row)

    writer.writerow(['name', 'balance'])
    wallet = fetch_wallet(username)
    for row in wallet:
        writer.writerow(row)

    return response


def download_xlsx(request):
    username = request.user.username
    user_id = get_user_id(username)

    response = HttpResponse(
        content_type='text/vnd.ms-excel',
        headers={'Content-Disposition': 'attachment; filename="export.xlsx"'},
    )

    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()

    counter = 0
    counter2 = 0
    for i in ['name', 'date', 'targetvalue']:
        worksheet.write(counter, counter2, i)
        counter2 += 1
    counter += 1
    counter2 = 0
    budget = fetch_budget(user_id)
    for row in budget:
        for i in row:
            if counter2 == 1:
                worksheet.write(counter, counter2, i.strftime('%d-%m-%Y'))
            else:
                worksheet.write(counter, counter2, i)
            counter2 += 1
        counter += 1
        counter2 = 0

    for i in ['jenisTransaksi', 'nominal', 'tanggalTransaksi']:
        worksheet.write(counter, counter2, i)
        counter2 += 1
    counter += 1
    counter2 = 0
    transaksi = fetch_transaksi(user_id)
    for row in transaksi:
        for i in row:
            if counter2 == 2:
                worksheet.write(counter, counter2, i.strftime('%d-%m-%Y'))
            else:
                worksheet.write(counter, counter2, i)
            counter2 += 1
        counter += 1
        counter2 = 0

    for i in ['name', 'balance']:
        worksheet.write(counter, counter2, i)
        counter2 += 1
    counter += 1
    counter2 = 0
    wallet = fetch_wallet(username)
    for row in wallet:
        for i in row:
            worksheet.write(counter, counter2, i)
            counter2 += 1
        counter += 1
        counter2 = 0

    workbook.close()

    return response


def download_json(request):
    username = request.user.username
    user_id = get_user_id(username)
    data = {}

    budget = fetch_budget(user_id)
    temp_dict = {}
    counter = 0
    for row in budget:
        temp = {"name": row[0], "date": row[1].strftime('%d-%m-%Y'), "targetvalue": row[2]}
        temp_dict[str(counter)] = temp
        counter += 1
    data["budget"] = temp_dict

    transaksi = fetch_transaksi(user_id)
    temp_dict = {}
    counter = 0
    for row in transaksi:
        temp = {"jenisTransaksi": row[0], "nominal": row[1], "tanggalTransaksi": row[2].strftime('%d-%m-%Y')}
        temp_dict[str(counter)] = temp
        counter += 1
    data["transaksi"] = temp_dict

    wallet = fetch_wallet(username)
    temp_dict = {}
    counter = 0
    for row in wallet:
        temp = {"name": row[0], "balance": row[1]}
        temp_dict[str(counter)] = temp
        counter += 1
    data["wallet"] = temp_dict

    response = HttpResponse(
        json.dumps(data),
        content_type='application/json',
        headers={'Content-Disposition': 'attachment; filename="export.json"'},
    )

    return response


def fetch_budget(user_id):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(f"""SELECT * FROM budgetentry WHERE uid={user_id};""")
    result = namedtuplefetchall(cursor)
    budget = []
    for res in result:
        budget.append([res.name, res.date, res.targetvalue])

    return budget


def fetch_transaksi(user_id):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(f"""SELECT * FROM authuser_transaksi WHERE users_id={user_id};""")
    result = namedtuplefetchall(cursor)
    transaksi = []
    for res in result:
        transaksi.append([res.jenisTransaksi, res.nominal, res.tanggalTransaksi])

    return transaksi


def fetch_wallet(username):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(f"""SELECT * FROM wallet WHERE userid='{username}';""")
    result = namedtuplefetchall(cursor)
    wallet = []
    for res in result:
        wallet.append([res.name, res.balance])

    return wallet
