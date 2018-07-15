from django.shortcuts import render
from lists.models import Item
#from django.http import HttpResponse

# Create your views here.

# Return type: HttpResponse Object
def home_page(request):
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text)
	else:
		new_item_text = ''

	# get an item value from the Http Post Object
	# combines the html template with the value
	# returns an HttpResponse object with that rendered text.
	return render(request, 'home.html', {
		'new_item_text': new_item_text,
	})
