from django.shortcuts import render, redirect
from django.http import HttpResponse

def homePageView(request) :
    return render(request, "/home")

def budgetCategory_MainView(request) :
    return render(request, "BudgetCategory_MainView.HTML") 

# menampilkan halaman utama "Kelola Jenis Budget"
# menampilkan daftar semua jenis budget, ketika di dropdown suatu entry budget akan mengaktifkan method viewAllBudget()
# method budgetCategory_MainView hanya berisi respon http yang mengaktifkan file budgetCategory_MainView.HTML 

def addCategory(request) : # menambahkan suatu jenis budget (nama, sifat-sifat lainnya misalnya batasan nominal)
    return render(request, "addCategory.HTML")

def viewAllBudget(request) : # menampilkan daftar semua budget dengan tipe tertentu
    return render(request, "viewAllBudget.HTML")

def deleteCategory(request) : # menghapus sebuah atau beberapa budget beserta seluruh budget yang tipenya dihapus
    return render(request, "deleteCategory.HTML") 

def cancelOperation(request) : # membatalkan operasi method apapun, dan mengembalikannya ke halaman utama
    return redirect(request, "budget-category")

def updateBudgetList(request) : # mengubah jumlah budget dalam suatu jenis budget tertentu
    return render(request, "BudgetCategory_MainView.HTML")

def updateBudgetCategory(request) : # mengubah jumlah jenis budget
    return render(request, "updateBudgetCategory.HTML")

def successOperation(request) : # jika operasi berhasil (disetujui oleh pengguna dan sistem)
    return redirect(request, "BudgetCategory_MainView.HTML")

def back(request) : # jika pengguna menekan tombol kembali (ditampilkan di halaman budgetCategory_MainView)
    return render(request, "/home") 
    


