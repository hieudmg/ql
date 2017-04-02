# coding=utf-8
from django import forms
from django.forms import DateTimeField
from .models import ThongTin, Trung, Phoi, TruPhoi, TinhDichDoNgayCH, BacSi, KyThuatVien
from django.utils.translation import activate

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
                  'hienNoan'
                  )
        error_messages = {
            'nsVo': {'max': u'Năm sinh nằm trong khoảng 1950-2000'}
        }


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
                  'loai00',
                  'loai01',
                  'loai02',
                  'loai03',
                  'loai10',
                  'loai11',
                  'loai12',
                  'loai13',
                  'loai20',
                  'loai21',
                  'loai22',
                  'loai23',
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
                  'testTime',
                  )
