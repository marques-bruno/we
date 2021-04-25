# from allauth.account.views import SignupView
# .forms import SignupForm


# class ProfileSignupView(SignupView):

#     success_url = ''  # profile specific success url
#     form_class = SignupForm
#     profile_class = None  # profile class goes here

#     def form_valid(self, form):
#         response = super(ProfileSignupView, self).form_valid(form)
#         profile = self.profile_class(user=self.user)
#         profile.save()
        
#         return response