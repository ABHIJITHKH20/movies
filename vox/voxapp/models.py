# from django.db import models
# from django.contrib.auth.models import User

# class vox(models.Model):
#     STATUS_CHOICES = [
#         ('NOW Showing', 'NOW Showing'),
#         ('Upcoming', 'Upcoming')
#     ]
#     title = models.CharField(max_length=255)
#     genre = models.CharField(max_length=255)
#     language = models.CharField(max_length=50)
#     duration = models.IntegerField()
#     release_date = models.DateField()
#     image = models.ImageField(upload_to='movies/', null=True)
#     showtime = models.CharField(max_length=50, default="00")
#     screen = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)

#     def __str__(self):
#         return self.title


# class Booking(models.Model):
#     movie = models.ForeignKey('vox', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     seats = models.CharField(max_length=255)  # e.g. "A1,B2,C3"
#     booking_time = models.DateTimeField(auto_now_add=True)
#     tickets = models.PositiveIntegerField(default=1)  # Number of tickets
#     price_per_ticket = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)

#     @property
#     def total_price(self):
#         return self.tickets * self.price_per_ticket

#     def __str__(self):
#         return f"{self.movie.title} - {self.user.username} - {self.seats}"













from django.db import models
from django.contrib.auth.models import User

class vox(models.Model):
    STATUS_CHOICES = [
        ('NOW Showing', 'NOW Showing'),
        ('Upcoming', 'Upcoming')
    ]
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    release_date = models.DateField()
    image = models.ImageField(upload_to='movies/', null=True)
    showtime = models.CharField(max_length=50, default="00")
    screen = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)
    trailer_url = models.URLField(max_length=500, blank=True, null=True)  # For external links (YouTube/Vimeo)
    

    def __str__(self):
        return self.title


class Booking(models.Model):
    movie = models.ForeignKey('vox', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.CharField(max_length=255)  # e.g. "A1,B2,C3"
    booking_time = models.DateTimeField(auto_now_add=True)
    tickets = models.PositiveIntegerField(default=1)
    price_per_ticket = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)

    @property
    def total_price(self):
        return self.tickets * self.price_per_ticket

    def __str__(self):
        return f"{self.movie.title} - {self.user.username} - {self.seats}"

