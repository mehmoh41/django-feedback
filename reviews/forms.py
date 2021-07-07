from django import forms
from django.forms import fields
from .models import Review
# class ReviewForm(forms.Form) :
#     user_name = forms.CharField(max_length=40, label="Your Name" , error_messages={
#         "required" : "Your name must not be empty!s",
#         "max_length" : "Please enter shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback" , widget=forms.Textarea , max_length=200)
#     rating = forms.IntegerField(label="Your Rating" , min_value=1 , max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name" : "Your Name",
            "review_text": "Your Feedback",
            "rating" : "Your Rating"
        }
        # exclude = ['user_name']
        error_messages = {
            "user_name" : {
                "required" : "Your Name is required!",
                "max_length": "Please Enter a shorter name!"
            },
            "review_text" : {
                "required" : "Review text field is required!",
                "max_length": "Please Enter a shorter review!"
            },
            "rating" : {
                "required" : "Rating field is required!",
                "max_length": "Please Enter a shorter number"
            }

        }