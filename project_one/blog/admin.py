
# blog/admin.py
from django.contrib import admin
from .models import Post, Profile, Company, Affiliater, Employee


admin.site.register(Post)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Company)

admin.site.register(Affiliater)

admin.site.register(Employee)