from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField


class About(models.Model):
    name = models.CharField(max_length=100)
    about = RichTextField()
    email = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return 'About Me'


class Social(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    icon = models.FileField(upload_to='icons/', blank=True)
    display = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Social'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    display = models.BooleanField(default=False)
    icon = models.FileField(upload_to='icons/', blank=True)

    def __str__(self):
        return self.name

    pass


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    name = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = RichTextField()
    main_image = models.ImageField(upload_to='images/', blank=True)
    alt_text_main = models.CharField(max_length=200, blank=True)
    screenshot1 = models.ImageField(upload_to='images/', blank=True)
    caption1 = models.CharField(max_length=100, blank=True)
    alt_text1 = models.CharField(max_length=200, blank=True)
    screenshot2 = models.ImageField(upload_to='images/', blank=True)
    caption2 = models.CharField(max_length=100, blank=True)
    alt_text2 = models.CharField(max_length=200, blank=True)
    screenshot3 = models.ImageField(upload_to='images/', blank=True)
    caption3 = models.CharField(max_length=100, blank=True)
    alt_text3 = models.CharField(max_length=200, blank=True)
    screenshot4 = models.ImageField(upload_to='images/', blank=True)
    caption4 = models.CharField(max_length=100, blank=True)
    alt_text4 = models.CharField(max_length=200, blank=True)
    project_url = models.CharField(max_length=200, blank=True)
    code_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title



class ProjectSkill(models.Model):
    title = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name
