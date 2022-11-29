import csv
import xlsxwriter
import json
from django.http import HttpResponse
from authuser.models import Transaksi


def download_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])  # Dummy
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


def download_xlsx(response):
    response = HttpResponse(
        content_type='text/vnd.ms-excel',
        headers={'Content-Disposition': 'attachment; filename="somefilename.xlsx"'},
    )

    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Some Data')  # Dummy
    workbook.close()

    return response


def download_json(response):
    data = {  # Dummy
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
    }

    response = HttpResponse(
        json.dumps(data),
        content_type='application/json',
        headers={'Content-Disposition': 'attachment; filename="somefilename.json"'},
    )

    return response


def fetch_data():  # Returns all wallet, budget, and transaction in dictionary format
    return ""
