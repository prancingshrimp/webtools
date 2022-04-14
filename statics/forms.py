from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.lookups import PostgresOperatorLookup

from statics.models import UserProfile, Static8FModel, Static6FModel

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )



class Static8FForm(forms.ModelForm):

    LGesamt = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    LSammler = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    Fabstand1 = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    Fabstand2 = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    Fabstand3 = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    mLeer = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'kg',
            'type': 'number',
        }
    ))

    mSammler = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'kg',
            'type': 'number',
        }
    ))

    VRohr = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'l',
            'type': 'number',
        }
    ))

    class Meta:
        model = Static8FModel
        # fields = '__all__'
        # fields = ('post',)
        fields = ('LGesamt', 'LSammler', 'Fabstand1', 'Fabstand2', 'Fabstand3', 'mLeer', 'mSammler', 'VRohr',)



class Static6FForm(forms.ModelForm):

    LGesamt = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    LSammler = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    Fabstand1 = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    Fabstand2 = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'mm',
            'type': 'number',
        }
    ))

    mLeer = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'kg',
            'type': 'number',
        }
    ))

    mSammler = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'kg',
            'type': 'number',
        }
    ))

    VRohr = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'l',
            'type': 'number',
        }
    ))

    class Meta:
        model = Static6FModel
        fields = ('LGesamt', 'LSammler', 'Fabstand1', 'Fabstand2', 'mLeer', 'mSammler', 'VRohr',)
