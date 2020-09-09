from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel,CityModel,CuisineModel
from django.contrib import messages

def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):
    sm = StateModel.objects.all()

    return render(request,"pwn/openstate.html",{'data':sm})


def openCity(request):
    sm = StateModel.objects.all()
    cm = CityModel.objects.all()
    return render(request,"pwn/opencity.html",{'state':sm,'city':cm})


def openCusine(request):
    cm = CuisineModel.objects.all()
    return render(request,"pwn/opencuisine.html",{'data':cm})


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")


def savestate(request):
    StateModel(name=request.POST.get('t1'),photo=request.FILES['t2']).save()
    messages.success(request,'state is saved')
    return openState(request)


def updatestate(request):
    sid = request.GET.get('id')
    print(sid)
    sm = StateModel.objects.get(id=sid)
    id = request.GET.get('sid')
    a = StateModel.objects.exclude(id=id)


    return render(request,'pwn/openstate.html',{'udata':sm,"remaining_data":a})


def updatestateid(request):
    #StateModel.objects.filter(id=request.GET.get('sid')).update(name=request.POST.get('t1'),photo=request.FILES.get('t2'))

    id=request.GET.get('sid')
    obj=StateModel.objects.get(id=id)

    name = request.POST.get('t1')
    photo = request.FILES.get('t2')
    obj.name=name
    obj.photo=photo
    obj.save()
    messages.success(request, 'updated success')
    #photo=request.FILES.get('t2')
    #print(photo)
    return openState(request)


def sdelete(request):
    StateModel.objects.filter(id=request.GET.get('sid')).delete()
    messages.success(request,'state deleted')
    return redirect('state')


def savecity(request):
    cid = request.POST.get('t2')
    name = request.POST.get('t1')
    photo = request.FILES.get('t3')
    print(cid,name,photo)

    print(photo)
    CityModel(name=request.POST.get('t1'),photo=request.FILES.get('t3'),city_state_id=cid).save()
    messages.success(request,'city is added')
    return redirect('city')


def updatecity(request):
    cm = CityModel.objects.filter(id=request.GET.get('cid'))
    id = request.GET.get('cid')
    a=CityModel.objects.exclude(id=id)


    return render(request,'pwn/opencity.html',{'ucity':cm,'remaining_data':a})


def updatecityid(request):
    id = request.GET.get('cid')
    name = request.POST.get('t1')
    photo = request.FILES.get('t3')
    #CityModel.objects.filter(id=request.GET.get('cid')).update(name=request.POST.get('t1'),photo =request.FILES.get('t3'))
    obj=CityModel.objects.get(id=id)
    obj.name=name
    obj.photo=photo
    obj.save()
    messages.success(request,'updated success')
    return openCity(request)


def cdelete(request):
    CityModel.objects.filter(id=request.GET.get('cid')).delete()
    messages.success(request, 'City deleted')
    return redirect('city')


def savecuisine(request):
    CuisineModel(type=request.POST.get('t1'),photo=request.FILES.get('t2')).save()
    messages.success(request,'cuisine saved')
    return openCusine(request)


def updatecuisine(request):
    cid = request.GET.get('cid')

    cm = CuisineModel.objects.filter(id=cid)
    a=CuisineModel.objects.exclude(id=cid)
    return render(request,'pwn/opencuisine.html',{'update':cm,"remaining_data":a})


def updatecuisineid(request):
    # CuisineModel.objects.filter(id=request.GET.get('cid')).update(type=request.POST.get('t1'),
    #                                                 photo=request.FILES.get('t2'))
    id = request.GET.get('cid')
    obj=CuisineModel.objects.get(id=id)
    photo = request.FILES.get('t2')
    type = request.POST.get('t1')
    obj.type=type
    obj.photo=photo
    obj.save()
    messages.success(request,'cuisine updated')
    return redirect('cuisine')


def dcuisine(request):
    CuisineModel.objects.filter(id=request.GET.get('cid')).delete()
    messages.success(request, 'cuisine deleted')
    return redirect('cuisine')