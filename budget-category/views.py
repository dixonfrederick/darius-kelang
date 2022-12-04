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

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

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
            return HttpResponseRedirect(reverse('viewAllBudgetCategory'))
    else:
        form = form_class()

    return render_to_response(template, {'form': form,}, context_instance=RequestContext(request))

    

def budgetList(request, form_class = BudgetCategory, template = "viewAllBudget.HTML") : 

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


def viewAllBudgetCategory(request) :
    
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT * FROM BUDGET_CATEGORY_LIST;""") #TODO
    result = namedtuplefetchall(cursor)
    return render (request, 'viewAllBudgetCategory.html', {'result': result})


def getBudgetCategoryByID(request) :
      
    pointer = connection.cursor()
    pointer.execute("SET SEARCH_PATH TO POSTGRES, PUBLIC")
    pointer.execute("SELECT * FROM BUDGET_CATEGORY WHERE ID = ""; ")
    result = namedtuplefetchall(pointer)
    return render (request, 'viewAllBudgetCategory.html', {'result': result})



def viewAllSpecificBudget(request) :

    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute("""SELECT * FROM BUDGET_LIST WHERE Category = "" ;""") #TODO
    result = namedtuplefetchall(cursor)
    return render (request, 'viewAllBudgetCategory.html', {'result': result})
   





def deleteCategory(request, slug, form_class = BudgetCategory, template = "deleteCategory.HTML") : # menghapus sebuah atau beberapa budget beserta seluruh budget yang tipenya dihapus

    category = get_object_or_404(form_class.active.all(), slug=slug)
    if request.POST:
        if request.POST.get('confirmed') and request.POST['confirmed'] == 'Iya':
            category.delete()
        return HttpResponseRedirect(reverse('viewAllBudgetCategory'))
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

def retrieveAllBudget(Id) :
    cursor = connection.cursor()
    cursor.execute("SET search_path TO postgres,public")
    cursor.execute(f"""SELECT * FROM BUDGET_LIST WHERE Category = "{Id}" ;""") #TODO
    list = namedtuplefetchall(cursor)
    return list
    


