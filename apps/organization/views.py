from django.shortcuts import render

# Create your views here.

from django.views.generic import View

class TeacherListView(View):
    """教师列表"""
    @staticmethod
    def get(request):
        return render(request, 'teachers-list.html')


class OrganizationList(View):
    """组织列表"""
    @staticmethod
    def get(request):
        return render(request, 'org-list.html')