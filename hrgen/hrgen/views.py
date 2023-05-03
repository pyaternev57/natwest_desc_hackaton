from django.views import generic
from django.shortcuts import render, get_object_or_404
from django import forms
from django.contrib import messages

from hrgen.openai_utils import generate_description, generate_questions, generate_summary
from hrgen.models import Position, Description, Resume, resume_sample



def get_position(job_title, yoe, required_skills):
    position = Position.objects.filter(
        job_title=job_title, yoe=yoe, skills=required_skills
    )
    if not position.exists():
        position = Position.objects.create(
             job_title=job_title, yoe=yoe, skills=required_skills
        )
    else:
        position = position.first()
    return position

class IndexView(generic.View):
    def get(self, request):
        return render(request,"index.html")
    

class SkillForm(forms.Form):
    job_title = forms.CharField()
    yoe = forms.IntegerField()
    required_skills = forms.CharField()


class CreateDescView(generic.View):
    def get(self, request):
        form = SkillForm()
        return render(request, "create_description.html", {"form": form, "text": ""})
    
    def post(self, request):
        form = SkillForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            text = generate_description(
                data["job_title"], data["required_skills"], data["yoe"]
            )
            position = get_position(data["job_title"], data["yoe"], data["required_skills"])
            Description.objects.create(position=position, text=text)
            return render(request, "create_description.html", {"form": form, "text": text})
        else:
            messages.add_message("Error while validating form")
            return render(request, "create_description.html", {"form": form, "text": ""})
        

# class PositionsView(generic.ListView):
#     def get(self, request):


class PositionsView(generic.ListView):
    model = Position
    paginate_by = 10
    template_name = "positions.html"


class PositionView(generic.DetailView):
    model = Position
    paginate_by = 10
    template_name = "position.html"
    context_object_name = "position"


class InterviewSelectView(generic.ListView):
    model = Position
    paginate_by = 10
    template_name = "interview.html"


class InterviewView(generic.View):
    def get(self, request, position_id):
        position = get_object_or_404(Position, pk=position_id)
        text = generate_questions(position.descriptions.first().text)
        return render(request, "questions.html", {"text": text, "position": position})
    
class ResumeForm(forms.Form):
    resume_text = forms.CharField(widget=forms.Textarea)


class SummaryView(generic.View):
    def get(self, request):
        form = ResumeForm()
        text = generate_summary(
                resume_sample
            )
        return render(request, "create_summary.html", {"form": form, "text": text})
    
    def post(self, request):
        form = ResumeForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            text = generate_summary(
                data["resume_text"]
            )
            Resume.objects.create(
                text=data["resume_text"], summary=text
            )
            return render(request, "create_summary.html", {"form": form, "text": text})
        else:
            messages.add_message("Error while validating form")
            return render(request, "create_summary.html", {"form": form, "text": ""})
        

class ResumesView(generic.ListView):
    model = Resume
    paginate_by = 10
    template_name = "positions.html"