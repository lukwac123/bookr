from django.contrib import admin

class BookrAdmin(admin.AdminSite):
    site_header = "Administracja witryną Bookr"
    logout_template = 'admin/logout.html'
