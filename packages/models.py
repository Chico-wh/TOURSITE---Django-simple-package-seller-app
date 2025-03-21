from django.db import models

class TravelPackage(models.Model):
    
    name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    package_type = models.CharField(max_length=50, choices=[
        ('Beach', 'Beach'),
        ('Adventure', 'Adventure'),
        ('Cultural', 'Cultural'),
        ('Family', 'Family'),
        ('Relaxation', 'Relaxation'),
        ('City', 'City'),
    ])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  
    rating = models.DecimalField(max_digits=3, decimal_places=1)  
    description = models.TextField()
    available = models.BooleanField(default=True)  
    tags = models.ManyToManyField('Tag', related_name='travel_packages', blank=True)
    image = models.ImageField(upload_to="packages/", null=True, blank=True) 

    def __str__(self):
        return self.name 


class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(
        max_length=50,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('None', 'None')],
        default='None'  
    )
    datetime = models.DateTimeField()
    
    num_adults = models.PositiveIntegerField(default=0) 
    num_children = models.PositiveIntegerField(default=0)  
    payment_method = models.CharField(
        max_length=50,
        choices=[('Stripe', 'Stripe'), ('Stripe', 'Stripe')],
        default='None'  
    )
    package = models.ForeignKey('TravelPackage', on_delete=models.CASCADE, related_name='bookings')
    payment_status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending' )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Booking by {self.name} for {self.package.name}"


class Tag(models.Model):
    """
Representa uma etiqueta para categorizar pacotes de viagem (por exemplo, 'Romântico', 'Aventura').    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Citys(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Hoteis(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(Citys, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
categories = [
    ('Standard', 'Standard'),
    ('Superior', 'Superior'),
    ('Luxo', 'Luxo'),

]

class HotelTarifa(models.Model):
    hotel = models.ForeignKey(Hoteis, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    Categorie = models.CharField(max_length=50, choices=categories)
    single = models.DecimalField(max_digits=10, decimal_places=2)
    price_single = models.DecimalField(max_digits=10, decimal_places=2)
    double = models.DecimalField(max_digits=10, decimal_places=2)
    price_double = models.DecimalField(max_digits=10, decimal_places=2)
    triple = models.DecimalField(max_digits=10, decimal_places=2)
    price_triple = models.DecimalField(max_digits=10, decimal_places=2)

    def Validation(self):
        if self.end_date < self.start_date:
            return "Data de encerramento não pode ser anterior à data de início"
        return "Data de validade válida"
        
    
    def __str__(self):
        return f"{self.hotel.name} - {self.start_date} - {self.end_date}"

