from django.contrib import admin
from .models import Berita, Dosen, Akademik

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
	list_display = ('judul', 'tanggal')


@admin.register(Dosen)
class DosenAdmin(admin.ModelAdmin):
	list_display = ('nama', 'jabatan')


@admin.register(Akademik)
class AkademikAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',)}