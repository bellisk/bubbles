from django.contrib import admin
from bubbles.bubblesapp.models import *

class ContactI(admin.TabularInline):
    model = Contact

class ProfileMA(admin.ModelAdmin):
    inlines = [ContactI]

admin.site.register(Profile, ProfileMA)
admin.site.register(Contact)


