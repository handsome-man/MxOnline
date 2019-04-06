from django.shortcuts import render

# Create your views here.

from django.views.generic import View

class TeacherListView(View):
    """教师列表"""
    @staticmethod
    def get(request):
        return render(request, 'teachers-list.html')


class OrganizationListView(View):
    """机构列表"""
    @staticmethod
    def get(request):
        return render(request, 'org-list.html')


class OrganizationIndexView(View):
    """机构首页"""
    @staticmethod
    def get(request):
        return render(request, 'org-detail-homepage.html')