from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def member_details(request):
    return render(request, 'member_details.html')
def member_list(request):
    return render(request, 'member_list.html')
def profile(request):
    return render(request, 'profile.html')
