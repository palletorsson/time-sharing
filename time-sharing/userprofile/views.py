from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Userprofile
from django.contrib.auth.decorators import login_required
from forms import UserprofileForm


def view_profile(request):
    """
    signals, profile, edit_profile, formular, list adds

    
    """

    user = Userprofile.objects.get(user = request.user)
    user_adds = user.share_set.all()
    print user_adds

    return render_to_response('userprofile/index.html', 
                             {'user' : user,
                              'user_adds': user_adds,
                              },
                             context_instance=RequestContext(request))

@login_required
def edit(request):
    userprofile = Userprofile.objects.get(user = request.user)
    if request.method == 'POST':
        form = UserprofileForm(request.POST, request.FILES, instance = userprofile)
        if form.is_valid():
            form.save()
            user_adds = userprofile.share_set.all()
            return render_to_response('userprofile/index.html', 
                             {'user' : userprofile,
                              'user_adds': user_adds,
                              },
                             context_instance=RequestContext(request))
    else:
        form = UserprofileForm(instance=userprofile)
        return render_to_response('userprofile/edit_user.html', {
            'form': form,
        }, context_instance=RequestContext(request))
