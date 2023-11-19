from django.shortcuts import render
def squareprism(request):
    context={}
    context['area'] = "0"
    context['b'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        b = request.POST.get('base','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('Base=',b)
        print('Height=',h)
        area = int(b) * int(h)
        context['area'] = area
        context['b'] = b
        context['h'] = h
        print('Area=',area)
    return render(request,'myapp/math.html',context)