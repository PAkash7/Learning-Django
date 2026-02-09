from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import MarsStatus, Discovery

def home(request):
    data = MarsStatus.objects.all().order_by('-timestamp')[:1] # Get latest status
    discoveries = Discovery.objects.all().order_by('-date_posted')
    context = {
        "data": data,
        "discoveries": discoveries
    }
    return render(request, "mars/home.html", context)

def news(request):
    context = {
        'discoveries': Discovery.objects.all().order_by('-date_posted')
    }
    return render(request, "mars/news.html", context)

def new_release(request):
    latest_discovery = Discovery.objects.latest('date_posted')
    return render(request, "mars/discovery_detail.html", {'post': latest_discovery})

def monthly_news(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=30)
    month_discoveries = Discovery.objects.filter(date_posted__range=(start_date, end_date)).order_by('-date_posted')
    return render(request, "mars/news.html", {'discoveries': month_discoveries, 'filter_title': 'Monthly Updates'})

def yearly_news(request):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=365)
    year_discoveries = Discovery.objects.filter(date_posted__range=(start_date, end_date)).order_by('-date_posted')
    return render(request, "mars/news.html", {'discoveries': year_discoveries, 'filter_title': 'Yearly Updates'})
# Create your views here.
def about(request):
    return render(request, "mars/about.html",{"title": "About"} )