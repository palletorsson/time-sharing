from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Userprofile
from django.contrib.auth.decorators import login_required
from models import Userprofile
from forms import UserprofileForm
from PIL import Image


def view_profile(request):
    """
    signals, profile, edit_profile, formular, list adds
    """

    user = Userprofile.objects.get(id = request.user.id)
    user_adds = user.share_set.all()
    print user_adds

    return render_to_response('userprofile/index.html', 
                             {'user' : user,
                              'user_adds': user_adds,
                              },
                             context_instance=RequestContext(request))


@login_required
def edit(request, id=None, template_name='userprofile/edit_user.html'):
    userprofile = Userprofile.objects.get(id = request.user.id)
    #u = user.user
    if request.method == 'POST':
        form = UserprofileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            edit_user = form.save(commit=False)
            edit_user.user = request.user
            edit_user.save()
            return HttpResponseRedirect('accounts/profile/')

    else:
        form = UserprofileForm(instance=userprofile)

    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))
