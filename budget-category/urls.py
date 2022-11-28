from django.urls import path

from .views import homePageView, budgetCategory_MainView

urlpatterns = [
    path("", homePageView, name="home"),
    path("budget-category", budgetCategory_MainView, name="budget-category"),
]