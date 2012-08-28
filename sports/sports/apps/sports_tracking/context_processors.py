from sports_tracking.models import Sport

def sports(request):
    sports = {}
    for type in Sport.SPORTS_CHOICES:
        sports[type[0]] = Sport.objects.get(type=type[0])
    return {"sports":sports}
