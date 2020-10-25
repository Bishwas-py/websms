from django.shortcuts import render, HttpResponse
from accounts.models import school_details 
from school.models import student_class
# Create your views here.
def profile(request):
    username= request.session['username']
    password=request.session['password']
    return render(request, "settings/profile.html", {'stc':stdClass.objects.filter(username=username, password=password), 'sdata': schoolDetails.objects.get(username=username, password=password)})


def addclass(request):
    get_class = request.POST.get('class')
    class_list = ["Grade "+ str(i) for i in range(1, 13)]+["Class "+ str(i) for i in range(1, 13)]+[str(i) for i in range(1, 13)]+['Montessori','Nursery','L.K.G','U.K.G','Kindergarten','Kinder Garten','K.G']
    if get_class in class_list:
        if not student_class.objects.filter(class_list=get_class):
            username = request.session['username']
            password = request.session['password']
            school_data = school_details.objects.get(username=username, password=password)
            class_data = student_class(connect_school=school_data, class_list=get_class)
            class_data.save()
            return HttpResponse(get_class)
        else:
            return HttpResponse(2) # 2 means already created
    else:
        return HttpResponse(0) # 0 means false i.e NONSENSE

def automatic_class(request):
    create_class = ['Nursery','L.K.G','U.K.G','Kindergarten']+["Class "+ str(i) for i in range(1, 11)]
    username = request.session['username']
    password = request.session['password']
    already_created = []
    if request.method == 'POST':
        school_data = school_details.objects.get(username=username, password=password)
        for Class in create_class:
            if not student_class.objects.filter(connect_school=school_data,class_list=Class):
                class_data = student_class(connect_school=school_data, class_list=Class)
                class_data.save()
            else:
                already_created.append(Class)
        if len(already_created) == len(create_class):
            return HttpResponse(0)
        else:
            return HttpResponse(1)
    else:
        return HttpResponse(0)
        