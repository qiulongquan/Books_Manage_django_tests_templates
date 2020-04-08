from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime
from polls.models import Question

# 测试test案例
# https://www.jetbrains.com/help/pycharm/2017.1/creating-and-running-your-first-django-project.html#d28041e21

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

        response = self.client.get(reverse('polls:question'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['question_list'], [])
