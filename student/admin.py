from django.contrib import admin
from student.models import Candidate
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Candidate._meta.fields]
admin.site.register(Candidate, CandidateAdmin)
