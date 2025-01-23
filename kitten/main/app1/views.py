from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect
from.models import user_registration
from.models import camera_registration
from django.contrib import messages
from django.http import JsonResponse
from django.views import View


# Create your views here.

def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'services.html')

def service1(request):
    return render(request,'services1.html')

def contact(request):
    return render(request,'contact.html')

def product(request):
    if request.method=='POST':
        a=request.POST['productName']
        b=request.POST['productPrice']
        c=request.POST['quantity']
        d=request.FILES['images']
        e=request.POST['description']
        data=add_product.objects.create(productname=a,productprice=b,quantity=c,image=d,description=e)
        data.save()
        return render(request,'addproduct.html')
    return render(request, 'addproduct.html')


def user_dashboard(request):
    # Check if the user is logged in
    if 'username' not in request.session:
        return redirect('login_view')  # Redirect to login if no session

    # Get the user data from the session
    username = request.session['username']
    user = user_registration.objects.filter(username=username).first()

    # If no user is found (shouldn't happen with proper session), redirect to login
    if not user:
        return redirect('login_view')

    # Pass the user data to the template
    return render(request, 'user_dashboard.html', {'user': user})

def photographer_dashboard(request):
    return render(request,'photographer_dashboard.html')
def success_page(request):
    return render(request,'rs.html')


def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')

def about1(request):
    return render(request,'about1.html')

def portfolio(request):
    return render(request,'portfolio.html')


# def reg(request):
#     if request.method == "POST":
#         user_type = request.POST.get("type")  # Check the user type from the hidden input
#         if user_type == "user":
#             # Process user registration
#             password = request.POST.get("password")
#             confirm_password = request.POST.get("confirm_password")
#             if password != confirm_password:
#                 return render(request, "rr.html", {"error": "Passwords do not match!"})
#
#             # Save User model
#             user = user_registration(
#                 fullname=request.POST.get("fullname"),
#                 email=request.POST.get("email"),
#                 phonenumber=request.POST.get("phonenumber"),
#                 username=request.POST.get("username"),
#                 password=request.POST.get("password")  # Hash password
#             )
#             user.save()
#             return redirect(login_view)
#                 # Hash password
#
#
#         elif user_type == "photographer":
#             # Process caregiver registration
#             password = request.POST.get("password")
#             confirm_password = request.POST.get("confirm_password")
#             if password != confirm_password:
#                 return render(request, "rr.html", {"error": "Passwords do not match!"})
#
#             # Save Caregiver model
#             photographer = camera_registration(
#                     fullname=request.POST.get("cg_fullname"),
#                     email=request.POST.get("cg_email"),
#                     phone_number=request.POST.get("cg_phonenumber"),
#                     username=request.POST.get("cg_username"),
#                     qualifications=request.POST.get("cg_qualifications"),
#                     experience=request.POST.get("cg_experience"),
#                     password=request.POST.get("cg_password"), # Hash password
#                     profile_picture=request.FILES.get("profile_picture")
#             )
#             photographer.save()
#             return redirect(login_view)
#
#     return render(request, "rr.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import user_registration, camera_registration


def reg(request):
    if request.method == "POST":
        user_type = request.POST.get("type")  # Check the user type from the hidden input

        if user_type == "user":
            # Check for duplicate email or username
            email = request.POST.get("email")
            username = request.POST.get("username")
            if user_registration.objects.filter(email=email).exists():
                return render(request, "rr.html", {"error": "Email is already registered!"})
            if user_registration.objects.filter(username=username).exists():
                return render(request, "rr.html", {"error": "Username is already taken!"})

            # Process user registration
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            if password != confirm_password:
                return render(request, "rr.html", {"error": "Passwords do not match!"})

            # Save User model
            user = user_registration(
                fullname=request.POST.get("fullname"),
                email=email,
                phonenumber=request.POST.get("phonenumber"),
                username=username,
                password=request.POST.get("password")  # You should hash the password
            )
            user.save()
            return redirect(login_view)  # Adjust to your actual login URL

        elif user_type == "photographer":
            # Check for duplicate email or username for photographer
            email = request.POST.get("cg_email")
            username = request.POST.get("cg_username")
            if camera_registration.objects.filter(email=email).exists():
                return render(request, "rr.html", {"error": "Email is already registered as a photographer!"})
            if camera_registration.objects.filter(username=username).exists():
                return render(request, "rr.html", {"error": "Username is already taken for photographer!"})

            # Process photographer registration
            password = request.POST.get("cg_password")
            confirm_password = request.POST.get("cg_confirm_password")
            if password != confirm_password:
                return render(request, "rr.html", {"error": "Passwords do not match!"})

            # Save Photographer model
            photographer = camera_registration(
                fullname=request.POST.get("cg_fullname"),
                email=email,
                phone_number=request.POST.get("cg_phonenumber"),
                username=username,
                qualifications=request.POST.get("cg_qualifications"),
                experience=request.POST.get("cg_experience"),
                password=request.POST.get("cg_password"),  # Hash the password
                profile_picture=request.FILES.get("profile_picture")
            )
            photographer.save()
            return redirect(login_view)  # Adjust to your actual login URL

    return render(request, "rr.html")


from django.shortcuts import redirect, render
from django.contrib import messages
from .models import user_registration, camera_registration

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # User login
        user = user_registration.objects.filter(username=username, password=password).first()
        if user:
            request.session['username'] = username
            request.session['user_type'] = 'user'
            messages.success(request, f'Welcome, {user.fullname} You are logined.')
            return redirect(user_dashboard)  # Replace with your user dashboard URL name

        # Photographer login
        photographer = camera_registration.objects.filter(username=username, password=password,is_accepted='accepted').first()
        print(photographer)
        if photographer:
            request.session['username'] = username
            request.session['user_type'] = 'photographer'
            messages.success(request, f'Welcome, {photographer.fullname} You are logined.')
            return redirect(photographer_dashboard)  # Replace with your photographer dashboard URL name

        # Admin login
        if username == 'admin' and password == '123': # Use this for basic admin login
            request.session['user_type'] = 'admin'
            messages.success(request, 'Welcome Admin! You are logged in.')
            return redirect(admin_dashboard)  # Replace with your admin dashboard URL name

        # Invalid credentials
        messages.error(request, 'Invalid username or password.')
        return redirect(login_view)

    return render(request, 'login.html')



def admin_view_photographer(request):
    unread_count = Notification.objects.filter(is_read=False).count()
    # Get all feedbacks or filter as needed
    photographers = camera_registration.objects.all()  # Get all teachers
    return render(request, 'admin_view_photographer.html', {'photographers': photographers,'unread_count': unread_count})




def cameraman_update_profile(request):
    # Assuming the logged-in owner's username is stored in the session
    username = request.session.get('username')

    # Ensure the user is authenticated
    if not username:
        messages.error(request, "You must be logged in to update your profile.")
        return redirect('login_view')  # Redirect to the login page

    # Retrieve the owner object
    photographer = camera_registration.objects.get(username=username)

    if request.method == 'POST':
        # Update owner details from the form data
        photographer.fullname = request.POST.get('fullname')
        photographer.username = request.POST.get('username')
        photographer.email = request.POST.get('email')
        photographer.phone_no = request.POST.get('phn')
        # Update the document field only if a new file is uploaded

        photographer.save()  # Save the updated owner object
        messages.success(request, "Profile updated successfully!")
        # return redirect('user_profile')  # Redirect to the owner profile page

        # For GET requests, render the update form with existing data
    return render(request, 'cameraman_update_profile.html', {'photographer': photographer})

def view_user(request):
    unread_count = Notification.objects.filter(is_read=False).count()
    user = user_registration.objects.all()
    return render(request,'admin_view_user.html',{'users':user,'unread_count': unread_count})

def reject_photographer(request, photographer_id):
    photographer = camera_registration.objects.get(pk=photographer_id)
    photographer.is_accepted = 'rejected'
    photographer.save()
    return redirect(admin_view_photographer)

def accept_photographer(request, photographer_id):
    photographer = camera_registration.objects.get(pk=photographer_id)
    photographer.is_accepted = 'accepted'
    print("is_accepted",photographer.is_accepted)
    photographer.save()
    return redirect(admin_view_photographer)

def user_profile(request):
    # Fetch the logged-in user's username from the session
    username = request.session.get('username')  # Ensure 'username' is set during login

    # Check if the user exists
    try:
        user =user_registration.objects.get(username=username)
    except user_registration.DoesNotExist:
        messages.error(request, 'User not found. Please log in again.')
        return redirect(login_view)  # Redirect to the login page if user not found

    # Render the profile template with the user details
    return render(request, 'user_profile.html', {'user': user})

def update_userprofile(request):
    # Assuming the logged-in owner's username is stored in the session
    username = request.session.get('username')

    # Ensure the user is authenticated
    if not username:
        messages.error(request, "You must be logged in to update your profile.")
        return redirect('login_view')  # Redirect to the login page

    # Retrieve the owner object
    user = user_registration.objects.get(username=username)

    if request.method == 'POST':
        # Update owner details from the form data
        user.fullname = request.POST.get('fullname')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.phone_no = request.POST.get('phn')
        # Update the document field only if a new file is uploaded

        user.save()  # Save the updated owner object
        messages.success(request, "Profile updated successfully!")
        # return redirect('user_profile')  # Redirect to the owner profile page

        # For GET requests, render the update form with existing data
    return render(request, 'update_userprofile.html', {'user': user})

def cameraman_profile(request):
    # Fetch the logged-in user's username from the session
    username = request.session.get('username')  # Ensure 'username' is set during login

    # Check if the user exists
    try:
        photographer =camera_registration.objects.get(username=username)
    except camera_registration.DoesNotExist:
        messages.error(request, 'User not found. Please log in again.')
        return redirect(login_view)  # Redirect to the login page if user not found

    # Render the profile template with the user details
    return render(request, 'cameraman_profile.html', {'photographer': photographer})





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PhotographerImage
from django.contrib import messages


def upload_image(request):
    if request.method == 'POST':
        category = request.POST.get('category')  # Retrieve selected category
        files = request.FILES.getlist('images')  # Retrieve the list of uploaded files

        # Get the photographer from the session
        photographer = camera_registration.objects.filter(username=request.session.get('username')).first()

        if photographer:
            # Save each image with the category and associate it with the photographer
            for file in files:
                PhotographerImage.objects.create(
                    photographer=photographer,  # Correct way to access the photographer object
                    image=file,
                    category=category
                )
            messages.success(request, "Images uploaded successfully!")
            # return redirect('photographer_dashboard')  # Redirect to the dashboard after upload
        else:
            messages.error(request, "Photographer not found or session expired.")
            return redirect('login')  # Redirect to login or error page if photographer is not found

    return render(request, 'upload_image.html')






def show_images(request):
    # Get the photographer's username from the session
    photographer_username = request.session.get('username')

    # Get the photographer object using the username from the session
    photographer = camera_registration.objects.filter(username=photographer_username).first()

    if photographer:
        # Get all images for the logged-in photographer
        photographer_images = PhotographerImage.objects.filter(photographer=photographer)

        # Filter images by category
        wedding_images = photographer_images.filter(category="Wedding")
        natural_images = photographer_images.filter(category="Natural")
        fashion_images = photographer_images.filter(category="Fashion")

        # Pass images to the context for the template
        context = {
            'wedding_images': wedding_images,
            'natural_images': natural_images,
            'fashion_images': fashion_images,
        }

        return render(request, 'show_images.html', context)
    else:
        # If photographer is not found or session is expired
        messages.error(request, "Photographer not found or session expired.")
        return redirect('login')  # Redirect to login or error page if photographer is not found

def show_imagess(request):
    # Get the photographer's username from the session
    photographer_username = request.session.get('username')

    # Get the photographer object using the username from the session
    photographer = camera_registration.objects.filter(username=photographer_username).first()

    if photographer:
        # Get all images for the logged-in photographer
        photographer_images = PhotographerImage.objects.filter(photographer=photographer)

        # Filter images by category
        wedding_images = photographer_images.filter(category="Wedding")
        natural_images = photographer_images.filter(category="Natural")
        fashion_images = photographer_images.filter(category="Fashion")

        # Pass images to the context for the template
        context = {
            'wedding_images': wedding_images,
            'natural_images': natural_images,
            'fashion_images': fashion_images,
        }

        return render(request, 'show_imagess.html', context)
    else:
        # If photographer is not found or session is expired
        messages.error(request, "Photographer not found or session expired.")
        return redirect('login')  # Redirect to login or error page if photographer is not found

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, get_object_or_404, redirect
from .models import add_product


def update(request, d):
    # Fetch the product to update
    data = get_object_or_404(add_product, pk=d)

    if request.method == 'POST':
        # Collect the updated data from the form
        a = request.POST['productname']
        b = request.POST['productprice']
        c = request.POST['quantity']
        e = request.POST['description']

        # Check if a new image was uploaded
        if 'images' in request.FILES:
            image = request.FILES['images']
            # Update the product with a new image
            data.image = image

        # Update other fields
        data.productname = a
        data.productprice = b
        data.quantity = c
        data.description = e

        # Save the updated product
        data.save()

        # Redirect to the product display page after update
        return redirect('product_display')  # Redirect to the display page

    return render(request, 'update_product.html', {'data': data})

def delete_product(request,d):
    data=add_product.objects.get(pk=d)
    data.delete()
    return render(request,'product_display.html')

def viewproduct(request):
    data = add_product.objects.all()
    return render(request, 'viewproduct.html', {'data': data})


def add_to_cart(request,d):
    data= add_product.objects.get(pk=d)
    user=user_registration.objects.get(username=request.session['user'])
    try:
        b=cart.objects.get(user_details=user,product_id=data)
        b.quantity+=1
        b.save()
    except cart.DoesNotExist:
        cart.objects.create(user_details=user,product_id=data)
        return redirect(carts)
    return redirect(carts)


def carts(request):
    user = user_registration.objects.get(username=request.session['user'])
    data=cart.objects.filter(user_details=user)
    l = []
    for i in data:
        total_price = int(i.product_id.productprice) * int(i.quantity)
        d = {'product': i.product_id, 'total_price': total_price}
        l.append(d)
    print("--------------")
    print(l)
    total_sum = sum(item['total_price'] for item in l)
# c=len(l)
    c = cart.objects.filter(user_details=user).count()
    print(total_sum)
    if not l:
        messages.success(request, 'cart is empty')
    return render(request, 'carts.html', {'data': data, 'price': l, 'total_price': total_sum, 'count': c})

def product_display(request):
    data=add_product.objects.all()
    return render(request, 'product_display.html',{'data':data})



from .models import available_Photographer








from .models import available_Photographer


def add_photographer(request):
    user_details = camera_registration.objects.get(username=request.session['username'])
    if request.method == 'POST':
        # Get data from the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        specialization = request.POST.get('specialization')
        location = request.POST['location']
        hourly_rate = request.POST.get('hourly_rate')



        try:
            print('---------------------------------------------')
            print('ok')
            print(specialization)
            print(hourly_rate)
            print(location)
            print(user_details.username)
            # Create and save the photographer to the database


            photographer=available_Photographer.objects.create(
                user=user_details,
                hourly_rate=hourly_rate,
                specialization=specialization,
                location=location,

            )
            photographer.save()

            print('---------------------------------------------')
            print('ok')
            messages.success(request, 'photographer added successfully!')
            return redirect(photographer_dashboard)
        except Exception as e:
            print(e)
            messages.error(request, f'Error adding photographer: {e}')
            return render(request, 'photographer_add_details.html')

    # If the method is not POST, render the form page
    return render(request, 'photographer_add_details.html',{'user':user_details})

from django.shortcuts import render
from .models import available_Photographer

def show_photographer(request):
    # Fetch photographers approved by the admin
    photographers = available_Photographer.objects.filter(is_accepted='PENDING').select_related('user')

    # Debug print for verification
    for photographer in photographers:
        print(photographer.user.fullname)  # Access camera_registration fields
        print(photographer.specialization)  # Access available_Photographer fields

    return render(request, 'available_photographer.html', {'photographers': photographers})






def logout(request):
    if 'user' in request.session:
        request.session.flush()
        return redirect(index)
    return redirect(index)

import razorpay
from django.http import JsonResponse




def sg(request):
    return render(request,'sg.html')



def view_portfolio(request,i):
    photographer=available_Photographer.objects.get(pk=i)
    images=PhotographerImage.objects.filter(photographer=photographer.user)
    if photographer:
        # Get all images for the logged-in photographer
        photographer_images = PhotographerImage.objects.filter(photographer=photographer.user)

        # Filter images by category
        wedding_images = photographer_images.filter(category="Wedding",photographer=photographer.user)
        natural_images = photographer_images.filter(category="Natural",photographer=photographer.user)
        fashion_images = photographer_images.filter(category="Fashion",photographer=photographer.user)

        # Pass images to the context for the template
        context = {
            'wedding_images': wedding_images,
            'natural_images': natural_images,
            'fashion_images': fashion_images,
        }

        return render(request, 'show_imagess.html', context)
    else:
        # If photographer is not found or session is expired
        messages.error(request, "Photographer not found or session expired.")
        return redirect('login')  # Redirect to login or error page if photographer is not found

# def view_portfolio2(request,i):
#     photographer=available_Photographer.objects.get(pk=i)
#     images=PhotographerImage.objects.filter(photographer=photographer.user)
#     if photographer:
#         # Get all images for the logged-in photographer
#         photographer_images = PhotographerImage.objects.filter(photographer=photographer.user)
#
#         # Filter images by category
#         wedding_images = photographer_images.filter(category="Wedding",photographer=photographer.user)
#         natural_images = photographer_images.filter(category="Natural",photographer=photographer.user)
#         fashion_images = photographer_images.filter(category="Fashion",photographer=photographer.user)
#
#         # Pass images to the context for the template
#         context = {
#             'wedding_images': wedding_images,
#             'natural_images': natural_images,
#             'fashion_images': fashion_images,
#         }
#
#         return render(request, 'show_images.html', context)
#     else:
#         # If photographer is not found or session is expired
#         messages.error(request, "Photographer not found or session expired.")
#         return redirect('login')  # Redirect to login or error page if photographer is not found



from django.shortcuts import render, redirect
from django.contrib import messages



from .models import Booking,user_registration, available_Photographer

def uregister(request, i, Photographer_id):
    user = user_registration.objects.get(username=request.session['username'])
    user_details = user_registration.objects.get(username=request.session['username'])

    p = available_Photographer.objects.get(pk=Photographer_id)

    if request.method == 'POST':
        # Extract data from the form
        username = request.POST.get('username', user.username)  # Default to logged-in user's username
        email = request.POST['email']
        phone = request.POST.get('phone')
        event_type = request.POST.get('event_type')
        event_date = request.POST.get('event_date')
        hours_needed = int(request.POST.get('hours_needed', 0))
        event_location = request.POST.get('event_location')
        hourly_rate = float(request.POST.get('hourly_rate', 0))  # Convert to float
        total_cost = hours_needed * hourly_rate
        additional_notes = request.POST.get('additional_notes')

        print('---------------------------------------------')
        print('Form submission details:')
        print(f"Event Type: {event_type}, Hourly Rate: {hourly_rate}, Event Location: {event_location},event_date:{event_date},")
        print(f"User: {user_details.username}")
        print(f"User: {user_details.email}")
        print(f"User: {user_details.phonenumber}")


        # Create and save the booking
        booking = Booking.objects.create(
            user=user_details,
            photographer_data=p,  # Use `p` as the photographer reference
            event_type=event_type,
            event_date=event_date,
            hourly_rate=hourly_rate,
            event_location=event_location,
            hours_needed=hours_needed,
            total_cost=total_cost,
            additional_notes=additional_notes,
            payment_status='successs',
            status='pending_approval'
        )
        booking.save()

        # Redirect to the payment page
        messages.success(request, 'Booking successful!')
        return redirect(payment,i=total_cost)  # Ensure 'payment' is defined in `urls.py`

        # Create a fallback route or template for errors

    return render(request, 'n.html', {
        'user': user,
        'rate': i,
        'Photographer_id': p,
        'user_details': user_details,
        'photographer_data': p,  # Include photographer details
    })

def payment(request,i):

    try:
        print(f"Received amount: {i}")
        amount = int(float(i)) * 100
        print(f"Converted amount to paise: {amount}")

        client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
        payment = client.order.create({
            'amount': amount,
            'currency': 'INR',
            'payment_capture': '1',
        })
        print(f"Razorpay order created: {payment}")

        booking = Booking.objects.last()


        return render(request, "payment.html", {
            'amount': amount / 100,
            'total': amount,
            'payment': payment,
            'booking': booking,

        })
    except Exception as e:
        print(f"Error: {e}")
        # return render("")
    return render(request,'payment.html')






from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages




# def approve_booking(request, booking_id):
#     if request.method == 'POST':
#         # Fetch the booking and update its status
#         booking = get_object_or_404(Booking, id=booking_id)
#         booking.status = 'approved'
#         booking.save()
#
#         # Optional: Add a success message
#         messages.success(request, 'Booking approved successfully!')
#
#         # Redirect to the admin dashboard or another page
#         return redirect('admin_dashboard')
# In views.py
from django.shortcuts import render
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings


def success(request):
    # Fetch the latest booking details
    booking = Booking.objects.last()  # Adjust this to target the correct booking if necessary

    # Update booking status to 'awaiting admin approval'
    booking.status = 'pending_approval'  # or 'awaiting_admin_approval'
    booking.save()

    # Optionally, send an email notification to the admin about the new booking


    # Pass the booking object to the template
    return render(request, 'success.html', {
        'booking': booking,
    })


def send_admin_notification(booking):
    """Send an email notification to the admin when a booking is made."""
    subject = f"New Booking for Approval: {booking.event_type} on {booking.event_date}"
    message = f"""
    A new booking has been made and is awaiting approval.

    Booking ID: {booking.id}
    Event Type: {booking.event_type}
    Event Date: {booking.event_date}
    Customer: {booking.user.username}
    Location: {booking.event_location}
    Total Cost: ₹{booking.total_cost}

    Please log in to the admin dashboard to review and approve the booking.

    Regards,
    Your Admin System
    """
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,  # Admin's email (configured in settings.py)
        [settings.ADMIN_EMAIL],  # Add your admin's email here or use dynamic fetching
    )


from django.shortcuts import render
from .models import Booking



def accept_booking(request):
    # Fetch all bookings that are pending approval
    pending_bookings = Booking.objects.filter(status='pending_approval')

    # Count unread notifications
    unread_count = Notification.objects.filter(is_read=False).count()

    # Debugging: Print the booking IDs to ensure they exist
    for booking in pending_bookings:
        print(f"Booking ID: {booking.id}")

    return render(request, 'admin_view_booking.html', {'pending_bookings': pending_bookings,'unread_count': unread_count})


# In views.py
from django.shortcuts import redirect, get_object_or_404
from .models import Booking

def approve_booking(request, booking_id):
    if request.method == 'POST':
        try:
            # Get the booking by ID
            booking = Booking.objects.get(id=booking_id)
            # Update status to approved
            booking.status = 'approved'
            booking.save()

            user_email = booking.user.email  # Assuming user has an email field
            send_mail(
                subject='Booking Approved',
                message=f'Dear {booking.user.username},\n\nYour booking with ID {booking.id} has been approved. The photographer {booking.photographer_data.user.username} will be in touch soon.\n\nThank you for choosing our service!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
                fail_silently=False,
            )
            # Return JSON response for AJAX
            return JsonResponse({'status': 'approved', 'booking_id': booking_id})
        except Booking.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Booking not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)



from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# def photographer_aproval(request):
#     # Get the logged-in photographer's username from the session
#     photographer_username = request.session.get('username')
#
#     if not photographer_username:
#         return HttpResponse("Session expired or not logged in. Please log in again.")
#
#     # Retrieve the photographer object using the username
#     photographer_user = camera_registration.objects.filter(username=photographer_username).first()
#
#     if not photographer_user:
#         return HttpResponse("Photographer not found in camera_registration.")
#
#     # Retrieve the available_Photographer object using the related user
#     photographer = available_Photographer.objects.filter(user=photographer_user).first()
#
#     if not photographer:
#         return HttpResponse("Photographer not found in available_Photographer.")
#
#     # Fetch only approved bookings for this photographer
#     approved_bookings = Booking.objects.filter(
#         photographer_data=photographer,
#         status='approved'  # Only show approved bookings
#     )
#
#     return render(request, 'photographer_aproval.html', {'approved_bookings': approved_bookings})

from django.utils.timezone import now

def photographer_aproval(request):
    photographer_username = request.session.get('username')

    if not photographer_username:
        return HttpResponse("Session expired or not logged in. Please log in again.")

    photographer_user = camera_registration.objects.filter(username=photographer_username).first()
    if not photographer_user:
        return HttpResponse("Photographer not found in camera_registration.")

    photographer = available_Photographer.objects.filter(user=photographer_user).first()
    if not photographer:
        return HttpResponse("Photographer not found in available_Photographer.")

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        try:
            booking = Booking.objects.get(id=booking_id, photographer_data=photographer, status='approved')
            booking.work_completed = True
            booking.work_completed_at = now()  # Record completion time
            booking.save()

            # Notify admin by creating an entry in a notification table (if applicable)
            # or simply make this visible in the admin dashboard.

            return JsonResponse({'status': 'success', 'message': 'Work marked as completed.'})
        except Booking.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Booking not found.'}, status=404)

    approved_bookings = Booking.objects.filter(photographer_data=photographer, status='approved')
    return render(request, 'photographer_aproval.html', {'approved_bookings': approved_bookings})

from django.http import JsonResponse

import json
from django.http import JsonResponse
from django.utils.timezone import now
from .models import Booking

from .models import Notification

def mark_work_completed(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            booking_id = data.get('booking_id')

            # Fetch the booking
            booking = Booking.objects.get(id=booking_id)

            # Update the booking to mark as completed
            booking.work_completed = True
            booking.work_completed_at = now()
            booking.save()

            # Create a notification for the admin
            Notification.objects.create(
                message=f"Photographer {booking.photographer_data.user.username} has completed booking ID {booking.id}."
            )

            return JsonResponse({'status': 'success', 'booking_id': booking_id})
        except Booking.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Booking not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid request data'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)



def admin_dashboard(request):
    # Count unread notifications
    unread_count = Notification.objects.filter(is_read=False).count()
    return render(request, 'admin_dashboard.html', {'unread_count': unread_count})

def admin_notification(request):
    notifications = Notification.objects.all()

    # Mark all unread notifications as read
    Notification.objects.filter(is_read=False).update(is_read=True)

    # Fetch unread notifications
    # notifications = Notification.objects.filter(is_read=False).order_by('-created_at')

    return render(request, 'admin_notification.html', {'notifications': notifications})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Notification

@csrf_exempt
def delete_notification(request, notification_id):
    if request.method == 'POST':
        try:
            notification = Notification.objects.get(id=notification_id)
            notification.delete()
            return JsonResponse({'status': 'success'})
        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notification not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})




from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import user_registration, PasswordReset

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            # Get the user by email
            user = user_registration.objects.get(email=email)

            # Generate a random token
            token = get_random_string(length=6)  # Generates a 6-character alphanumeric token

            # Create or update the PasswordReset record
            PasswordReset.objects.update_or_create(
                user=user,
                defaults={'token': token}  # Update the token if it exists
            )

            # Generate reset link
            reset_link = f'http://127.0.0.1:8000/reset_password/{token}'

            # Send reset email
            send_mail(
                'Reset Your Password',
                f'Hello {user.username},\n\nClick the link below to reset your password:\n{reset_link}\n\nIf you did not request this, please ignore this email.',
                'settings.EMAIL_HOST_USER',  # Replace with your email host user from settings
                [email],
                fail_silently=False
            )

            messages.success(request, "Password reset link has been sent to your email.")
            return redirect(login_view)  # Redirect to the login page or another relevant page

        except user_registration.DoesNotExist:
            messages.error(request, "Email not registered.")
            return redirect('forgot_password')

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect(forgot_password)

    return render(request, 'forgot.html')





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import PasswordReset

def reset_password(request, token):
    try:
        # Check if the token exists and is valid
        password_reset = get_object_or_404(PasswordReset, token=token)

        if request.method == 'POST':
            # Get the new password from the form
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password:
                # Update the user's password
                user = password_reset.user
                user.password = make_password(new_password)  # Hash the password
                user.save()

                # Delete the token after successful password reset
                password_reset.delete()

                messages.success(request, "Your password has been reset successfully.")
                return redirect(login_view)  # Redirect to login page
            else:
                messages.error(request, "Passwords do not match.")

        return render(request, 'reset.html', {'token': token})

    except PasswordReset.DoesNotExist:
        messages.error(request, "Invalid or expired token.")
        return redirect(forgot_password)


def feedback_thank_you(request):
    return render(request,'feedback_thank_you.html')

from .models import Feedback
from django.contrib.auth.decorators import login_required

def submit_feedback(request):
    user = user_registration.objects.get(username=request.session['username'])
    user_details = user_registration.objects.get(username=request.session['username'])



    if request.method == 'POST':
        # Handle feedback submission
        username = request.POST.get('username', user.username)  # Default to logged-in user's username
        rating = request.POST['rating']
        review = request.POST['review']
        # photographer = available_Photographer.objects.get(id=photographer_id)

        feedback = Feedback(
            user=user_details,

            # photographer=photographer,
            rating=rating,
            review=review
        )
        feedback.save()

        # Redirect or show success message
        return redirect(feedback_thank_you)  # Define a success URL for redirection

    return render(request, 'submit_feedback.html', {
        'user': user,
        'user_details': user_details,


    })

def admin_feedback_view(request):
    # Count unread notifications
    unread_count = Notification.objects.filter(is_read=False).count()
    # Get all feedbacks or filter as needed
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'admin_feedback_view.html', {'feedbacks': feedbacks,'unread_count': unread_count})


from django.shortcuts import render, redirect, get_object_or_404

def delete_feedback(request, feedback_id):
    # Get the feedback object, or return a 404 if not found
    feedback = get_object_or_404(Feedback, id=feedback_id)

    # Delete the feedback
    feedback.delete()

    # Redirect back to the feedback list page (admin dashboard in this case)
    return redirect('admin_feedback_view')  # Assuming 'admin_dashboard' is the name of the page showing feedbacks

def show_all_photographers_images(request):
    # Fetch all images uploaded by all photographers
    all_images = PhotographerImage.objects.all()

    # Filter images by category
    wedding_images = all_images.filter(category="Wedding")
    natural_images = all_images.filter(category="Natural")
    fashion_images = all_images.filter(category="Fashion")

    # Pass images to the context for the template
    context = {
        'wedding_images': wedding_images,
        'natural_images': natural_images,
        'fashion_images': fashion_images,
    }

    return render(request, 'photo.html', context)

def show_all_photographers_imagess(request):
    # Fetch all images uploaded by all photographers
    all_images = PhotographerImage.objects.all()

    # Filter images by category
    wedding_images = all_images.filter(category="Wedding")
    natural_images = all_images.filter(category="Natural")
    fashion_images = all_images.filter(category="Fashion")

    # Pass images to the context for the template
    context = {
        'wedding_images': wedding_images,
        'natural_images': natural_images,
        'fashion_images': fashion_images,
    }

    return render(request, 'gallery.html', context)