from django.shortcuts import render_to_response, Http404, HttpResponse, render 
from django.http import HttpResponseRedirect   # get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import Share
from forms import ShareForm
from userprofile.models import Userprofile

#from PIL import Image

"""
signals, profile, edit_profile, formular, list adds
"""


"""
def ads(request):
    ads = Share.objects.filter(status='A') # order_by('-created') in meta model
    return render_to_response('share/index.html',
                             {'ads': ads},
                             context_instance=RequestContext(request))
"""
    
def detail(request, pk):
    
    try:
        ad = Share.objects.get(pk=pk)
    except:
        return HttpResponse(404)
        # return HttpResponseRedirect('/add_does_not_exist/')
        # return redirect('detail')

    return render_to_response('share/detail.html', {'ad': ad},
                              context_instance=RequestContext(request)
                              )

@login_required
def add_ad(request):
    """
    >>> a = 'a'
    >>> a
    a
    """
    if request.method == 'POST':
        form = ShareForm(request.POST, request.FILES)
        if form.is_valid():
            new_ad = form.save(commit=False)
            new_ad.user = request.user.profile
            new_ad.status = 'A'
            new_ad.save()               
            return HttpResponseRedirect('/ads/')
    else:
        form = ShareForm()
    return render_to_response(
        'share/add_ad.html',
        {'form': form}, 
        context_instance=RequestContext(request)
    )
    
@login_required
def delete_ad(request, pk):
    ad = Share.objects.get(pk=pk)
    ad.delete()
 
    user = Userprofile.objects.get(user = request.user)
    user_adds = user.share_set.all()
    return render_to_response('userprofile/index.html', 
                             {'user' : user,
                              'user_adds': user_adds,
                              },
                             context_instance=RequestContext(request))
@login_required
def edit_ad(request, pk):
    ad = Share.objects.get(pk=pk)
    if request.method == 'POST':
        form = ShareForm(request.POST, request.FILES, instance = ad)
        if form.is_valid():
            form.save()               
            user = Userprofile.objects.get(user = request.user)
            user_adds = user.share_set.all()
            return render_to_response('userprofile/index.html', 
                             {'user' : user,
                              'user_adds': user_adds,
                              },
                             context_instance=RequestContext(request))
    else:
        form = ShareForm(instance = ad)
    return render_to_response(
        'share/add_ad.html',
        {'form': form}, 
        context_instance=RequestContext(request)
    )

