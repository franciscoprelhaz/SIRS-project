from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from log.forms import UserForm, UserProfileForm
#from django.template import RequestContext

# Create your views here.
#login required is to not allow any non authenticated views
@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")


def register(request):
    #context = RequestContext(request)
    registered = False

    #if HTTP Post process data
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #save user to the db
            user = user_form.save()
            #hash the password
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    #render forms to blank
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render('log/register.html',
                  {'user_form': user_form,
                  'profile_form': profile_form,
                  'registered': registered,},
                  request
                  )


