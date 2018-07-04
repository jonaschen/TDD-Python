from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

# Return type: HttpResponse Object
def home_page(request):
	#return HttpResponse('<html>' + '<title>To-Do lists</title>' + '</html>')
	#return render(request, 'home.html')

	# get an item value from the Http Post Object
	# combines the html template with the value
	# returns an HttpResponse object with that rendered text.
	return render(request, 'home.html', {
		'new_item_text': request.POST.get('item_text', ''),
	})
