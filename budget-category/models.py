from django.db import models

#class addCategory(models.model) :


# class deleteCategory(models.model) :


class BudgetType(models.model) :

   budgetTypeName = models.CharField(max_length=18, null=False)
   budgetValueLimit = models.IntegerField(null=False)
   
   def __str__(self):
      return self.BudgetType 


class Budget(models.model) :

   budgetID = models.IntegerField(max_length=30, null=False)
   budgetName = models.CharField(max_length=18, null=False)
   budgetTotalValue = models.IntegerField(null=False)
   userID = models.CharField(max_length=30, null=False)
   
   def __str__(self):
      return self.Budget 
