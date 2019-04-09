from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
# Create your views here.

from course.models import Course


class CourseListView(View):
    """课程列表"""
    @staticmethod
    def get(request):
        # 所有课程
        all_course = Course.objects.all()
        # 课程搜索功能
        keywords = request.GET.get('keywords', '')
        if keywords:
            all_course = all_course.filter(name__icontains=keywords)

        # 热门课程推荐
        hot_course = all_course.order_by('-click_nums')[:3]

        # 最热门
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'hot':
                all_course = all_course.order_by('-click_nums')
            elif sort == 'students':
                all_course = all_course.order_by('-fav_nums')

        # 分页
        page = request.GET.get('page', '')
        p = Paginator(all_course, 6)
        all_course = p.get_page(page)
        return render(request, 'course-list.html', {
            'all_course': all_course,
            'sort': sort,
            'hot_course': hot_course,
            'page': page,
        })


class CourseDetailView(View):
    """课程详情"""
    @staticmethod
    def get(request):
        return render(request, 'course-detail.html')