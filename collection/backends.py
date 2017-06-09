from registration.backends.simple.views import RegistrationView

# subclassing RegistrationView to use the template we created

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        # goes to url corresponding to create_thing.html template
        return('registration_create_thing')
