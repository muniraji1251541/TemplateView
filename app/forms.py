from django import forms

course=(('Python','Python'),('Java','Java'),('Mern','Mern'))
gender=(('male','male'),('female','female'))
lang=(('English','english'),('Tamil','tamil'),('Telugu','telugu'))

class Profile(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField(min_value=20)
    course=forms.ChoiceField(choices=(course))
    gender=forms.ChoiceField(choices=gender,widget=forms.RadioSelect)
    language=forms.MultipleChoiceField(choices=lang,widget=forms.CheckboxSelectMultiple)
