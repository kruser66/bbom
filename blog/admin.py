from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from blog.models import User, Post
from blog.forms import UserCreationForm, UserChangeForm


class InlinePostAdmin(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ['name', 'email', 'is_admin']
    list_filter = ['is_admin']

    fieldsets = [
        (None, {"fields": ['name', "email", "password", 'is_admin']}),
    ]

    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email', 'password1', 'password2'],
            },
        ),
    ]
    search_fields = ['email']
    ordering = ['email']
    inlines = [InlinePostAdmin]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'body']

    list_filter = ['user__email']