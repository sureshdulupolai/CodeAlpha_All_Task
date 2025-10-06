from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Event, Registration
from .forms import EventForm  # We'll use a ModelForm for adding events

# List all events
def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'eventapp/event_list.html', {'events': events})

# View details of a single event
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'eventapp/event_detail.html', {'event': event})

# Register for an event
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Registration.objects.create(name=name, email=email, event=event)
        return render(request, 'eventapp/success.html', {'event': event})
    return render(request, 'eventapp/register.html', {'event': event})

# API endpoint: List of events (JSON)
def api_event_list(request):
    events = list(Event.objects.values('id', 'title', 'description', 'date', 'location'))
    return JsonResponse(events, safe=False)

# Optional: Add new event (for organizers/admin)
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventapp:event_list')
    else:
        form = EventForm()
    return render(request, 'eventapp/add_event.html', {'form': form})
