from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import *

app_name = 'school'

views_employee = SimpleRouter()
views_employee.register('', EmployeeView, basename='employee-router')

views_student = SimpleRouter()
views_student.register('', EstudentView, basename='student-router' )

views_school = SimpleRouter()
views_school.register('', SchoolView, basename='school-router' )

view_school_serie = SimpleRouter()
view_school_serie.register('', SchoolSerieView, basename='school-serie-ruter')

view_school_class = SimpleRouter()
view_school_class.register('', SchoolClassView, basename='school-class-ruter')

view_school_room = SimpleRouter()
view_school_room.register('', SchoolroomView, basename='school-room-ruter')

view_school_subjects = SimpleRouter()
view_school_subjects.register('', SchoolSubjectsView, basename='school-subjects-ruter')

view_class_room = SimpleRouter()
view_class_room.register('', ClassroomView, basename='class-room-ruter')

view_presence_in_class = SimpleRouter()
view_presence_in_class.register('', PresenceInClassView, basename='presence-in-class-ruter')

view_test_score = SimpleRouter()
view_test_score.register('', TestScoreView, basename='test-score-ruter')

urlpatterns = [
    path('employee', include(views_employee.urls)),
    path('student', include(views_student.urls)),
    path('school', include(views_school.urls)),
    path('school-serie', include(view_school_serie.urls)),
    path('school-class', include(view_school_class.urls)),
    path('school-room', include(view_class_room.urls)),
    path('school-subject', include(view_school_subjects.urls)),
    path('class-room', include(view_class_room.urls)),
    path('presence-in-class', include(view_presence_in_class.urls)),
    path('test-score', include(view_test_score.urls)),

]