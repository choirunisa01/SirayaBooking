from django.db import models

# Create your models here.

class Book(models.Model):
    nama = models.CharField('Nama Lengkap',  max_length=60)
    alamat = models.CharField(max_length=300)
    noktp = models.CharField('Nomor KTP', max_length=20)
    tanggal = models.DateField('Tanggal Booking')

    LIST_JAM = (
        ('08.00 - 10.00', '08.00 - 10.00'),
        ('08.00 - 10.00', '10.00 - 12.00'),
        ('14.00 - 16.00', '14.00 - 16.00'),
        ('16.00 - 18.00', '16.00 - 18.00'),
    )

    jam = models.CharField(
        max_length = 100,
        choices = LIST_JAM, 
        default= '14.00 - 16.00'
    )

    def __str__(self):
        return self.nama
    