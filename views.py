from django.http import Http404
from django.shortcuts import render
import datetime

def about(request):
    return render(request, 'content/about.html')

def home(request):
    return render(request, 'content/home.html')

def library_services(request):
  return render(request, 'content/library-services.html')  

def privacy_policy(request):
  return render(request, 'content/privacy-policy.html')    

def products(request):
  return render(request, 'content/products.html')
  
def publisher_services(request):
  return render(request, 'content/publisher-services.html')
    
def terms_of_service(request):
  return render(request, 'content/terms-of-service.html')    
    
    
      
#def current_datetime(request):
#    return render_to_response('current_datetime.html', 
#                              {'current_date': datetime.datetime.now()})
#
#def hours_ahead(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
#    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#    return HttpResponse(html)
