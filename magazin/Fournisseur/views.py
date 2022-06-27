from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Fourn
from .forms import FournForm
# Create your views here.


def all_fourn(request):
      fourn_data=Fourn.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  fourn_data
            else:
                  fourn_data=Fourn.objects.filter(Nom =Search)

<<<<<<< HEAD
      countdt = Fourn.objects.count()
      return render(request,"Fournisseur/fournisseurs.html",{'fourn_data':fourn_data,'countdt': countdt})
=======
<<<<<<< HEAD
      countfr = Fourn.objects.count()
      return render(request,"Fournisseur/fournisseurs.html",{'fourn_data':fourn_data,'countfr': countfr})
=======
      countdt = Fourn.objects.count()
      return render(request,"Fournisseur/fournisseurs.html",{'fourn_data':fourn_data,'countdt': countdt})
>>>>>>> 8be79b34c5469a9341f0101d2a141bbadde9eb1b
>>>>>>> tempbranch

def add_fourn(request):
      form=FournForm
      if request.method == 'POST':
            form=FournForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/fourns')  # 4
      else:
       return render(request,"Fournisseur/add_fourn.html",{'form':form})

def update_fourn(request,Id):
      fourn_data=Fourn.objects.get(Id=Id)
<<<<<<< HEAD
      form=FournForm(instance=Fourn_data)
=======
<<<<<<< HEAD
      form=FournForm(instance=fourn_data)
=======
      form=FournForm(instance=Fourn_data)
>>>>>>> 8be79b34c5469a9341f0101d2a141bbadde9eb1b
>>>>>>> tempbranch
      if request.method == 'POST':
            form=FournForm(request.POST,instance=fourn_data)
            if form.is_valid():
                  form.save()
            return redirect('/fourns')  # 4
      else:
       return render(request,"Fournisseur/update_fourn.html",{'form':form})

def delete_fourn(request,Id):
      fourn_data=Fourn.objects.get(Id=Id)
      fourn_data.delete()
      return redirect('/fourns')