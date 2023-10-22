from django.shortcuts import render
from django.http import HttpResponse
from . import db
from bson import ObjectId
from .forms import JobDataForm

# Create your views here.
def index(request):
    collection=db.getCollection()
    collection=collection.find({})
    result_list=[]
    for item in collection:
        item["id"] = str(item.pop("_id"))
        result_list.append(item)
    # result_list=[
    #     {
    #         'id':1,
    #         'jobTitle':'Title',
    #         'companyLocation':'This is loc',
    #         'jobRequirement':[
    #             'this is a text',
    #             'this is next text'
    #         ],
    #         'metadata':[
    #             'sal',
    #             'tol'
    #         ]
    #     },
    #     {
    #         'id':2,
    #         'jobTitle':'Title',
    #         'companyLocation':'This is loc',
    #         'jobRequirement':[
    #             'this is a text',
    #             'this is next text'
    #         ],
    #         'metadata':[
    #             'sal',
    #             'tol'
    #         ]
    #     },
    #     {
    #         'id':3,
    #         'jobTitle':'Title',
    #         'companyLocation':'This is loc',
    #         'jobRequirement':[
    #             'this is a text',
    #             'this is next text'
    #         ],
    #         'metadata':[
    #             'sal',
    #             'tol'
    #         ]
    #     },
        # {
        #     'id':4,
        #     'jobTitle':'Title',
        #     'companyLocation':'This is loc',
        #     'jobRequirement':[
        #         'this is a text',
        #         'this is next text'
        #     ],
        #     'metadata':[
        #         'sal',
        #         'tol'
        #     ]
        # },
    # ]
    print(result_list)
    return render(request,"index.html",{'data':result_list})


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
   
    return render(request,"edit.html",{'form':form})

def update(request):
    if request.method=="POST":
        jobTitle = request.POST.get('jobTitle', '')
        companyLocation = request.POST.get('companyLocation', '')
        jobRequirement = request.POST.get('jobRequirement', '')
        metadata = request.POST.get('metadata', '')
        id=request.POST.get('id','')
        jR = jobRequirement[1:len(jobRequirement)-2].split(',')
        jR = [item.strip("'").strip() for item in jR if item.strip()]        
        
        mR = metadata[1:len(metadata)-2].split(',')
        mR = [item.strip("'").strip() for item in mR if item.strip()]
        updated_data = {
        'jobTitle': jobTitle,
        'companyLocation': companyLocation,
        'jobRequirement': jR,
        'metadata': mR,
        }

        collection=db.getCollection()
        # Update the document based on a unique identifier (e.g., "_id")
        collection.update_one({'_id': ObjectId(id)}, {'$set': updated_data})
        return HttpResponse("updated")