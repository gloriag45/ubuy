from django.contrib import admin
from .models import *

class ToolInLine(admin.TabularInline):
    model =Tool
    extra = 1

class ExperienceInLine(admin.TabularInline):
    model =Experience
    extra = 1

class SuggestionInLine(admin.TabularInline):
    model =Suggestion  
    extra = 1

class  ChallengeInLine(admin.TabularInline):
    model = Challenge
    extra = 1

class  TaskImageInLine(admin.TabularInline):
    model = TaskImage
    extra = 1

class  SkillInLine(admin.TabularInline):
    model = Skill
    extra = 1



# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [ToolInLine,TaskImageInLine,SuggestionInLine,ExperienceInLine, ChallengeInLine,SkillInLine]
admin.site.register(Interns)
admin.site.register(Universities)
admin.site.register(InternshipDay)
# admin.site.register(Task)
# admin.site.register(Tool)
# admin.site.register(Challenge)
# admin.site.register(Experience)
# admin.site.register(Suggestion)
# admin.site.register(Skill)
# admin.site.register(TaskImage)
