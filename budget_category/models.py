from django.db import models, connection
import datetime



class BudgetManager(models.Manager):
    def get_query_set(self):
        return super(BudgetManager, self).get_query_set().filter(is_deleted=False)


class Actions(models.model) :

    creation = models.DateTimeField('Creation', default=datetime.datetime.now)
    update = models.DateTimeField('Update', default=datetime.datetime.now)
    deletion = models.BooleanField('Is deleted', default=False, db_index=True)
    #view = 

    def updateBudgetList(self, *args, **kwargs) :

      self.update = datetime.datetime.now()
      super(Actions, self).save(*args, **kwargs)
  

    def deleteCategory(self) :

      self.deletion = True
      self.updateBudgetList()

    def getBudgetCategoryByID(self, **kwargs) :

      return Actions.objects.filter(title__icontains = kwargs)

    def retrieveAllBudget(Id) :
      cursor = connection.cursor()
      cursor.execute("SET search_path TO postgres,public")
      cursor.execute(f"""SELECT * FROM BUDGET_LIST WHERE Category = "{Id}" ;""") #TODO
      list = cursor.fetchall()
      return list
      
      






class BudgetType(models.model) :

   budgetTypeName = models.CharField(max_length=18, null=True)
   budgetValueLimit = models.IntegerField(null=True)
   
   def __str__(self):
      return self.BudgetType 


class Budget(BudgetType) :

   budgetID = models.IntegerField(max_length=30, null=True)
   budgetName = models.CharField(max_length=18, null=True)
   budgetTotalValue = models.IntegerField(null=True)
   userID = models.CharField(max_length=30, null=True)
   
   def __init__(self, budgetID, budgetName, budgetTotalValue, budgetValueLimit, budgetTypeName, userID) :
      super().__init__(budgetTypeName, budgetValueLimit)
      self.budgetID = budgetID
      self.budgetName = budgetName
      self.budgetTotalValue = budgetTotalValue
      self.userID = userID

   def __str__(self):
      return self.Budget 