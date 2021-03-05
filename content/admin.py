from django.contrib import admin
from django.contrib.admin.options import get_content_type_for_model
from .models import About, Category, Project, ProjectSkill, Recommendation, Skill, Social

class RecommendationInline(admin.StackedInline):
    model = Recommendation

class CategoryAdmin(admin.ModelAdmin):
    inlines = [RecommendationInline,]

class ProjectSkillInLine(admin.StackedInline):
    model = ProjectSkill

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectSkillInLine,] 
    list_display = ['id', 'title']   


admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Social)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)