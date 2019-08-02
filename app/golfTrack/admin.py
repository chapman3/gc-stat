from django.contrib import admin
from .models import Hole, Course, Scores, Round, Scorecard
# Register your models here.
admin.site.register(Hole)
admin.site.register(Course)
admin.site.register(Scores)
admin.site.register(Round)
admin.site.register(Scorecard)