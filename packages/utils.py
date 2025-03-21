from django.conf import settings
from datetime import datetime, date
import uuid
import requests

def validate_booking(name, email, booking_date, num_adults, num_children, payment_method, consent):
  
    errors = {}
    if '@' not in email:
        errors['email'] = "Invalid email address."
    if not booking_date or datetime.strptime(booking_date, '%Y-%m-%d').date() < date.today():
        errors['datetime'] = "The date must be today or a future date."
    if num_adults <= 0:
        errors['SelectPerson'] = "Number of persons must be at least 1."
    if num_children < 0:
        errors['SelectKids'] = "Number of kids cannot be negative."
    if not payment_method:
        errors['payment_method'] = "Payment method is required."
    if not consent:
        errors['consent'] = "You must agree to the terms and conditions."
    return errors


def calculate_total_price(package, num_adults, num_children, child_discount):
    """
   Calcula o preço total de um pacote de viagem com base no número de adultos, crianças e um desconto para crianças.

Argumentos:

package (PacoteDeViagem): O pacote de viagem que está sendo reservado.

num_adults (int): Número de adultos.

num_children (int): Número de crianças.

child_discount (Decimal): Desconto para crianças (por exemplo, 0,5 para 50%).

Retorna:

Decimal: O preço total da reserva.

Exemplo:
    """
    unit_price = package.price
    adults_price = unit_price * num_adults
    children_price = (unit_price * child_discount) * num_children
    return adults_price + children_price

