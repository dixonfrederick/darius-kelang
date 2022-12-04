from django.db import models, connection
import datetime


class BudgetManager(models.Manager):
    def get_query_set(self):
        return super(BudgetManager, self).get_query_set().filter(is_deleted=False)


class Actions(models.Model):
    creation = models.DateTimeField('Creation', default=datetime.datetime.now)
    update = models.DateTimeField('Update', default=datetime.datetime.now)
    deletion = models.BooleanField('Is deleted', default=False, db_index=True)

    # view =

    def updateBudgetList(self, *args, **kwargs):
        self.update = datetime.datetime.now()
        super(Actions, self).save(*args, **kwargs)

    def deleteCategory(self):
        self.deletion = True
        self.updateBudgetList()

    def getBudgetCategoryByID(self, **kwargs):
        return Actions.objects.filter(title__icontains=kwargs)

    def retrieveAllBudget(Id):
        cursor = connection.cursor()
        cursor.execute("SET search_path TO postgres,public")
        cursor.execute(f"""SELECT * FROM BUDGET_LIST WHERE Category = "{Id}" ;""")  # TODO
        list = cursor.fetchall()
        return list


class BudgetType(models.Model):
    budgetTypeName = models.CharField(max_length=18, null=True)
    budgetTotalValue = models.IntegerField(null=True)
    userID = models.CharField(max_length=30, null=True)
    budgetTypeID = models.AutoField(primary_key=True)

    def __init__(self, budgetName, userID):
        self.budgetTypeName = budgetName
        self.budgetName = budgetName
        self.budgetTotalValue = 0
        self.userID = userID

    def updateValue(self, value):
        self.budgetTotalValue += value

    def __str__(self):
        return self.budgetName
