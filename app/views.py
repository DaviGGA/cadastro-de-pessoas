from django.shortcuts import render, redirect
from . models import *

def index(request):
    persons = Person.objects.all()
   
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        street = request.POST['street']
        number = request.POST['number']
        cep = request.POST['cep']

        cep_nums = cep.replace("-","")

        address = Address.objects.create(street = street, house_number = number, cep = cep_nums)
        person = Person.objects.create(name = name, age = age, address = address)

        address.save()
        person.save()

        return redirect('/')

          
    return render(request, 'index.html', {'persons' : persons})


def delete(request,pk):
    if request.method == 'POST':
        person = Person.objects.filter(pk = pk).first()
        person_address = Address.objects.get(pk = person.address.pk)
        person_address.delete()

        return redirect ('/')

def edit (request,pk):
    person = Person.objects.filter(pk = pk).first()
    person_address = Address.objects.get(pk = person.address.pk)

    if request.method == 'POST':
        name = request.POST['e-name']
        age = request.POST['e-age']
        street = request.POST['e-street']
        number = request.POST['e-number']
        cep = request.POST['e-cep']

        print(person_address.street)
        print("OI")

        person.name = name
        person.age = age
        person_address.street = street
        person_address.house_number = number
        person_address.cep = cep
        
        
        person.save()
        person_address.save()

        return redirect ('/')

    return render(request, 'edit.html', {'person' : person})


def search(request):
    query = request.GET['query']
    if query:
        persons = Person.objects.filter(name__icontains = query)
    else:
        return redirect('/')

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        street = request.POST['street']
        number = request.POST['number']
        cep = request.POST['cep']

        cep_nums = cep.replace("-","")

        address = Address.objects.create(street = street, house_number = number, cep = cep_nums)
        person = Person.objects.create(name = name, age = age, address = address)

        address.save()
        person.save()

        return redirect('/')

    return render(request, 'index.html', {'persons' : persons})