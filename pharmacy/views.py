from django.shortcuts import render, redirect
from .models import Medicine, Order
from .forms import MedicineForm, OrderForm

def home(request):
    return render(request, 'pharmacy/home.html')

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'pharmacy/add_medicine.html', {'form': form})

def order_medicine(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = OrderForm()
    return render(request, 'pharmacy/order_medicine.html', {'form': form})
