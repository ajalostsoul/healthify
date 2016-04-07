# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Voters,Question,Question_Setter
import re

def home(request):
    registered=False
    if request.session.get('email',False):
        registered=True
    return render(request,'signup.html',{'registered':registered})

def success(request):
    
    errors={}
    if request.method=="POST":
        
        match=re.match(r'[^@]+@[^@]+\.[^@]+',request.POST.get('email')) 
       # if (not request.POST.get('email','')) or :
        if not match:
            errors['email']="Enter a valid Email"
        if not request.POST.get('firstname',''):
            errors['firstname']="Firstname cant be empty"
            
        if len(errors)==0:
            first_name=request.POST.get('firstname','')
            last_name=request.POST.get('lastname','')
            email=request.POST.get('email')
            
            if Voters.objects.filter(email=email):
                msg="This id is already in use"
                return render (request,'signup.html',{'msg':msg,'email':request.POST.get('email','')})
            else:
                request.session['email']=email
                s=Voters(first_name=first_name,last_name=last_name,email=email)
                s.save()
                
            return HttpResponseRedirect('/quiz/')
        
    return render(request,'signup.html',{'errors':errors,'email':request.POST.get('email',''),'firstname':request.POST.get('firstname',''),'lastname':request.POST.get('lastname','')})

def adminvalidate(request):
    errors={}
    msg=""
    if request.method=="POST":
        if not request.POST.get('adminemail',''):
           errors['adminemail']="Please enter a valid email"
        if len(errors)==0:
            if Question_Setter.objects.filter(email=request.POST.get('adminemail')):
                request.session['adminemail']=request.POST.get('adminemail')
                return HttpResponseRedirect('/quiz_creation/')
            else:
                msg="This Email id not authorized to set questions"                
    return render(request,'quiz_authenticate.html',{'errors':errors,'adminemail':request.POST.get('adminemail',''),'msg':msg})

def quizsuccess(request):
    errors={}
    msg=""
    if not request.session.get('adminemail',False):
        return HttpResponseRedirect('/quiz-authenticate/')
    if request.method=="POST":
        if not request.POST.get('formquestion',''):
           errors['quizform']="Please enter the question"
        if not request.POST.get('title',''):
           errors['title']="Please enter the apt title for the question"
        if not request.POST.get('option1',''):
           errors['option1']="None of the option can be blank"
        if not request.POST.get('option2',''):
           errors['option2']="None of the option can be blank"
        if not request.POST.get('option3',''):
           errors['option3']="None of the option can be blank"
        if not request.POST.get('option4',''):
           errors['option4']="None of the option can be blank"
        
        if len(errors)==0:
            title=request.POST.get('title')
            question=request.POST.get('formquestion')
            option1=request.POST.get('option1')
            option2=request.POST.get('option2')
            option3=request.POST.get('option3')
            option4=request.POST.get('option4')
            
            Question.objects.all().delete()
            q=Question(title=title,question=question,option1=option1,option2=option2,option3=option3,option4=option4)
            q.save()
            #delete vote column values of voters
            Voters.objects.all().update(vote='')
            quizmsg="Question is successfully saved"
            return render(request,'signup.html',{'quizmsg':quizmsg})
        
    return render(request,'quiz_creation.html',{'errors':errors,'title':request.POST.get('title',''),'quizform':request.POST.get('formquestion',''),'option1':request.POST.get('option1',''),'option2':request.POST.get('option2',''),'option3':request.POST.get('option3',''),'option4':request.POST.get('option4','')})


def quiz(request):
    
    if request.session.get('email',False):          #if email is presnet => user is registered but may have voted or maybe not
        if not request.session.get('hasvoted',False):   #user has registered but not voted        
            params={}
            q=Question.objects.filter(id='1')
            if len(q)==0:
                quesmsg="Currently there are no questions present to vote.."
                return render(request,'signup.html',{'quesmsg':quesmsg})
            else:
                params['question']=q[0].question
                params['option1']=q[0].option1
                params['option2']=q[0].option2
                params['option3']=q[0].option3
                params['option4']=q[0].option4

            return render(request,'quiz.html',{'params':params})
        else:    #user has registered and voted already, take him to home page
            return render(request,'signup.html',{'quizmsg':"Already voted"})
    else:
        quesmsg="Please signin to vote"
        return render(request,'signup.html',{'quesmsg':quesmsg})

def quessuccess(request):
    if request.session.get('email',False):  #user is still loggedin
        v=Voters.objects.get(email=request.session['email'])    
        if v.vote:  # already voted
            quesmsg=request.session['email']+"has already voted,Please logout and try with some other id"
            return render(request,'signup.html',{'quesmsg':quesmsg})
        else:
            #update the table with vote field
            v=Voters.objects.filter(email=request.session['email']).update(vote=request.POST.get('choices'))
            request.session['hasvoted']=True
            return render(request,'share.html')
            
    elif not request.session.get('email',False):   #user has signed out
        quesmsg="Please signin again to continue"
        return render(request,'signup.html',{'quesmsg':quesmsg})
    
def logout(request):
    try:
        del request.session['email'],request.session['hasvoted']
    except:
        pass
    return HttpResponseRedirect('/home/')

def quizcreation(request):
    if request.session.get('adminemail',False):
        return render(request,'quiz_creation.html')
    else:
        return HttpResponseRedirect('/quiz-authenticate/')


def quizauthenticate(request):   
    return render(request,'quiz_authenticate.html')