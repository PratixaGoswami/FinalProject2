from django.shortcuts import render, redirect
from django.forms import modelform_factory



def create_object(request, model, template_name, success_url):
    msg=""
    FormClass = modelform_factory(model, exclude=[])
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            msg="Data saved successfully"
            return redirect(success_url)
        else:
            print(form.errors)
            msg="Error ! something went wrong!"
    

    return render(request, template_name, {'msg':msg})



def read_objects(request, model, template_name):
    objects = model.objects.all()  
    return render(request, template_name, {'objects': objects})



def update_object(request, model, template_name, success_url, id):
    msg=""
    getid= model.objects.get(id=id) 
    FormClass = modelform_factory(model, exclude=[])
    if request.method == 'POST':
        form = FormClass(request.POST, instance=getid)
        if form.is_valid():
            form.save()
            msg="updated successfully!"
            return redirect(success_url)
        else:
            msg= " Error... Please try again."
    

    return render(request, template_name,{'msg':msg,'getid':getid})





def delete_object(request, model, success_url, id):
    
    instance =  model.objects.get (id=id)
    instance.delete()
    return redirect(success_url)
