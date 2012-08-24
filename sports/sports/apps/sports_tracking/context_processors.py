from sports_tracking.models import Sport

def sport_FF(request):
    return{
        "sport_FF" : Sport.objects.get(type="FF").display()
    }

def sport_VB(request):
    return{
        "sport_VB" : Sport.objects.get(type="VB").display()
    }

def sport_BB(request):
    return{
        "sport_BB" : Sport.objects.get(type="BB").display()
    }

def sport_SR(request):
    return{
        "sport_SR" : Sport.objects.get(type="SR").display()
    }

def sport_SB(request):
    return{
        "sport_SB" : Sport.objects.get(type="SB").display()
    }

def sport_HY(request):
    return{
        "sport_HY" : Sport.objects.get(type="HY").display()
    }
