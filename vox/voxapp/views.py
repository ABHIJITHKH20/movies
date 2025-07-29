from django.shortcuts import render, get_object_or_404, redirect
from .models import vox, Booking
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'homepage.html')

def vox_list(request):
    vox_movies = vox.objects.all()
    return render(request, 'main.html', {'vox_movies': vox_movies})

@login_required
def book_movie(request, movie_id):
    movie = get_object_or_404(vox, id=movie_id)


    booked_seats = []
    all_bookings = Booking.objects.filter(movie=movie)
    for booking in all_bookings:
        booked_seats.extend(booking.seats.split(','))

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats')


        overlap = set(selected_seats) & set(booked_seats)
        if overlap:
            messages.error(request, f"Seats already booked: {', '.join(overlap)}")
            return redirect('book_movie', movie_id=movie.id)

        booking = Booking.objects.create(
            movie=movie,
            user=request.user,
            seats=','.join(selected_seats),
            tickets=len(selected_seats),
            price_per_ticket=movie.price
        )

        messages.success(request, "Seats successfully booked!")
        return redirect('payment_page', movie_id=movie.id)

    return render(request, 'book movie.html', {
        'movie': movie,
        'booked_seats': booked_seats
    })


@login_required
def payment_page(request, movie_id):
    movie = get_object_or_404(vox, id=movie_id)
    latest_booking = Booking.objects.filter(movie=movie, user=request.user).order_by('-booking_time').first()

    if not latest_booking:
        messages.error(request, "No recent booking found. Please book the seats first.")
        return redirect('book_movie', movie_id=movie.id)

    # Make sure booking.tickets is the number of seats selected
    total_price = latest_booking.tickets * movie.price  # Ensure ticket price is correct

    return render(request, 'payment.html', {
        'movie': movie,
        'booking': latest_booking,
        'total_price': total_price  # Ensure total_price is correctly passed here
    })



@login_required
def process_payment(request):
    if request.method == "POST":
        movie_id = request.POST.get('movie_id')
        movie = get_object_or_404(vox, id=movie_id)
        latest_booking = Booking.objects.filter(movie=movie, user=request.user).order_by('-booking_time').first()

        return redirect('payment_success', booking_id=latest_booking.id)
    
    return redirect('home')


@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    movie = booking.movie

    # Calculate total price in case it's missing
    total_price = booking.tickets * movie.price  # Ensure this is correct

    return render(request, 'payment_success.html', {
        'booking': booking,
        'movie': movie,
        'total_price': total_price,  # Pass total_price here
    })




def login_view(request):
    if request.method == 'POST':
        # TODO: Add login logic here
        return redirect('home')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        # TODO: Add registration logic here
        return redirect('home')
    return render(request, 'register.html')









def search(request):
    query = request.GET.get('query', '')
    print(f"Search query: {query}")  # Debugging print statement
    results = vox.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_result.html', {'query': query, 'results': results})

