# Django Imports
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib.auth.models import User

# Third-Party Imports
from weasyprint import HTML
import numpy as np
import os
import datetime

# Local Imports
from .models import Booking

def send_confirmation_email(name, email, package_name, total_price):
     
    subject = f"Booking Confirmation for {package_name}"
    print('Sending email...')
    message = render_to_string('confirmation_email.html', {
        'name': name,
        'package_name': package_name,
        'total_price': total_price
    })
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        html_message=message  
    )




def generate_pdf_invoice(booking_id):
   #gerra um pdv usando Threads (nota: Não e uma boa pratica por ser muito lento,procurar alternativas mais rapidas depois )
    
    booking = Booking.objects.get(id=booking_id)
    discount = (booking.package.price * 50 / 100) * booking.num_children
    today = datetime.date.today()
    print('Generating PDF invoice...')

    html_content = render_to_string('invoice.html', {'booking': booking, 'discount': discount, 'today': today})

    pdf = HTML(string=html_content).write_pdf()

    fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'invoices'))
    filename = f'invoice_{booking.id}.pdf'
    pdf_file = ContentFile(pdf)  

    fs.save(filename, pdf_file)

    print(f'PDF invoice saved as {filename}')

    return filename

