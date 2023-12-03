from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from demoapp.forms import Loginform, Userloginform, QuestionForm
from demoapp.models import Question


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form = Loginform()
    form1 = Userloginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        form1 = Userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            tcr = form1.save(commit=False)
            tcr.user = user
            tcr.save()
            return redirect('loginview')
    return render(request,'registration.html',{'form':form,'form1':form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminhome')

        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')

        else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

def userhome(request):
    return render(request,'user/userhome.html')

def adminhome(request):
    return render(request,'admin/adminhome.html')

# QUESTION

def add_questions(request):
    form = QuestionForm()
    u = request.user
    if request.method == 'POST':
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('question_view_admin')
    return render(request,'admin/add_question.html',{'form':form})

# Teacher View Questions

def question_view_admin(request):
    u = request.user
    data = Question.objects.all()
    return render(request, 'admin/view_question.html', {'data': data})

def delete_question(request,id):
    qustn = Question.objects.get(id=id)
    qustn.delete()
    return redirect('question_view_admin')


def test(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.Ans)
            print()
            if q.Ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100

        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total

        }
        # return redirect(student)
        return render(request,'user/exam_result.html',context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions
        }

        return render(request,'user/exam.html',context)

