from django.shortcuts import render
from django.http import HttpResponse
# Import the Category model
from rango.models import Category



def index(request):
    # Query the database for a list of the top 5 categories 
    # by the number of likes in descending order.
    category_list = Category.objects.order_by('-likes')[:5]
    
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # Render the response
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')