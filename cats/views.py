#from django.shortcuts import render

# Create your views here.
#/home/mnmmnm/django_projects/mysite/cats/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed
from cats.forms import MakeForm
from django.forms import ModelForm
#from autos.models import Make

# Create the form class.
'''class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'
'''

# Create your views here.

class CatList(LoginRequiredMixin,View) :
    fields = '__all__'
    def get(self, request):
        mc = Breed.objects.all().count();
        al = Cat.objects.all();

        ctx = { 'breed_count': mc, 'cat_list': al };
        return render(request, 'cats/cat_list.html', ctx)

class BreedView(LoginRequiredMixin,View) :
    fields = '__all__' #added
    def get(self, request):
        ml = Breed.objects.all();
        ctx = { 'breed_list': ml };
        return render(request, 'cats/breed_list.html', ctx)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    template = 'cats/breed_form.html'
    fields = '__all__'#added
    success_url = reverse_lazy('cats:all')
    '''
    def get(self, request) :
        form = MakeForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = MakeForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        #make = form.save()
        return redirect(self.success_url)'''

# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'#added
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'
    '''
    def get(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance = make)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)'''

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'#added
    success_url = reverse_lazy('cats:all')
    #template = 'autos/make_confirm_delete.html'

'''
    def get(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        #form = MakeForm(instance=make)
        ctx = { 'make': make }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)'''

# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin,UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin,DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References