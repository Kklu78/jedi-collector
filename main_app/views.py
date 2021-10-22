from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
from .forms import TrainingForm


# Create your views here.
def home(request):
  return redirect('index')

def about(request):
    return render(request, 'about.html')

def jedis_index(request):
    jedis = Jedi.objects.all()
    return render(request, 'jedis/index.html', { 'jedis': jedis })

def jedis_detail(request, jedi_id):
    jedi = Jedi.objects.get(id=jedi_id)
    m_weapons = Weapon.objects.exclude(id__in = jedi.weapons.all().values_list('id'))
    training_form = TrainingForm()
    return render(request, 'jedis/detail.html', { 'jedi': jedi,
    'training_form': training_form,
    'weapons': m_weapons })

def add_training(request, jedi_id):
    form = TrainingForm(request.POST)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.jedi_id = jedi_id
        new_training.save()
    return redirect('detail', jedi_id = jedi_id)

def assoc_weapon(request, jedi_id, weapon_id):
    Jedi.objects.get(id=jedi_id).weapons.add(weapon_id)
    return redirect('detail', jedi_id=jedi_id)


class jediCreate(CreateView):
    model = Jedi
    fields = ['name', 'rank', 'age']
    success_url = '/jedis/'

class jediUpdate(UpdateView):
    model = Jedi
    fields = ['name', 'rank', 'age']

class jediDelete(DeleteView):
    model = Jedi
    success_url = '/jedis/'