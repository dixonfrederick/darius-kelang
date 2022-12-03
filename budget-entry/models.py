from django.db import models
from django.conf import settings

# class entry(models.Model):
    # int id =
    # int uid = userId
    # int budgetId =
    # int budgetTargetValue =
    # int budgetFulfilledValue =
    # date editDate =
    # final date createdDate =
    # final date fulfilledDate =

    # def __str__(self):
    #     return self


# class Transaksi(models.Model):
#     jenisTransaksi = models.CharField(max_length=30, null=True)
#     nominal = models.BigIntegerField(null=True)
#     tanggalTransaksi = models.DateField(auto_now=True)
#     users = models.ForeignKey(settings.AUTH_USER_MODEL,
#                               on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.jenisTransaksi