from django.contrib import admin
from .models import Course, Content, Student, Instructor, Enrollment, Exam, Result, Message

admin.site.register(Course)
admin.site.register(Content)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Exam)
admin.site.register(Result)
admin.site.register(Message)