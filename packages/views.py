from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.urls import reverse

from .models import TravelPackage, Booking

from .tasks import generate_pdf_invoice, send_confirmation_email
from .utils import validate_booking, calculate_total_price
import threading
from decimal import Decimal
from datetime import datetime


def book_package(request, pk):
    
    package = get_object_or_404(TravelPackage, pk=pk)
    return render(request, 'travel_package_booking.html', {'package': package})


from django.shortcuts import render
from .models import TravelPackage

def travel_package_list(request):
    """
    Renders a list of all travel packages along with rating options.

    Returns:
        HttpResponse: The rendered list page displaying all travel packages and rating options.
    """
    # Obtendo a lista completa de pacotes
    travel_packages = TravelPackage.objects.all()
    
    # Pegando a consulta de pesquisa da URL, caso haja
    search_query = request.GET.get('search', '')

    # Se houver um termo de pesquisa, filtramos os pacotes
    if search_query:
        travel_packages = travel_packages.filter(name__icontains=search_query) | travel_packages.filter(description__icontains=search_query)

    # Definindo o intervalo de avaliação (1 a 5 estrelas)
    ratings_range = range(1, 6)

    # Renderizando o template com os pacotes filtrados (se houver pesquisa)
    return render(request, 'travel_package_list.html', {
        'packages': travel_packages,
        'ratings_range': ratings_range
    })

from django.utils.timezone import make_aware
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def booking_handler_view(request, package_id):
    package = get_object_or_404(TravelPackage, id=package_id)
    child_discount = Decimal('1')

    if request.method == 'POST':
        # Fetch form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        booking_date = request.POST.get('datetime')
        num_adults = int(request.POST.get('SelectPerson', 0))
        num_children = int(request.POST.get('SelectKids', 0))
        gender = request.POST.get('SelectGender', 'None')
        payment_method = request.POST.get('payment_method', '0')
        consent = request.POST.get('consent')

        # Server-side validations
        errors = validate_booking(name, email, booking_date, num_adults, num_children, payment_method, consent)

        # If there are errors, return the same form with errors
        if errors:
            print(f"Error: {errors}")
            return render(request, 'travel_package_booking.html', {
                'package': package,
                'name': name,
                'email': email,
                'booking_date': booking_date,
                'num_adults': num_adults,
                'num_children': num_children,
                'gender': gender,
                'payment_method': payment_method,
                'errors': errors  # Pass errors to the template
            })

        # Calculate total price
        total_price = calculate_total_price(package, num_adults, num_children, child_discount)

        # Convert naive booking_date to an aware datetime
        naive_datetime = datetime.strptime(booking_date, '%Y-%m-%d')
        aware_datetime = make_aware(naive_datetime)

        # Save booking with pending payment
        booking = Booking.objects.create(
            package=package,
            name=name,
            email=email,
            datetime=aware_datetime,  # Use the aware datetime
            num_adults=num_adults,
            num_children=num_children,
            total_price=total_price,
            gender=gender,
            payment_status='Pending',  # Default to Pending
            payment_method=payment_method
        )

        # If payment method is online, generate payment URL
        if payment_method == "Stripe":
            # Cria um produto e um preço no Stripe
            product = stripe.Product.create(name=f'Booking for {package.name}')
            price = stripe.Price.create(
                product=product.id,
                unit_amount=int(total_price * 100),  # Convertendo para centavos
                currency='usd'
            )

            # Gera o link de pagamento
            payment_link = stripe.PaymentLink.create(
                line_items=[
                    {
                        'price': price.id,
                        'quantity': 1,
                    },
                ],
            )

            # Atualiza o status do pagamento e redireciona o usuário
            if payment_link.url:
                booking.payment_status = 'Pending'  # Atualiza o status para 'Pending'
                booking.save()
                print(f"Booking mail ok: {booking.id}")
                thread = threading.Thread(target=generate_pdf_invoice, args=({booking.id}))
                thread.start()
                return redirect(payment_link.url)
            else:
                # Se o URL de pagamento não puder ser gerado, retorna a página de erro
                booking.delete()
                return redirect(reverse('booking_fail'))

        print(f"Booking mail ok: {booking.id}")
        send_confirmation_email(args=[name, email, package.name, total_price])
        generate_pdf_invoice(args=[booking.id])
        return redirect(reverse('booking_success'))

    return render(request, 'travel_package_booking.html', {'package': package})


    return render(request, 'travel_package_booking.html', {'package': package})


def booking_success(request):
    """
    Renders the booking success page after a successful booking.
    Returns:
        HttpResponse: Renders the 'booking_success.html' template to show the user the booking confirmation.
    """
    return render(request, 'booking_success.html') 


def booking_fail(request):
    """
    Renders the booking failure page when a booking attempt    """
    return render(request, 'booking_fail.html')  
def packages_view(request):
    search_query = request.GET.get('search', '')
    packages = Pac.objects.all()

    if search_query:
        packages = packages.filter(name__icontains=search_query) | packages.filter(description__icontains=search_query)

    return render(request, 'your_template.html', {'packages': packages})


 