from hello.models import Hello
from django.test import TestCase
from django.urls import reverse


class BookTests(TestCase):
    def test_was_equal(self):
        # print("qiulongquan_hello={}".format(Hello.was_equal(Hello)))
        # self.assertIs(Hello.was_equal(self), True)

        response = self.client.get(reverse('polls:question'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['question_list'], [])
