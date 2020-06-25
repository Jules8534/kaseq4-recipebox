from django import forms
from apprecipebox.models import Author, Recipe


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(widget=forms.Textarea)
    timeRequired = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)


class AddRecipeFormStaff(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    timeRequired = forms.CharField(max_length=30)
    instructions = forms.CharField(widget=forms.Textarea)

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'instructions')


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=150)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
