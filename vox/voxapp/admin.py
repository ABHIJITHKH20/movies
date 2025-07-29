# from django.contrib import admin
# from .models import vox, Booking

# @admin.register(vox)
# class VoxAdmin(admin.ModelAdmin):
#     list_display = ('title', 'genre', 'language', 'release_date')

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('movie',  'seats', 'tickets', 'price_per_ticket', 'total_price_display', 'booking_time')
#     search_fields = ('movie__title',  'seats')

#     def username(self, obj):
#         return obj.user.username if obj.user else '-'
#     username.short_description = 'Username'

#     def total_price_display(self, obj):
#         return obj.total_price
#     total_price_display.short_description = 'Total Price'










from django.contrib import admin
from .models import vox, Booking

@admin.register(vox)
class VoxAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'release_date')
    search_fields = ('title', 'genre', 'language')
    list_filter = ('genre', 'language', 'release_date')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'username', 'seats', 'tickets', 'price_per_ticket', 'total_price_display', 'booking_time')
    search_fields = ('movie__title', 'user__username', 'seats')
    list_filter = ('booking_time',)

    def username(self, obj):
        return obj.user.username if obj.user else '-'
    username.short_description = 'Username'

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = 'Total Price'
