from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, Event
from .forms import ProductForm

# -----------------------------
# Public pages
# -----------------------------
def home(request):
    return render(request, 'store/home.html')

def store_page(request):
    products = Product.objects.all()
    return render(request, 'store/store.html', {'products': products})

def events_page(request):
    events = Event.objects.all()
    return render(request, 'store/events.html', {'events': events})

# -----------------------------
# Login / Logout
# -----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in

            # -----------------------
            # Role-based redirect
            # -----------------------
            if user.is_superuser:
                return redirect('manager_dashboard')
            elif user.is_staff:
                return redirect('employee_dashboard')
            else:
                return redirect('home')  # customer
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# -----------------------------
# Dashboards
# -----------------------------
@login_required
def manager_dashboard(request):
    if not request.user.is_superuser:  # only managers
        return redirect('home')
    return render(request, 'store/manager_dashboard.html')

@login_required
def employee_dashboard(request):
    if not request.user.is_staff or request.user.is_superuser:  # only employees
        return redirect('home')
    return render(request, 'store/employee_dashboard.html')

# -----------------------------
# Staff-only actions
# -----------------------------
def is_staff_user(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_staff_user)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store_page')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html')

@user_passes_test(is_staff_user)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('store_page')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/edit_product.html', {'product_id': product_id})

@user_passes_test(is_staff_user)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('store_page')
    return render(request, 'store/delete_product.html', {'product': product})

@user_passes_test(is_staff_user)
def add_event(request):
    # TODO: Implement event creation form
    return render(request, 'store/add_event.html')

@user_passes_test(is_staff_user)
def edit_event(request, event_id):
    # TODO: Implement event edit form
    return render(request, 'store/edit_event.html', {'event_id': event_id})

@user_passes_test(is_staff_user)
def delete_event(request, event_id):
    # TODO: Implement event deletion
    return redirect('events_page')