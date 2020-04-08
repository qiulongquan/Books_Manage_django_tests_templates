from django.contrib import admin
from .models import Question
from .models import Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 按照自定义字段集显示效果
    # 这个自定义了question页面里面显示的字段集 field ，现在是显示2个项目'pub_date', 'question_text'
    # fieldsets = [
    #     (None, {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    # list显示效果
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 最基本显示效果
    # fields = ['question_text', 'pub_date']

    # 这个是question和choice创建关联的，不能删掉
    inlines = [ChoiceInLine]

    # 添加了一个“过滤器”侧边栏，允许人们以pub_date字段来过滤列表：
    list_filter = ['pub_date']
    # 添加一个搜索框 支持LIKE 模糊查找
    search_fields = ['question_text']
    # 每页显示的内容数量
    list_per_page = 2


admin.site.register(Question, QuestionAdmin)

