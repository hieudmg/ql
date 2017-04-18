# coding=utf-8
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.

class BacSi(models.Model):
    ten = models.CharField(max_length=10)
    nghiHuu = models.BooleanField(default=False)

    def __str__(self):
        return self.ten.encode('utf-8')


class ThongTin(models.Model):
    bs = models.ForeignKey(BacSi, on_delete=models.SET_NULL, null=True, blank=True)
    maSo = models.CharField(max_length=20, unique=True)
    tenVo = models.CharField(max_length=30)
    tenChong = models.CharField(max_length=30)
    nsVo = models.IntegerField(validators=[MaxValueValidator(2000), MinValueValidator(1950)])
    nsChong = models.IntegerField(validators=[MaxValueValidator(2000), MinValueValidator(1950)])
    lienHe = models.CharField(max_length=30, blank=True)
    hienTinhTrung = models.BooleanField(default=False)
    hienNoan = models.CharField(max_length=30, blank=True)


class Trung(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE, primary_key=True)
    tongSoTrung = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    GV = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    MI = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    truongThanh = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    vo = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    batThuong = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    thoaiHoa = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    nangNoan = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    thoaiHoaSauICSI = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    tongSoTrungICSI = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    tongSoTrungTT = models.IntegerField(validators=[MinValueValidator(0)], default=0)


class Phoi(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE, primary_key=True)
    loai1 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai2 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai3 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    tongSoPhoiTiepTucTheoDoi = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    tongSoPhoiChuyen = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    tongSoPhoiLuuTruLanh = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    tongSoPhoiHuy = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soPhoiN2 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soPhoiN3 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soPhoiN4 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soPhoiN5 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soCryotop2 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soCryotop3 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soCryotop4 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    soCryotop5 = models.IntegerField(validators=[MinValueValidator(0)], default=0)


class TinhDichDoNgayCH(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE, primary_key=True)
    matDo = models.FloatField(validators=[MinValueValidator(0)], default=0)
    doDiDong = models.FloatField(validators=[MinValueValidator(0)], default=0)
    hinhDang = models.FloatField(validators=[MinValueValidator(0)], default=0)


class TruPhoi(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE, primary_key=True)
    viTriTruPhoi = models.CharField(max_length=20, default='-------')
    label00 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label01 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label02 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label03 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label10 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label11 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label12 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label13 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label20 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label21 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label22 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    label23 = models.CharField(max_length=20, default='rgba(0, 0, 0, 0)')
    loai001 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai002 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai003 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai101 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai102 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai103 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai201 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai202 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai203 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    truPhoiToanBo = models.BooleanField(default=False)
    xinTrung = models.BooleanField(default=False)
    PICSI = models.BooleanField(default=False)
    truLanh = models.BooleanField(default=False)
    TESE = models.BooleanField(default=False)
    PESAMESA = models.BooleanField(default=False)


class KyThuatVien(models.Model):
    ten = models.CharField(max_length=20)
    nghiHuu = models.BooleanField(default=False)


class ChocHut(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE)
    HCG = models.DateTimeField(default=datetime.now, blank=True)
    gioCH = models.DateTimeField(default=datetime.now, blank=True)
    soNang = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    added = models.BooleanField(default=False)


class ChuyenPhoi(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE)
    soPhoiRa = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    ngayKiemTra = models.DateField(default=datetime.now, blank=True)
    ngayChuyenPhoi = models.DateField(default=datetime.now, blank=True)
    added = models.BooleanField(default=False)


class DongPhoi(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE)
    ngayDongPhoi = models.DateField(default=datetime.now, blank=True)
    ngayNopTien = models.DateField(default=datetime.now, blank=True)
    added = models.BooleanField(default=False)
