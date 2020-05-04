from django.contrib import admin

from first_app.models import Person
admin.site.register (Person)


from first_app.models import TypesOfDisaster
admin.site.register(TypesOfDisaster)

from first_app.models import Organization
admin.site.register(Organization)

from first_app.models import Blog
admin.site.register(Blog)




