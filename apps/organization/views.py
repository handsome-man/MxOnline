from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
# Create your views here.

from organization.models import CityDict, CourseOrg, Teacher


class TeacherListView(View):
    """教师列表"""
    @staticmethod
    def get(request):
        # 所有的老师
        all_teacher = Teacher.objects.all()

        # 搜索框搜索内容
        keywords = request.GET.get('keywords', '')
        if keywords:
            # i忽略大小写
            all_teacher = all_teacher.filter(name__icontains=keywords)

        # 讲师排行榜
        hot_teacher = all_teacher.order_by('-work_years')[:2]

        # 人气
        sort = request.GET.get('sort', '')
        if sort:
            all_teacher = all_teacher.order_by('-click_nums')

        # 共多少人
        teacher_count = all_teacher.count()

        return render(request, 'teachers-list.html', {
            'all_teacher': all_teacher,
            'sort': sort,
            'hot_teacher': hot_teacher,
            'teacher_count': teacher_count,
        })


class OrganizationListView(View):
    """机构列表"""

    @staticmethod
    def get(request):
        all_city = CityDict.objects.all()
        all_course_org = CourseOrg.objects.all()

        # 搜索框搜索内容
        keywords = request.GET.get('keywords', '')
        if keywords:
            all_course_org = all_course_org.filter(Q(name__icontains=keywords) | Q(desc__icontains=keywords))

        # 机构类型
        ct = request.GET.get('ct', '')
        if ct:
            all_course_org = all_course_org.filter(category=ct)

        # 所在地区
        city_id = request.GET.get('city', '')
        if city_id:
            all_course_org = all_course_org.filter(city=int(city_id))

        # 授课机构排名
        hot_orgs = all_course_org.order_by('-click_nums')[:5]

        # 热度
        sort = request.GET.get('sort', '')
        if sort:
            # 学习人数
            if sort == 'students':
                all_course_org = all_course_org.order_by('-students')
            # 课程数
            elif sort == 'courses':
                all_course_org = all_course_org.order_by('-course_nums')

        # 共多少家
        org_nums = all_course_org.count()

        return render(request, 'org-list.html', {
            'all_city': all_city,
            'hot_orgs': hot_orgs,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': ct,
            'sort': sort,
            'all_course_org': all_course_org,
        })


class OrganizationIndexView(View):
    """机构首页"""

    @staticmethod
    def get(request):
        return render(request, 'org-detail-homepage.html')
