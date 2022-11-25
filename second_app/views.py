from django.shortcuts import render

from second_app.models import User

# Create your views here.


def index(request):
    return render(request,'apps_templates_two/index.html')

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'User': user_list}
    return render(request,'apps_templates_two/users.html', context=user_dict)