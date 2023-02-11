from django.shortcuts import render
from . models import *
from django.shortcuts import redirect

def index(request):

    persons = Person.objects.all()
   
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        street = request.POST['street']
        number = request.POST['number']
        cep = request.POST['cep']

        address = Address.objects.create(street = street, house_number = number, cep = cep)
        person = Person.objects.create(name = name, age = age, address = address)

        address.save()
        person.save()

        return redirect('/')

          
    return render(request, 'index.html', {'persons' : persons})


def delete(request,pk):
    if request.method == 'POST':
        person = Person.objects.filter(pk = pk).first()
        person.delete()

        return redirect ('/')

def edit (request,pk):
    person = Person.objects.filter(pk = pk).first()

    if request.method == 'POST':
        name = request.POST['e-name']
        age = request.POST['e-age']
        street = request.POST['e-street']
        number = request.POST['e-number']
        cep = request.POST['e-cep']

        person.name = name
        person.age = age
        person.address.street = street
        person.address.house_number = number
        person.address.cep = cep
        
        person.save()

        return redirect ('/')

    return render(request, 'edit.html', {'person' : person})