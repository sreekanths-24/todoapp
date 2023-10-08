from django import forms
from .models import Task

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']

    # Customize form fields as needed

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'})
    )

    description = forms.CharField(
        label='Description',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description'})
    )

    due_date = forms.DateTimeField(
        label='Due Date',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM'}),
        input_formats=['%Y-%m-%d %H:%M']
    )
