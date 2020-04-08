# mysite/polls/questions.py
from django.shortcuts import render, resolve_url, get_object_or_404
from .models import Question
from django.http import Http404
from .models import Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def detail(request, question_id):
    print("qiulongquan_question_id={}".format(question_id))
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        # 可以抛出一个raise也可以跳转到error页面
        # raise Http404("Question does not exist.")
        return render(request, 'polls/error.html')
    # django默认会返回一个带字典对象的HttpResponse对象，render 渲染 html文件的字典带着然后作为HttpResponse对象返回
    return render(request, 'polls/detail.html', {'question': question})


# 下面的这种写法也可以的，如果找不到就返回http404错误
# def detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     # django默认会返回一个带字典对象的HttpResponse对象，render 渲染 html文件的字典带着然后作为HttpResponse对象返回
#     return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    # django默认会返回一个带字典对象的HttpResponse对象，render 渲染 html文件的字典带着然后作为HttpResponse对象返回
    return render(request, 'polls/results.html', context)


def question(request):
    print("qiulongquan_question_strat")
    question_list = Question.objects.order_by('-pub_date')[:]
    context = {'question_list': question_list}
    # django默认会返回一个带字典对象的HttpResponse对象，render 渲染 html文件的字典带着然后作为HttpResponse对象返回
    return render(request, 'polls/question.html', context)


def replyQuestion(request, question_id):
    questionID = question_id
    # print("qiulongquan_questionID={}".format(questionID))
    # 只返回一条记录的时候用get，返回结果可以直接读取不需要for
    question_info = Question.objects.get(id=questionID)
    # 返回多条或者一条记录的时候用filter，但是返回结果要用for循环来读取
    choice_info = Choice.objects.filter(question_id=questionID)
    # print("qiulongquan_question_info={},{}".format(question_info.question_text, question_info.pub_date))
    context = {'question_info': question_info, 'choice_info': choice_info}
    return render(request, 'polls/choice.html', context)


def delQuestion(request, question_id):
    questionID = question_id
    Question.objects.filter(id=questionID).delete()
    # 重定向
    return HttpResponseRedirect(reverse('polls:question'))


def addQuestion(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']

    from django.utils import timezone
    temp_question = Question(question_text=question_text, pub_date=timezone.now())
    temp_question.save()

    #重定向redirect
    return HttpResponseRedirect(reverse('polls:question'))


def choice(request):
    if request.method == 'POST':
        question_id = request.POST['question_id']
        # print("qiulongquan_question_id={}".format(question_id))
        checkbox_status = request.POST.getlist('tags')
        # print("qiulongquan_checkbox_status={}".format(checkbox_status))
        temp_choice = Choice(choice_text=request.POST['choice_text'], attitude=checkbox_status, question_id=request.POST['question_id'])
        temp_choice.save()

    #重定向redirect
    url = resolve_url('polls:replyQuestion', question_id)
    return HttpResponseRedirect(url)
