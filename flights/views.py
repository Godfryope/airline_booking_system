from django.shortcuts import render
from .models import Flight, Passenger

def search_seat(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '').lower()
        passengers = Passenger.objects.filter(seat_number__icontains=search_query)

        return render(request, 'flights/seat_search_results.html', {'passengers': passengers})
    
    return render(request, 'flights/seat_search.html')
