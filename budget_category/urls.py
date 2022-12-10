from django.urls import path

from budget_category.views import *

urlpatterns = [
    path("home/", homePageView, name="home"),
    path("budget_category/", budgetCategory_MainView, name="budget_category"),
    path("addCategory", addCategory, name="addCategory"),
    path("deleteCategory", deleteCategory, name="deleteCategory"),
    path("updateBudgetList", updateBudgetList, name="updateBudgetList"),
    path("updateBudgetCategory", updateBudgetCategory, name="updateBudgetCategory"),
    path("cancel", cancelOperation, name="cancelOperation"),
    path("viewAllBudgetCategory", viewAllBudgetCategory, name="viewAllBudgetCategory"),
    path("successOperation/", successOperation, name="successOperation"),
]