from django.shortcuts import render

# Create your views here.
def post_index(request):
    return render(request, 'account/post_index.html', {})

def post_sign_up(request):
    return render(request, 'account/sign_up.html', {})
