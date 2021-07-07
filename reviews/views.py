from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.
# def review(request) :

#     if request.method == 'POST':
#       form  = ReviewForm(request.POST)
#       if form.is_valid():
#            form.save()
#            return HttpResponseRedirect("/welcome")
#     else:
#         form = ReviewForm()
#     return render(request , "reviews/review.html" , {
#         "form" : form
#     }) 


# before we were using View class for displaying and saving form data to database
# but now we are using FormView with less configuration the View and it handles
# the get request

## Another beautiful approach is using CreateView
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/welcome"

    # we don't need this piece of code while using CreateView but need it when using FormView
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # we don't need this code in FormView and CreatView but we need it while using the View
    # def get(self,request):
    #      form = ReviewForm()
    #      return render(request , "reviews/review.html" , {
    #     "form" : form
    # }) 
    # def post(self , request):
    #     form  = ReviewForm(request.POST)
    #     if form.is_valid():
    #        form.save()
    #        return HttpResponseRedirect("/welcome")


    #     return render(request , "reviews/review.html" , {
    #     "form" : form
    # }) 



class WelcomeView(TemplateView):
    template_name = "reviews/welcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This is a message from the view class"
        return context

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query =  super().get_queryset()
    #     data = base_query.filter(rating__gt = 4)
    #     return data
        
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


    # in the html page we can access the by lowercase of the Model e.g: review

# don't store complex things inside the session like: objects
# instead store simple data like strings,id,boolean etc
class AddFavoriteView(View):
    def post(self , request):
        review_id = request.POST['review_id']
        # fav_review = Review.objects.get(pk=review_id)
        # request.session["favorite_review"] = fav_review
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/"+review_id)
