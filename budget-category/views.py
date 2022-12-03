from django.core.paginator import *
from django.shortcuts import *
from django.template import *
from django.conf import *
from django.urls import *
from collections import *
from django.http import *
from django.db import *
from templates import *
from models import *
from forms import *


def homePageView(request) :
    return render(request, "/home")

def budgetCategory_MainView(request) :
    return render(request, "BudgetCategory_MainView.HTML") 

# menampilkan halaman utama "Kelola Jenis Budget"
# menampilkan daftar semua jenis budget, ketika di dropdown suatu entry budget akan mengaktifkan method viewAllBudget()
# method budgetCategory_MainView hanya berisi respon http yang mengaktifkan file budgetCategory_MainView.HTML 

def addCategory(request, form_class = BudgetCategory, template = "addCategory.HTML"  ) : # menambahkan suatu jenis budget (nama, sifat-sifat lainnya misalnya batasan nominal)

    if request.POST:
        form = form_class(request.POST)
        
        if form.is_valid():
            category = form.save()
            return HttpResponseRedirect(reverse('budget_category_list'))
    else:
        form = form_class()

    return render_to_response(template, {'form': form,}, context_instance=RequestContext(request))

    

def viewAllBudget(request, form_class = BudgetCategory, template = "viewAllBudget.HTML") : # menampilkan daftar semua budget dengan tipe tertentu

    categories_list = form_class.active.all()

    try:
        paginator = Paginator(categories_list, getattr(settings, 'Daftar Jenis Budget', 10))
        page = paginator.page(request.GET.get('Laman', 1))
        categories = page.object_list
    except InvalidPage:
        raise Http404('Sorry, invalid page requested.')

    return render_to_response(template, {
        'Kategori': categories,
        'paginator': paginator,
        'Laman': page,
    }, context_instance=RequestContext(request))



def deleteCategory(request, slug, form_class = BudgetCategory, template = "deleteCategory.HTML") : # menghapus sebuah atau beberapa budget beserta seluruh budget yang tipenya dihapus

    category = get_object_or_404(form_class.active.all(), slug=slug)
    if request.POST:
        if request.POST.get('confirmed') and request.POST['confirmed'] == 'Iya':
            category.delete()
        return HttpResponseRedirect(reverse('budget_category_list'))
    return render_to_response(template, {'category': category,}, context_instance=RequestContext(request))
    

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
    


