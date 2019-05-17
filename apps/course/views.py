from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
# Create your views here.

from course.models import Course
from organization.models import CourseOrg


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
    def get(request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数 访问一次增加1
        course.click_nums += 1
        course.save()
        # 课程标签相同的即位相关课程
        tag = course.tag
        relate_course = Course.objects.exclude(id=int(course_id))
        relate_course = relate_course.filter(tag=tag)[1:2]
        return render(request, 'course-detail.html',
                      {
                          'course': course,
                          'relate_course': relate_course
                       })