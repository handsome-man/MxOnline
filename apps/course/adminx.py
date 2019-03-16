# -*- coding: utf-8 -*-
__author__ = 'kevin'
__date__ = '2019/3/16 13:46'

import xadmin

from .models import Course, BannerCourse, Lesson, Video, CourseResource


class CourseAdmin(object):
    '课程'

    list_display = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'tag', 'is_banner', 'add_time', 'course_org', 'category', 'teacher', 'youneed_know', 'teacher_tell']
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'tag', 'is_banner', 'course_org', 'category', 'teacher', 'youneed_know', 'teacher_tell']
    list_filter = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'tag', 'is_banner', 'add_time', 'course_org', 'category', 'teacher', 'youneed_know', 'teacher_tell']


class BannerCourseAdmin(object):
    '''轮播课程'''

    list_display = [ 'name','desc','degree','learn_times','students']
    search_fields = ['name', 'desc', 'degree', 'students']
    list_filter = [ 'name','desc','degree','learn_times','students']


class LessonAdmin(object):
    '''章节'''

    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    #这里course__name是根据课程名称过滤
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    '''视频'''

    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    '''课程资源'''

    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)