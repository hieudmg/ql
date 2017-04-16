# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import ThongTin, Trung, BacSi, TruPhoi, Phoi, TinhDichDoNgayCH, KyThuatVien, ChocHut, ChuyenPhoi
from .forms import FormTT, FormTR, FormP, FormTP, FormTD, FormBS, FormKTV, FormCH, FormCP
from datetime import datetime


def thongtin_list(request):
    thongtin = ThongTin.objects.all()
    return render(request, 'benhnhan/thongtin_list.html', {'thongtin': thongtin})


def test(request):
    return render(request, 'benhnhan/test.html')


def thongtin_add(request):
    data = dict()

    if request.method == 'POST':
        form = FormTT(request.POST)
        if form.is_valid():
            form.save()
            tt = ThongTin.objects.latest('id')
            tr = Trung(tt=tt)
            tr.save()
            tp = TruPhoi(tt=tt)
            tp.save()
            p = Phoi(tt=tt)
            p.save()
            td = TinhDichDoNgayCH(tt=tt)
            td.save()
            ch = ChocHut(tt=tt)
            ch.save()
            cp = ChuyenPhoi(tt=tt)
            cp.save()
            data['form_is_valid'] = True
            thongtin = ThongTin.objects.all()
            data['html_thongtin_preview'] = render_to_string('benhnhan/includes/thongtin_preview.html', {
                'thongtin': thongtin
            })
        else:
            data['form_is_valid'] = False
    else:
        form = FormTT()

    context = {'form': form}
    data['html_form'] = render_to_string('benhnhan/includes/thongtin_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def trung_add(request):
    data = dict()
    tt = ThongTin.objects.latest('id')
    tr = Trung(tt=tt)

    if request.method == 'POST':
        formtr = FormTR(request.POST, instance=tr)
        if formtr.is_valid():
            formtr.save()
            data['formtr_is_valid'] = True
        else:
            data['formtr_is_valid'] = False
    else:
        formtr = FormTR(instance=tr)

    context = {'formtr': formtr}
    data['html_formtr'] = render_to_string('benhnhan/includes/trung_add.html',
                                           context,
                                           request=request
                                           )
    return JsonResponse(data)


def thongtin_edit(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)

    if request.method == 'POST':
        form = FormTT(request.POST, instance=thongtin)
        formtr = FormTR(request.POST, instance=thongtin.trung)
        formp = FormP(request.POST, instance=thongtin.phoi)
        formtp = FormTP(request.POST, instance=thongtin.truphoi)
        formtd = FormTD(request.POST, instance=thongtin.tinhdichdongaych)
        if formtd.is_valid() and formtr.is_valid() and formp.is_valid() and formtp.is_valid():
            # form.save()
            formtr.save()
            formp.save()
            formtp.save()
            formtd.save()
            data['form_is_valid'] = True
            thongtin = ThongTin.objects.all()
            data['html_thongtin_preview'] = render_to_string('benhnhan/includes/thongtin_preview.html', {
                'thongtin': thongtin
            })
        else:
            data['form_is_valid'] = False
    else:
        form = FormTT(instance=thongtin)
        formtr = FormTR(instance=thongtin.trung)
        formp = FormP(instance=thongtin.phoi)
        formtp = FormTP(instance=thongtin.truphoi)
        formtd = FormTD(instance=thongtin.tinhdichdongaych)

    context = {'form': form, 'formtr': formtr, 'formp': formp, 'formtp': formtp, 'formtd': formtd}
    data['html_form'] = render_to_string('benhnhan/includes/thongtin_edit.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def thongtin_info(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    if request.method == 'POST':
        form = FormTT(request.POST, instance=thongtin)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            thongtin = ThongTin.objects.all()
            data['html_thongtin_preview'] = render_to_string('benhnhan/includes/thongtin_preview.html', {
                'thongtin': thongtin
            })
        else:
            data['form_is_valid'] = False
    else:
        form = FormTT(instance=thongtin)

    context = {'form': form, }
    data['html_form'] = render_to_string('benhnhan/includes/thongtin_info.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def thongtin_del(request, pk):
    tt_del = get_object_or_404(ThongTin, pk=pk)
    data = dict()
    if request.method == 'POST':
        tt_del.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        thongtin = ThongTin.objects.all()
        data['html_thongtin_preview'] = render_to_string('benhnhan/includes/thongtin_preview.html', {
            'thongtin': thongtin
        })
    else:
        context = {'tt_del': tt_del}
        data['html_form'] = render_to_string('benhnhan/includes/thongtin_del.html', context, request=request)
    return JsonResponse(data)


def bacsi_list(request):
    bacsi = BacSi.objects.all()
    return render(request, 'bacsi/bacsi_list.html', {'bacsi': bacsi})


def bacsi_add(request):
    data = dict()

    if request.method == 'POST':
        formbs = FormBS(request.POST)
        if formbs.is_valid():
            formbs.save()
            bacsi = BacSi.objects.all()
            data['form_is_valid'] = True
            data['html_bacsi_preview'] = render_to_string('bacsi/includes/bacsi_preview.html', {
                'bacsi': bacsi
            })
        else:
            data['form_is_valid'] = False
    else:
        formbs = FormBS()

    context = {'formbs': formbs}
    data['html_form'] = render_to_string('bacsi/includes/bacsi_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def bacsi_edit(request, pk):
    data = dict()
    bacsi = get_object_or_404(BacSi, pk=pk)
    if request.method == 'POST':
        formbs = FormBS(request.POST, instance=bacsi)
        if formbs.is_valid():
            formbs.save()
            data['form_is_valid'] = True
            bacsi = BacSi.objects.all()
            data['html_bacsi_preview'] = render_to_string('bacsi/includes/bacsi_preview.html', {
                'bacsi': bacsi
            })
        else:
            data['form_is_valid'] = False
    else:
        formbs = FormBS(instance=bacsi)

    context = {'formbs': formbs, }
    data['html_form'] = render_to_string('bacsi/includes/bacsi_edit.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def bacsi_del(request, pk):
    data = dict()
    bacsi = get_object_or_404(BacSi, pk=pk)
    if request.method == 'POST':
        bacsi.delete()
        data['form_is_valid'] = True
        bacsi = BacSi.objects.all()
        data['html_bacsi_preview'] = render_to_string('bacsi/includes/bacsi_preview.html', {
            'bacsi': bacsi
        })
    else:
        context = {'bacsi': bacsi}
        data['html_form'] = render_to_string('bacsi/includes/bacsi_del.html', context, request=request)
    return JsonResponse(data)


def kythuatvien_list(request):
    kythuatvien = KyThuatVien.objects.all()
    return render(request, 'kythuatvien/kythuatvien_list.html', {'kythuatvien': kythuatvien})


def kythuatvien_add(request):
    data = dict()

    if request.method == 'POST':
        formktv = FormKTV(request.POST)
        if formktv.is_valid():
            formktv.save()
            kythuatvien = KyThuatVien.objects.all()
            data['form_is_valid'] = True
            data['html_kythuatvien_preview'] = render_to_string('kythuatvien/includes/kythuatvien_preview.html', {
                'kythuatvien': kythuatvien
            })
        else:
            data['form_is_valid'] = False
    else:
        formktv = FormKTV()

    context = {'formktv': formktv}
    data['html_form'] = render_to_string('kythuatvien/includes/kythuatvien_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def kythuatvien_edit(request, pk):
    data = dict()
    kythuatvien = get_object_or_404(KyThuatVien, pk=pk)
    if request.method == 'POST':
        formktv = FormKTV(request.POST, instance=kythuatvien)
        if formktv.is_valid():
            formktv.save()
            data['form_is_valid'] = True
            kythuatvien = KyThuatVien.objects.all()
            data['html_kythuatvien_preview'] = render_to_string('kythuatvien/includes/kythuatvien_preview.html', {
                'kythuatvien': kythuatvien
            })
        else:
            data['form_is_valid'] = False
    else:
        formktv = FormKTV(instance=kythuatvien)

    context = {'formktv': formktv, }
    data['html_form'] = render_to_string('kythuatvien/includes/kythuatvien_edit.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def kythuatvien_del(request, pk):
    data = dict()
    kythuatvien = get_object_or_404(KyThuatVien, pk=pk)
    if request.method == 'POST':
        kythuatvien.delete()
        data['form_is_valid'] = True
        kythuatvien = KyThuatVien.objects.all()
        data['html_kythuatvien_preview'] = render_to_string('kythuatvien/includes/kythuatvien_preview.html', {
            'kythuatvien': kythuatvien
        })
    else:
        context = {'kythuatvien': kythuatvien}
        data['html_form'] = render_to_string('kythuatvien/includes/kythuatvien_del.html', context, request=request)
    return JsonResponse(data)


def chochut_list(request):
    chochut = ChocHut.objects.all()
    return render(request, 'benhnhan/chochut_list.html', {'chochut': chochut})


def chochut_add(request, pk):
    data = dict()

    thongtin = get_object_or_404(ThongTin, pk=pk)
    chochut = thongtin.chochut
    if not chochut.added:
        chochut.HCG = datetime.now
        chochut.gioCH = datetime.now

    if request.method == 'POST':
        formch = FormCH(request.POST, instance=chochut)
        form = FormTT(request.POST, instance=thongtin)
        if formch.is_valid():
            formch.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        formch = FormCH(instance=chochut)
        form = FormTT(instance=thongtin)

    context = {'formch': formch, 'form': form}
    data['html_form'] = render_to_string('benhnhan/includes/chochut_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def chochut_edit(request, pk):
    data = dict()

    thongtin = get_object_or_404(ThongTin, pk=pk)
    chochut = thongtin.chochut
    if request.method == 'POST':
        formch = FormCH(request.POST, instance=chochut)
        form = FormTT(instance=thongtin)
        if formch.is_valid():
            formch.save()
            chochut = ChocHut.objects.all()
            data['html_chochut_preview'] = render_to_string('benhnhan/includes/chochut_preview.html', {
                'chochut': chochut
            })
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        formch = FormCH(instance=chochut)
        form = FormTT(instance=thongtin)

    context = {'formch': formch, 'form': form}
    data['html_form'] = render_to_string('benhnhan/includes/chochut_edit.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def chochut_del(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    chochut = thongtin.chochut

    if request.method == 'POST':
        chochut.added = False
        chochut.save()
        data['form_is_valid'] = True
        chochut = ChocHut.objects.all()
        data['html_chochut_preview'] = render_to_string('benhnhan/includes/chochut_preview.html', {
            'chochut': chochut
        })
    else:
        context = {'chochut': chochut}
        data['html_form'] = render_to_string('benhnhan/includes/chochut_del.html', context, request=request)
    return JsonResponse(data)


def chuyenphoi_list(request):
    chuyenphoi = ChuyenPhoi.objects.all()
    return render(request, 'benhnhan/chuyenphoi_list.html', {'chuyenphoi': chuyenphoi})


def chuyenphoi_add(request, pk):
    data = dict()

    thongtin = get_object_or_404(ThongTin, pk=pk)
    chuyenphoi = thongtin.chuyenphoi
    if not chuyenphoi.added:
        chuyenphoi.ngayChuyenPhoi = datetime.now
        chuyenphoi.ngayKiemTra = datetime.now

    if request.method == 'POST':
        formcp = FormCP(request.POST, instance=chuyenphoi)
        form = FormTT(request.POST, instance=thongtin)
        if formcp.is_valid():
            formcp.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        formcp = FormCP(instance=chuyenphoi)
        form = FormTT(instance=thongtin)

    context = {'formcp': formcp, 'form': form}
    data['html_form'] = render_to_string('benhnhan/includes/chuyenphoi_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def chuyenphoi_edit(request, pk):
    data = dict()

    thongtin = get_object_or_404(ThongTin, pk=pk)
    chuyenphoi = thongtin.chuyenphoi
    if request.method == 'POST':
        formcp = FormCP(request.POST, instance=chuyenphoi)
        form = FormTT(instance=thongtin)
        if formcp.is_valid():
            formcp.save()
            chuyenphoi = ChuyenPhoi.objects.all()
            data['html_chuyenphoi_preview'] = render_to_string('benhnhan/includes/chuyenphoi_preview.html', {
                'chuyenphoi': chuyenphoi
            })
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        formcp = FormCP(instance=chuyenphoi)
        form = FormTT(instance=thongtin)

    context = {'formcp': formcp, 'form': form}
    data['html_form'] = render_to_string('benhnhan/includes/chuyenphoi_edit.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def chuyenphoi_del(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    chuyenphoi = thongtin.chuyenphoi

    if request.method == 'POST':
        chuyenphoi.added = False
        chuyenphoi.save()
        data['form_is_valid'] = True
        chuyenphoi = ChuyenPhoi.objects.all()
        data['html_chuyenphoi_preview'] = render_to_string('benhnhan/includes/chuyenphoi_preview.html', {
            'chuyenphoi': chuyenphoi
        })
    else:
        context = {'chuyenphoi': chuyenphoi}
        data['html_form'] = render_to_string('benhnhan/includes/chuyenphoi_del.html', context, request=request)
    return JsonResponse(data)
