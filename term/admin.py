from django.contrib import admin

from term.models import Term, Category, Suggestion

admin.site.register(Term)
admin.site.register(Category)
admin.site.register(Suggestion)
