from django.db import models
import authuser.models


class BudgetEntry(models.Model):
    id = models.IntegerField()
    uid = models.ForeignKey(authuser.models.User, on_delete=models.CASCADE)
    # catId = models.ForeignKey(budget-category.models., on_delete=models.CASCADE)

    name = models.CharField()
    date = models.DateField()
    targetValue = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    # int budgetFulfilledValue =
    # final date fulfilledDate =

    def __str__(self):
        return self.name
