from django.contrib import admin
from . models import candidate, skills, project
# Register your models here.
admin.site.register(candidate)
admin.site.register(skills)
admin.site.register(project)

