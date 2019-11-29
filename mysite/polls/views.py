from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import question, choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# Create your views here.
def index(request):
    latest_q= question.objects.order_by('-pub_date')
    context = {'latest_question':latest_q}
    return render(request,"polls/index.html",context)

def question_id(request,question_id):
    q= get_object_or_404(question,pk=question_id)
    context={'question':q}
    return render(request,"polls/details.html",context)

def result(request,question_id):
    q = get_object_or_404(question,pk=question_id)
    return render(request,"polls/result.html",{'question':q})

def vote(request,question_id):
    q = get_object_or_404(question,pk=question_id)
    try:
        selected_choice= q.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,"polls/details.html",{'question':q, 'error_message':" choice one !!!"})
    else :
        selected_choice.voit+=1
        selected_choice.save()

        return HttpResponsePermanentRedirect(reverse("polls:result",args=(q.id,)))
