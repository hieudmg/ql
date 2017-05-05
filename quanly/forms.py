# coding=utf-8
from django import forms
from django.forms import DateTimeField
from .models import ThongTin, Trung, Phoi, TruPhoi, TinhDichDoNgayCH, BacSi, KyThuatVien, ChocHut, ChuyenPhoi, DongPhoi
from django.utils.translation import activate
from django.core.validators import MaxValueValidator, MinValueValidator

activate('vi')


class FormTT(forms.ModelForm):
    class Meta:
        model = ThongTin
        fields = ('maSo',
                  'tenVo',
                  'nsVo',
                  'tenChong',
                  'nsChong',
                  'lienHe',
                  'bs',
                  'hienTinhTrung',
                  'hienNoan',
                  'ngayNhap'
                  )


class FormTR(forms.ModelForm):
    class Meta:
        model = Trung
        fields = ('GV',
                  'MI',
                  'tongSoTrung',
                  'truongThanh',
                  'vo',
                  'batThuong',
                  'thoaiHoa',
                  'nangNoan',
                  'thoaiHoaSauICSI',
                  'tongSoTrungTT',
                  'tongSoTrungICSI',
                  )


class FormP(forms.ModelForm):
    class Meta:
        model = Phoi
        fields = ('loai1',
                  'loai2',
                  'loai3',
                  'tongSoPhoiTiepTucTheoDoi',
                  'tongSoPhoiLuuTruLanh',
                  'tongSoPhoiHuy',
                  'soCryotop2',
                  'soCryotop3',
                  'soCryotop4',
                  'soCryotop5',
                  'soPhoiN2',
                  'soPhoiN3',
                  'soPhoiN4',
                  'soPhoiN5',
                  'tongSoPhoiChuyen',
                  )


class FormTP(forms.ModelForm):
    class Meta:
        model = TruPhoi
        fields = ('viTriTruPhoi',
                  'label00',
                  'label01',
                  'label02',
                  'label03',
                  'label10',
                  'label11',
                  'label12',
                  'label13',
                  'label20',
                  'label21',
                  'label22',
                  'label23',
                  # --------------------
                  'loai011',
                  'loai012',
                  'loai013',
                  'loai111',
                  'loai112',
                  'loai113',
                  'loai211',
                  'loai212',
                  'loai213',

                  'loai021',
                  'loai022',
                  'loai023',
                  'loai121',
                  'loai122',
                  'loai123',
                  'loai221',
                  'loai222',
                  'loai223',

                  'loai031',
                  'loai032',
                  'loai033',
                  'loai131',
                  'loai132',
                  'loai133',
                  'loai231',
                  'loai232',
                  'loai233',
                  # ----------------------
                  'PESAMESA',
                  'PICSI',
                  'TESE',
                  'truLanh',
                  'truPhoiToanBo',
                  'xinTrung',
                  )


class FormTD(forms.ModelForm):
    class Meta:
        model = TinhDichDoNgayCH
        fields = ('doDiDong',
                  'hinhDang',
                  'matDo',
                  )


class FormBS(forms.ModelForm):
    class Meta:
        model = BacSi
        fields = ('ten',
                  'nghiHuu',
                  )


class FormKTV(forms.ModelForm):
    class Meta:
        model = KyThuatVien
        fields = ('ten',
                  'nghiHuu',
                  )


class FormCH(forms.ModelForm):
    class Meta:
        model = ChocHut
        fields = ('HCG',
                  'gioCH',
                  'soNang',
                  'added',
                  'stt'
                  )


class FormCP(forms.ModelForm):
    class Meta:
        model = ChuyenPhoi
        fields = ('soPhoiRa',
                  'ngayKiemTra',
                  'ngayChuyenPhoi',
                  'ngayRaPhoi',
                  'added'
                  )


class FormDP(forms.ModelForm):
    class Meta:
        model = DongPhoi
        fields = ('ngayDongPhoi',
                  'ngayNopTien',
                  'added'
                  )


class FormExCH(forms.Form):
    chonNgay = forms.DateField()


class FormTK(forms.Form):
    thang = forms.IntegerField(validators=[MinValueValidator(1)])
    nam = forms.IntegerField(validators=[MinValueValidator(2017)])
    tongSoTreSinh = forms.IntegerField(validators=[MinValueValidator(0)])
    tongSoTuiThai = forms.IntegerField(validators=[MinValueValidator(0)])


class FormX(forms.Form):
    t1t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t1t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t2t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t2t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t3t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t3t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t4t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t4t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t5t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t5t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t6t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t6t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t7t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t7t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t8t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t8t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t9t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t9t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t10t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t10t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t11t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t11t2 = forms.IntegerField(validators=[MinValueValidator(0)])
    t12t1 = forms.IntegerField(validators=[MinValueValidator(0)])
    t12t2 = forms.IntegerField(validators=[MinValueValidator(0)])
