from django.shortcuts import render_to_response, Http404, HttpResponse, render 
from django.http import HttpResponseRedirect   # get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import Share
from forms import ShareForm
from PIL import Image

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
    