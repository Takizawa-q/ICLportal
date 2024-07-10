from django.shortcuts import render
from django.http import HttpResponse
from .models import AboutSection, InstructionsSection, LinksSection, LearningSection
def index(request):
    abouts = AboutSection.objects.all()
    learnings = LearningSection.objects.all()
    links = LinksSection.objects.all()
    instructions = InstructionsSection.objects.all()
    
    return render(request, 'iclmenu/index.html',
                  {"abouts": abouts,
                   "learnings": learnings,
                   "links": links,
                   "instructions": instructions})