from django.contrib import admin

from first_app.models import Person
admin.site.register (Person)


from first_app.models import TypesOfDisaster
admin.site.register(TypesOfDisaster)

from first_app.models import Organization
admin.site.register(Organization)

from first_app.models import Blog
admin.site.register(Blog)

from first_app.models import ContactUs
admin.site.register(ContactUs)

from first_app.models import Register
admin.site.register(Register)

from first_app.models import Review
admin.site.register(Review)

from first_app.models import HelpSupport
admin.site.register(HelpSupport)

from first_app.models import Notify
admin.site.register(Notify)

from first_app.models import Subscribe
admin.site.register(Subscribe)

