from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('home/', views.home_page, name='home_page'),
    path('login', views.log_in, name='log_in'),
    path('logout', views.logout_user, name='log_out'),
    path('about/', views.about, name='about'),

    #Candidats
    path('gestion_candidat/', views.grstion_condidat, name='gestion_condidat'),
    path('gestion_candidat/create', views.add_condidat, name="add_condidat"),
    path('gestion_candidat/create/up', views.create_condidat, name="create_condidat"),
    path('gestion_condidat/update/<int:id>', views.update_condidat, name="update_condidat"),
    path('gestion_condidat/updat/<int:id>', views.update_condida , name="update_condida"),
    path('gestion_candidat/show/<int:id>', views.show_condidat, name="show_condidat"),
    path('gestion_candidat/delete/<int:id>', views.delete_condidat, name="delete_condidat"),

    #Jurys
    path('jury/', views.jury, name="jury"),
    path('jury/create', views.add_jury, name="add_jury"),
    path('jury/creat', views.create_jury, name="create_jury"),
    path('jury/show/<int:id>', views.show_jury, name="show_jury"),
    path('jury/delete/<int:id>', views.delete_jury, name="delete_jury"),
    path('jury/update/<int:id>', views.update_jury, name="update_jury"),
    path('jury/updat/<int:id>', views.update_jur, name="update_jur"),

    #Soumissions
    path('soumission/', views.soumission, name="soumission"),
    path('soumission/create', views.add_soumission, name="add_soumission"),



]
