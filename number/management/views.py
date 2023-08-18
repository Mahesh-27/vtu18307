from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def fetch_nums(request):
    links = request.GET.getlist('url')

    if not links:
        return JsonResponse({'error': 'No URLs provided'}, status=400)

    nums = []

    for l in links:
        try:
            response = requests.get(l, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                nums.extend(data.get('nums', []))
        except requests.Timeout:
            pass  

    unique_sorted_numbers = sorted(list(set(nums)))
    return JsonResponse({'nums': unique_sorted_numbers})
