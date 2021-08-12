from django.contrib.auth.decorators import login_required
from django.db.models.fields import AutoField
from django.shortcuts import render, get_object_or_404, redirect
from .models import Community, Reply
from django.utils import timezone
from .forms import CommentForm

# Create your views here.

def communityhome(request):
    community=Community.objects
    return render(request, 'communityhome.html',{'communitys':community})

def communityhome1(request):
    community=Community.objects
    return render(request, 'write.html',{'communitys':community})

def reply1(request):
    reply=Reply.objects
    return render(request, 'mypage.html',{'replys':reply})

def new(request):
    return render(request, 'new.html')

def detail(request, community_id):
    community_detail=get_object_or_404(Community, pk=community_id)
    return render(request,'detail.html',{'community':community_detail, 'replys':reply})

def create(request):
    community=Community()
    community.author=request.user
    community.title=request.POST.get('title')
    community.body=request.POST.get('body')
    community.pub_date=timezone.now() 
    community.save()
    return redirect('communityhome')

@login_required
def create1(request):
    logged_in_user=request.user
    logged_in_user_own=Community.objects.filter(author=request.user)
    return render(request, 'write.html', {'myown': logged_in_user_own})



def reply(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid(): #유효성 검사
            reply = form.save(commit=False)
            reply.post = community
            reply.save()
            return redirect('detail', community_id)
    else:
        form = CommentForm()
    return render(request, 'reply.html', {'form' : form})

