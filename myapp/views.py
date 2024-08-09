from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpFrom
from .models import Candidature, Jury, Travail

# Create your views here.

def log_in(request):
     return render(request, 'login.html', {})

def home(request):

     # check to see if loging in
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          # Authenticate
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request, user)
               messages.success(request, "You Have Been Logged In!")
               return redirect('home_page')
          else:
               messages.success(request, "There Was An Error Loggin In, Please Try Again...")
               return redirect('log_in')
     else:
          return render(request, 'login.html')


def home_page(request):
     candidates = Candidature.objects.count()
     jurys = Jury.objects.count()
     traveaux = Travail.objects.count()

     return render(request, 'home.html', {'candidates':candidates, 'jurys':jurys, 'traveaux':traveaux})

def logout_user(request):
     logout(request)
     messages.success(request, 'You Have Been Logged Out...')
     return redirect('home')


def register_user(request):
     if request.method == 'POST':
          form = SignUpFrom(request.POST)
          if form.is_valid():
               form.save()
               # Authenticate and login
               username = form.cleaned_data['username']
               password = form.cleaned_data['password1']
               user = authenticate(username=username, password=password)
               login(request, user)
               messages.success(request, " You Have Successfully Register")
               return redirect('home')
     else:
          form = SignUpFrom()
          return render(request, 'register.html', {'form': form})

     return render(request, 'register.html', {'form': form})

#def home(request):
#     return render(request, 'home.html')

def about(request):
     return render(request, 'about.html')

# Gestion des Candidatuers
def grstion_condidat(request):
     condidats = Candidature.objects.all()
     return render(request, 'condidats/index.html', {'condidats':condidats})

def add_condidat(request):
     return render(request, 'condidats/create.html')
def create_condidat(request):
     ma = request.POST['matricule']
     fn = request.POST['first_name']
     ln = request.POST['last_name']
     nc = request.POST['num_cin']
     ph = request.POST['phone']
     em = request.POST['email']
     des = request.POST['description']
     cat = request.POST['categorie']
     count_travail = Travail.objects.count()
     nu_insc = count_travail + 1
     direction = request.POST['direction']

     travail = Travail(num_inscription=nu_insc, categorie=cat, description=des)
     travail.save()

     candidat = Candidature(matricule=ma, first_name=fn, last_name=ln, num_cin=nc, phone=ph, email=em, direction=direction , travail_id=travail)
     candidat.save()


     return redirect('gestion_condidat')

def update_condidat(request, id):
     condidat = Candidature.objects.get(id=id)
     return render(request, 'condidats/update.html', {'condidat':condidat})

def update_condida(request, id):
     ma = request.POST['matricule']
     fn = request.POST['first_name']
     ln = request.POST['last_name']
     nc = request.POST['num_cin']
     ph = request.POST['phone']
     em = request.POST['email']
     condidat = Candidature.objects.get(id=id)
     condidat.matricule = ma
     condidat.first_name = fn
     condidat.last_name = ln
     condidat.num_cin = nc
     condidat.phone = ph
     condidat.email = em
     condidat.save()
     return redirect('gestion_condidat')
def show_condidat(request, id):
     condidat = Candidature.objects.get(id=id)
     travail = Travail.objects.get(id=condidat.travail_id)
     return render(request, 'condidats/show.html', {'condidat':condidat, 'travail':travail})

def delete_condidat(request, id):
     condidat = Candidature.objects.get(id=id)
     condidat.delete()
     return redirect('gestion_condidat')

def jury(request):
     jurys = Jury.objects.all()
     return render(request, 'jurys/index.html', {'jurys':jurys})

def add_jury(request):
     return render(request, 'jurys/create.html')

def create_jury(request):
     jury_count = Jury.objects.count()
     if jury_count >= 3 :
          messages.success(request, 'Vous ne puvez pas ajouter un autre jury!!!')
          return redirect('jury')
     else:
          un = request.POST['username']
          fn = request.POST['first_name']
          ln = request.POST['last_name']
          ph = request.POST['phone']
          em = request.POST['email']
          jury = Jury(username=un, first_name=fn, last_name=ln, phone=ph, email=em)
          jury.save()
          return redirect('jury')

def update_jury(request, id):
     jury = Jury.objects.get(id=id)
     return render(request, 'jurys/update.html', {'jury':jury})

def update_jur(request, id):
     un = request.POST['username']
     fn = request.POST['first_name']
     ln = request.POST['last_name']
     ph = request.POST['phone']
     em = request.POST['email']
     jury = Jury.objects.get(id=id)
     jury.username = un
     jury.first_name = fn
     jury.last_name = ln
     jury.phone = ph
     jury.email = em
     jury.save()
     return redirect('jury')
def show_jury(request, id):
     jury = Jury.objects.get(id=id)
     return render(request, 'jurys/show.html', {'jury':jury})

def delete_jury(request, id):
     jury = Jury.objects.get(id=id)
     jury.delete()
     return redirect('jury')


def soumission(request):

     traveaux = Travail.objects.all()
     return render(request, 'soumissions/index.html',{'traveaux':traveaux})

def add_soumission(request):
     candidates = Candidature.objects.all()
     return render (request, 'soumissions/create.html', {'candidates':candidates})










