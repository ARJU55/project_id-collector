from django.contrib import admin
from django.http import HttpResponse
from .models import Course, Tech, Syllabus, ProjectDetails
from reportlab.pdfgen import canvas

admin.site.register(Course)
admin.site.register(Tech)
admin.site.register(Syllabus)
admin.site.register(ProjectDetails)

