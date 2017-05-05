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
    ngayNhap = models.DateField(default=datetime.now, blank=True)


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

    loai011 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai012 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai013 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai021 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai022 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai023 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai031 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai032 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai033 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai111 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai112 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai113 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai121 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai122 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai123 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai131 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai132 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai133 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai211 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai212 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai213 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai221 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai222 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai223 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai231 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai232 = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    loai233 = models.IntegerField(validators=[MinValueValidator(0)], default=0)

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
    stt = models.IntegerField(default=0)
    HCG = models.DateTimeField(default=datetime.now, blank=True)
    gioCH = models.DateTimeField(default=datetime.now, blank=True)
    soNang = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    added = models.BooleanField(default=False)


class ChuyenPhoi(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE)
    soPhoiRa = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    ngayKiemTra = models.DateField(default=datetime.now, blank=True)
    ngayChuyenPhoi = models.DateField(default=datetime.now, blank=True)
    ngayRaPhoi = models.DateField(default=datetime.now, blank=True)
    added = models.BooleanField(default=False)
    timeAdd = models.DateTimeField(default=datetime.now, blank=True)


class DongPhoi(models.Model):
    tt = models.OneToOneField(ThongTin, on_delete=models.CASCADE)
    ngayDongPhoi = models.DateField(default=datetime.now, blank=True)
    ngayNopTien = models.DateField(default=datetime.now, blank=True)
    added = models.BooleanField(default=False)


class ThongKe(models.Model):
    thang = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    nam = models.IntegerField(validators=[MinValueValidator(2017)], default=datetime.now().year)
    tongSoTreSinh = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    tongSoTuiThai = models.IntegerField(validators=[MinValueValidator(0)], default=0)
