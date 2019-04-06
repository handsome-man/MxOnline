from django.shortcuts import render

# Create your views here.

from django.views.generic import View


class CourseListView(View):
    """课程列表"""
    @staticmethod
    def get(request):
        return render(request, 'course-list.html')


class CourseDetailView(View):
    """课程详情"""
    @staticmethod
    def get(request):
        return render(request, 'course-detail.html')