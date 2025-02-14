from django import forms
from .models import Meep, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(
        label="Profile Picture",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )

    profile_image_v2 = forms.ImageField(
        label="Profile Picture V2",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text="Upload a profile picture",
    )

    profile_bio = forms.CharField(
        label="",
        max_length=500,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Profile Bio"}
        ),
    )
    homepage_link = forms.CharField(
        label="",
        max_length=500,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Website Link"}
        ),
    )
    facebook_link = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Facebook link"}
        ),
    )
    instagram_link = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Instagram link"}
        ),
    )
    linkedin_link = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Linkedin link"}
        ),
    )

    class Meta:
        model = Profile
        fields = (
            "profile_image",
            "profile_image_v2",
            "profile_bio",
            "homepage_link",
            "facebook_link",
            "instagram_link",
            "linkedin_link",
        )


class MeepForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter Your Twitt",
                "class": "form-control",
            },
        ),
        label="",
    )
    meep_image = forms.ImageField(
        label="Meep image:",
        required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}),
        help_text="Upload a profile picture",
    )

    class Meta:
        model = Meep
        exclude = ("user", "likes")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["username"].label = ""
        self.fields["username"].help_text = ""

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = ""

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = ""


class UpdateForm(SignUpForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
