from django.shortcuts import render

# Create your views here.

from django.views.generic import View


class CourseListView(View):
    """课程列表"""
    @staticmethod
    def get(request):
        return render(request, 'course-list.html')
