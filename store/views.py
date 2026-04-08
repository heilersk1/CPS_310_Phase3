from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

# -----------------------------
# Public pages
# -----------------------------
def home(request):
    return render(request, 'store/home.html')

def store_page(request):
    return render(request, 'store/store.html')

def events_page(request):
    return render(request, 'store/events.html')

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
    # TODO: Implement product creation form
    return render(request, 'store/add_product.html')

@user_passes_test(is_staff_user)
def edit_product(request, product_id):
    # TODO: Implement product edit form
    return render(request, 'store/edit_product.html', {'product_id': product_id})

@user_passes_test(is_staff_user)
def delete_product(request, product_id):
    # TODO: Implement product deletion
    return redirect('store_page')

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