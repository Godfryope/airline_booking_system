from django.shortcuts import render
from .models import Flight

def search_flights(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '').lower()
        flights = Flight.objects.all()

        matching_flights = []
        for flight in flights:
            if search_query in flight.flight_number.lower() or \
               search_query in flight.origin.lower() or \
               search_query in flight.destination.lower():
                matching_flights.append(flight)

        return render(request, 'flights/search_results.html', {'flights': matching_flights})
    
    return render(request, 'flights/flights.html')
