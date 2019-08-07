from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # Show a form for the user to fill out
    print("/////////// INDEX ROUTE SHOWING FORM //////////")
    return render(request,'index.html')

def process(request):
    # Process the form data then redirect
    print("/////////// FORM BEING PROCESSED //////////")
    print(request)
    print(request.POST)
    print(request.POST['num'])
    request.session['session_num'] = request.POST['num']
    print(request.session['session_num'])
    return redirect('/success')

def success(request):
    # This tells the user the form was successfully processed
    context = {
        'flavor_of_the_month' : 'Cookies & Cream'
    }
    return render(request,'success.html',context)