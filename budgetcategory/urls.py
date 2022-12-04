from django.urls import path

from .views import *

urlpatterns = [
    path("home/", homePageView, name="home"),
    path("budgetcategory/", budgetCategory_MainView, name="budgetcategory"),
    path("add-category", addCategory, name="addCategory"),
    path("delete-category", deleteCategory, name="deleteCategory"),
    path("update-budget-list", updateBudgetList, name="updateBudgetList"),
    path("update-budgetcategory", updateBudgetCategory, name="updateBudgetCategory"),
    path("cancel/", cancelOperation, name="cancelOperation"),
    path("view-budget-entry", viewAllBudgetCategory, name="viewAllBudgetCategory"),
    path("success-operation/", successOperation, name="successOperation"),
]
