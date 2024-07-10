from django.contrib import admin
from .models import AboutSection, LinksSection, LearningSection, InstructionsSection

for form in [AboutSection, LinksSection, LearningSection, InstructionsSection]:
    admin.site.register(form)

