from django.shortcuts import render
def greeting(request):
    if request.GET:
        name = request.GET.get('username')
        return render(request,'output.html',{
            'name': name,
        })
    return render(request,'input.html' )
