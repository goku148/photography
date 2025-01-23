from django.db import models

# Create your models here.



class user_registration(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)             # user registration
    is_accepted = models.BooleanField(default=False)

    def _str_(self):
        return self.username


class camera_registration(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    username = models.CharField(max_length=30)              # photographer registration
    password = models.CharField(max_length=10)
    experience = models.TextField()
    qualifications = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Added ImageField
    is_accepted = models.CharField(max_length=30,default='pending')

    def _str_(self):
        return self.username

class PhotographerImage(models.Model):
    photographer = models.ForeignKey(
        'camera_registration',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='photographer_images/')
    category = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class available_Photographer(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
    ]


    user = models.ForeignKey(camera_registration, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='photographers/', null=True)
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, help_text="Hourly rate in INR")
    portfolio_link = models.URLField(max_length=500)
    is_accepted = models.CharField(max_length=10, choices=STATUS_CHOICES,default='PENDING')  # New field for admin approval

    def __str__(self):
        return self.user.username


from django.db import models

from django.db import models



class Booking(models.Model):




    # ForeignKey to the user_registration model
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE, related_name='bookings')
    photographer_data = models.ForeignKey(available_Photographer, on_delete=models.CASCADE)


    # Fields for the photography booking form
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()


    event_location = models.CharField(max_length=200)
    hours_needed = models.PositiveIntegerField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    additional_notes = models.TextField(blank=True, null=True)
    payment_status = models.CharField(max_length=20, default='pending')
    status = models.CharField(max_length=20, default='pending')
    work_completed = models.BooleanField(default=False)
    work_completed_at = models.DateTimeField(null=True, blank=True)  # Optional timestamp

    def __str__(self):
        return f"Booking by {self.user.username} on {self.event_date} at {self.event_type}"

    def calculate_total_cost(self):
        """Calculate the total cost based on hours needed and hourly rate."""
        return self.hours_needed * self.hourly_rate

    def save(self, *args, **kwargs):
        """Override save method to automatically calculate total cost."""
        if not self.total_cost:
            self.total_cost = self.calculate_total_cost()
        super().save(*args, **kwargs)


class add_product(models.Model):
    productname=models.CharField(max_length=20)
    productprice=models.CharField(max_length=10)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')

class cart(models.Model):
    user_details=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    product_id=models.ForeignKey(add_product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

class PasswordReset(models.Model):
    user=models.ForeignKey(user_registration,on_delete=models.CASCADE)
    # photographer=models.ForeignKey(camera_registration,on_delete=models.CASCADE)
    token=models.CharField(max_length=20)





class Feedback(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)  # The user providing the feedback

    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating out of 5
    review = models.TextField(blank=True, null=True)  # Optional detailed review
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds the feedback timestamp

    def __str__(self):
        return f"Feedback by {self.user.username}"

from django.db import models
from django.utils.timezone import now

class Notification(models.Model):
    message = models.TextField()  # The notification message
    created_at = models.DateTimeField(default=now)  # Timestamp of the notification
    is_read = models.BooleanField(default=False)  # To mark if the notification is read

    def __str__(self):
        return f"Notification: {self.message[:50]}..."