from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "role",
            "description",
            "tech_stack",
            "image_url",
        ]

        labels = {
            "title": "Project Name",
            "role": "Role in Project",
            "description": "Project Description",
            "tech_stack": "Technologies Used",
            "image_url": "Project Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "role": TextInput(
                attrs={
                    "placeholder": "Backend, Frontend",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your project",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }