from django.db import models
import authuser.models as users
import budget_category.models as budget


class BudgetEntry(models.Model):
    ID = models.AutoField(primary_key=True)
    UID = models.ForeignKey(users.User, on_delete=models.CASCADE)
    catID = models.ForeignKey(budget.BudgetType, on_delete=models.CASCADE)

    name = models.CharField(max_length=60)
    date = models.DateField()
    targetValue = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    # int budgetFulfilledValue =
    # final date fulfilledDate =

    def __init__(self, UID, catID, cat, name, date, targetValue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cat.updateValue(targetValue)
        self.UID = UID
        self.catID = catID
        self.name = name
        self.date = date

    def updateTarget(self, targetValue):
        self.targetValue = targetValue

    def __str__(self):
        return self.name
