from django.shortcuts import render
from django.http import HttpResponse
from .models import AdTracking
from django.db.models import Count, Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


# Create your views here.
def index(request):
    return HttpResponse("Testing to add new ads")

# views.py


# Login not required for this view
@login_required
def track_ad_click(request):
    if request.method == 'POST':
        ad_id = request.POST.get('ad_id')
        user = request.user
        ad_tracking, created = AdTracking.objects.get_or_create(user=user, ad_id=ad_id, defaults={'clicks': 1})
        if not created:
            ad_tracking.clicks += 1
            ad_tracking.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


# Login not required for this view
@login_required
def track_ad_download(request):
    if request.method == 'POST':
        ad_id = request.POST.get('ad_id')
        user = request.user
        ad_tracking, created = AdTracking.objects.get_or_create(user=user, ad_id=ad_id, defaults={'downloads': 1})
        if not created:
            ad_tracking.downloads += 1
            ad_tracking.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})



def ad_tracking_metrics(request):
    ad_tracking_data = AdTracking.objects.values('ad_id', 'user__username').annotate(
        total_clicks=Sum('clicks'),
        total_downloads=Sum('downloads')
    ).order_by('ad_id')

    context = {
        'ad_tracking_data': ad_tracking_data,
    }

    return render(request, 'ads/metrics.html', context)