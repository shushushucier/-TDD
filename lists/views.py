from django.shortcuts import render

# Create your views here.
def home_page(request):
	return render(request, 'home.html')
	# return HttpResponse('<html><title>To-Do lists</title></html>')