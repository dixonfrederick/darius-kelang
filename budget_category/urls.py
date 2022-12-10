from django.urls import path

from .views import *

urlpatterns = [
    path("home/", homePageView, name="home"),
    path("budget_category/", budgetCategory_MainView, name="budget_category"),
    path("add-category", addCategory, name="addCategory"),
    path("delete-category", deleteCategory, name="deleteCategory"),
    path("update-budget-list", updateBudgetList, name="updateBudgetList"),
    path("update-budget_category", updateBudgetCategory, name="updateBudgetCategory"),
    path("cancel/", cancelOperation, name="cancelOperation"),
    path("view-budget-entry", viewAllBudgetCategory, name="viewAllBudgetCategory"),
    path("success-operation/", successOperation, name="successOperation"),
]