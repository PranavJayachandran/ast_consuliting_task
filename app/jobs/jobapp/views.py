from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import db
from . import utils
from bson import ObjectId
from .forms import JobDataForm,SearchForm

# Create your views here.
def index(request):
    form=SearchForm(request.GET)
    if form.is_valid():
        if(form.cleaned_data['query']!=''):
            collection=db.getCollection()
            collection.create_index([("jobTitle", "text"),
                                 ("companyLocation","text")])
            collection = collection.find({"$text": {"$search": form.cleaned_data['query']}})
            result_list=[]
            for item in collection:
                item["id"] = str(item.pop("_id"))
                result_list.append(item)
            averageSalary=utils.getAverageSalary(result_list)
            return render(request,"index.html",{'data':result_list,'form':form,'averageSalary':averageSalary})
        else :
            collection=db.getCollection()
            collection=collection.find({})
            result_list=[]
            for item in collection:
                item["id"] = str(item.pop("_id"))
                result_list.append(item)
            averageSalary=utils.getAverageSalary(result_list)
            return render(request,"index.html",{'data':result_list,'form':form,'averageSalary':averageSalary})

    


def delete(request,dynamic_id):
    collection=db.getCollection()
    result = collection.delete_one({"_id": ObjectId(dynamic_id)})

# Check if the document was deleted successfully
    if result.deleted_count == 1:
        print("Document with ID {} deleted successfully.".format(dynamic_id))
    else:
        print("Document with ID {} not found.".format(dynamic_id))
    return render(request,"index.html")

def edit(request,edit_id):
    collection=db.getCollection()
    collection=collection.find({"_id": ObjectId(edit_id)})
    result_list=[]
    for item in collection:
        item["id"] = str(item.pop("_id"))
        result_list.append(item)

    form = JobDataForm(result_list[0])
    form.fields['companyLocation'].widget.attrs['size'] = 100
   
    return render(request,"edit.html",{'form':form})

def update(request):
    if request.method=="POST":
        jobTitle = request.POST.get('jobTitle', '')
        companyLocation = request.POST.get('companyLocation', '')
        salary=request.POST.get('salary','')
        id=request.POST.get('id','')
        updated_data = {
        'jobTitle': jobTitle,
        'companyLocation': companyLocation,
        'salary':salary,
        }
        collection=db.getCollection()
        collection.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
        return redirect(index)