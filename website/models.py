from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita/')
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = "Berita"

class Dosen(models.Model):
    nama = models.CharField(max_length=100)
    nidn = models.CharField(max_length=20, null=True, blank=True) 
    jabatan = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='dosen/')
    
    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Dosen"
    

class Akademik(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short = models.CharField(max_length=255, blank=True)
    full = models.TextField(blank=True)
    image = models.ImageField(upload_to='akademik/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Akademik'
    
    