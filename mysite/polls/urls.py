# polls/urls.py
from django.urls import path
from . import questions
from . import choice

#添加这行 命名空间
app_name = 'polls'

urlpatterns = [
    path('question/', questions.question, name='question'),
    path('detail/<int:question_id>', questions.detail, name='detail'),
    path('results/<int:question_id>', questions.results, name='results'),
    path('<int:question_id>/vote/', questions.vote, name='vote'),
    path('addQuestion/', questions.addQuestion, name='addQuestion'),
    path('choice/', questions.choice, name='choice'),
    path('replyQuestion/<int:question_id>', questions.replyQuestion, name='replyQuestion'),
    path('delQuestion/<int:question_id>', questions.delQuestion, name='delQuestion'),
]