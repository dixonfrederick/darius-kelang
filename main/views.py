from django.shortcuts import render
from authuser.views import getBalance



@api_view(['GET'])
#@permission_classes((IsAuthenticated, ))
def homePageView(request):
    if request.user.is_authenticated:
        balance = getBalance(request.user.username)
    else:
        balance = 0
    return render(request, 'main/main.html', {'balance': balance})
