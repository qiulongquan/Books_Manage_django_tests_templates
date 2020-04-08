from django.db import models


class Hello(models.Model):
    your_name = models.CharField(max_length=15)

    def __str__(self):
        return "<{0}>".format(self.your_name)

    def was_equal(self):
        a = Hello.objects.get(pk=1)
        print("qiulongquan_a={}".format(a.your_name))
        return a.your_name == "kenji"


class Qiu(models.Model):
    qiu_name = models.CharField(max_length=15)

    def __str__(self):
        return self.qiu_name


class Hello1(models.Model):
    qiu_name1 = models.CharField(max_length=20)

    def __str__(self):
        return "<{0}>".format(self.qiu_name1)
