from django.shortcuts import get_object_or_404, render
from .models import About, Category, Project, ProjectSkill, Recommendation, Skill, Social

def index(request):
    about = About.objects.get(id=1)
    recommendations = Recommendation.objects.all().order_by('title')
    categories = Category.objects.all().order_by('name')
    skills = Skill.objects.all()
    socials = Social.objects.filter(display=True)
    projects = Project.objects.all().order_by('-id')

    context = {
        'about': about,
        'categories': categories,
        'projects': projects,
        'skills': skills,
        'socials': socials,
        'recommendations': recommendations,
    }
    return render(request, 'pages/index.html', context)

def project(request, project_slug):
    about = About.objects.get(id=1)
    project = get_object_or_404(Project, slug=project_slug)
    project_skills = project.projectskill_set.all()
    socials = Social.objects.filter(display=True)

    
    context = {
        'about': about,
        'project': project,
        'project_skills': project_skills,
        'socials': socials,
    }
    return render(request, 'pages/project.html', context)