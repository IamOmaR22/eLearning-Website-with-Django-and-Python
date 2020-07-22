from django import template
from django.utils.safestring import mark_safe
from courses.models import Course
import markdown

register = template.Library()

@register.simple_tag
def newest_course():
    ''' Gets the most recent course that was added to the library. '''
    return Course.objects.latest('created_at')
# register.simple_tag('newest_course')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    ''' Return dictionary of courses to display as navigation pane '''
    courses = Course.objects.all()
    return {'courses':courses}
# register.inclusion_tag('courses/course_nav.html')(nav_courses_list)

@register.filter('time_estimate')
def time_estimate(word_count):
    ''' Estimate the number of minutes it will take to complete a step based
    on the passed-in wordcount. '''
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    ''' Converts markdown text to HTML '''
    html_body = markdown.markdown(markdown_text)
    return mark_safe(html_body)