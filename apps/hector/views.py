from django.shortcuts import render, HttpResponse, redirect

def index (request):
    return render(request, 'hector/index.html')

def process(request):
    print "process"
    request.session['name'] = request.POST['name']
    print request.session['name']
    request.session['password'] = request.POST['password']
    print request.session['password']
    return redirect('/login')

def login(request):
    print "login"
    return render(request, 'hector/login.html')

def compare(request):
    print "compare"
    request.session['name2'] = request.POST['name2']
    x = request.session['name']
    y = request.session['name2']
    print x
    print y

    request.session['password2'] = request.POST['password2']
    a = request.session['password']
    b = request.session['password2']
    print a
    print b

    if x == y and a == b:
        return HttpResponse('Match')
    return HttpResponse("No match")

def reset(request):
    request.session.clear()
    return redirect('/')

def odell(request):
    return HttpResponse('Catches Everything')
