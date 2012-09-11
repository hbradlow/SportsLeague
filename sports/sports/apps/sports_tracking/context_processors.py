from sports_tracking.models import Sport

def sports(request):
    sports = []
    for type in Sport.SPORTS_CHOICES:
        try:
            sports.append(Sport.objects.get(type=type[0]))
        except:
            pass
    return {"sports":sports}
