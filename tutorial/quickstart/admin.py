from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin

from .models import UserProfile, Category, BoardGame, Order, OrderItem, Review


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'custom_method',)
    list_filter = ('user__is_active',)
    date_hierarchy = 'user__date_joined'
    search_fields = ('user__username', 'user__email')

    def custom_method(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    custom_method.short_description = 'Full Name'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

    @admin.display(description="boardgame__count")
    def category_post_count(self, obj):
        return obj.post_set.count()


@admin.register(BoardGame)
class BoardGameAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('title', 'price', 'category_name', 'image',)
    list_filter = ('category',)
    search_fields = ('title',)
    raw_id_fields = ('category',)

    @admin.display(description="category__name")
    def category_name(self, obj):
        return obj.category.name

    # @admin.display(description='Image')
    # def image_thumbnail(self, obj):
    #     return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')


class OrderInLine(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_ordered', 'complete',)
    list_filter = ('complete',)
    date_hierarchy = 'date_ordered'
    # filter_horizontal = ('items',)
    raw_id_fields = ('user',)
    readonly_fields = ('date_ordered',)
    inlines = (OrderInLine,)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('board_game', 'board_game__title', 'user', 'rating', 'created_at',)
    raw_id_fields = ('board_game', 'user')
    list_filter = ('rating',)
    date_hierarchy = 'created_at'
    search_fields = ('board_game__title', 'user__username')

    @admin.display(description="board_game__title")
    def board_game__title(self, obj):
        return obj.board_game.title


# Register your models here.
