from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from health_hospitalizations.models import *
from health_hospitalizations.forms import *
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def mealOrders(request):
    type = "grid"
    orders = gnuhealth_inpatient_meal_order.objects.all()
    return render(request, 'health_hospitalizations/meal_orders.html'
                  , {'orders': orders
                  , 'type': type})

def addMealOrder(request):
    if request.method == "POST":
        form = mealOrderForm(request.POST)
        if form.is_valid():
            try:
                type = "grid"
                msg = "1"
                latest = gnuhealth_inpatient_meal_order.objects.latest('id')
                form.fields["id"].initial = latest.id + 1
                form.save()
                orders = gnuhealth_inpatient_meal_order.objects.all()
                messages.success(request, f'Success, Record Saved Successfully')
                return render(request, 'health_hospitalizations/patients/meal_orders.html'
                              , {'type': type, 'msg': msg, 'orders': orders})
            except:
                pass
        else:                
            messages.error(request, f'Sorry, Record Save Error')
            return HttpResponse("Invalid Form.")
    else:
        form = mealOrderForm()
        latest = gnuhealth_inpatient_meal_order.objects.latest('id')
        form.fields["id"].initial = latest.id + 1
        form.fields["create_uid"].initial = 1
        form.fields["write_uid"].initial = 1
        form.fields["create_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields["write_date"].initial = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        form.fields['id'].widget.attrs['readonly'] = True
        form.fields['create_date'].widget.attrs['readonly'] = True
        form.fields['write_date'].widget.attrs['readonly'] = True
        form.fields['create_uid'].widget.attrs['readonly'] = True
        form.fields['write_uid'].widget.attrs['readonly'] = True
        type = "add"
        return render(request, 'health_hospitalizations/meal_orders.html', {'type': type, 'form': form})


def editMealOrder(request, id):
    type = "edit"
    editForm = gnuhealth_inpatient_meal_order.objects.get(id=id)
    return render(request, 'health_hospitalizations/meal_orders.html', {'form': editForm, 'type': type})


def updateMealOrder(request, id):
    type = "grid"
    order = gnuhealth_inpatient_meal_order.objects.get(id=id)
    name = request.POST['name']
    notes = request.POST['notes']
    code = request.POST['code']
    order_id = order.id
    create_date = order.create_date
    write_date = order.write_date
    create_uid = order.create_uid
    write_uid = order.write_uid
    order = gnuhealth_inpatient_meal_order(id=order_id, create_date=create_date, write_date=write_date, create_uid=create_uid
                              , write_uid=write_uid, name=name, notes=notes, code=code)
    order.save()
    msg = "3"
    orders = gnuhealth_inpatient_meal_order.objects.all()

    if True:
        messages.success(request, f'Success, Record Updated Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Update Error')


    return render(request, 'health_hospitalizations/meal_orders.html'
                       , {'type': type, 'msg': msg, 'orders': orders})


def deleteMealOrder(request, id):
    order = gnuhealth_inpatient_meal_order.objects.get(id=id)
    ordery.delete()
    type = "grid"
    msg = "2"
    orders = gnuhealth_inpatient_meal_order.objects.all()
    if True:
        messages.success(request, f'Success, Record Deleted Successfully')
    elif False:
        messages.error(request, f'Sorry, Record Delete Error')

    return render(request, 'health_hospitalizations/meal_orders.html'
                              , {'type': type, 'msg': msg, 'orders': orders})

