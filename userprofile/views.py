from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Userprofile



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

