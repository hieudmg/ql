# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import ThongTin, Trung, BacSi, TruPhoi, Phoi, TinhDichDoNgayCH, KyThuatVien, ChocHut, ChuyenPhoi, DongPhoi
from .forms import FormTT, FormTR, FormP, FormTP, FormTD, FormBS, FormKTV, FormCH, FormCP, FormDP, FormExCH
from datetime import *
from dateutil.relativedelta import relativedelta
from docx import Document
from docx.shared import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


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
            dp = DongPhoi(tt=tt)
            dp.save()
            data['form_is_valid'] = True
            thongtin = ThongTin.objects.all()
            data['html_thongtin_preview'] = render_to_string('benhnhan/includes/thongtin_preview.html', {
                'thongtin': thongtin, 'user': request.user
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
                'thongtin': thongtin, 'user': request.user
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
                'thongtin': thongtin, 'user': request.user
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
            'thongtin': thongtin, 'user': request.user
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
                'bacsi': bacsi, 'user': request.user
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
                'bacsi': bacsi, 'user': request.user
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
            'bacsi': bacsi, 'user': request.user
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
                'kythuatvien': kythuatvien, 'user': request.user
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
                'kythuatvien': kythuatvien, 'user': request.user
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
            'kythuatvien': kythuatvien, 'user': request.user
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
        chochut.stt = len(ChocHut.objects.filter(added=True)) + 1

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
                'chochut': chochut, 'user': request.user
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
        chochut = ChocHut.objects.filter(added=True).order_by('stt')
        _i = 1
        for ch in chochut:
            ch.stt = _i
            ch.save()
            _i += 1
        chochut = ChocHut.objects.all()
        data['html_chochut_preview'] = render_to_string('benhnhan/includes/chochut_preview.html', {
            'chochut': chochut, 'user': request.user
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
        chuyenphoi.ngayChuyenPhoi = date.today()
        chuyenphoi.ngayKiemTra = date.today()

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
                'chuyenphoi': chuyenphoi, 'user': request.user
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
            'chuyenphoi': chuyenphoi, 'user': request.user
        })
    else:
        context = {'chuyenphoi': chuyenphoi}
        data['html_form'] = render_to_string('benhnhan/includes/chuyenphoi_del.html', context, request=request)
    return JsonResponse(data)


def dongphoi_list(request):
    dongphoi = DongPhoi.objects.all()
    return render(request, 'benhnhan/dongphoi_list.html', {'dongphoi': dongphoi})


def dongphoi_add(request, pk):
    data = dict()

    thongtin = get_object_or_404(ThongTin, pk=pk)
    dongphoi = thongtin.dongphoi
    if not dongphoi.added:
        dtn = date.today()
        dongphoi.ngayDongPhoi = dtn
        dongphoi.ngayNopTien = dtn + relativedelta(years=1)

    if request.method == 'POST':
        formdp = FormDP(request.POST, instance=dongphoi)
        form = FormTT(request.POST, instance=thongtin)
        if formdp.is_valid():
            formdp.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        formdp = FormDP(instance=dongphoi)
        form = FormTT(instance=thongtin)

    context = {'formdp': formdp, 'form': form}
    data['html_form'] = render_to_string('benhnhan/includes/dongphoi_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def dongphoi_edit(request, pk):
    data = dict()

    thongtin = get_object_or_404(ThongTin, pk=pk)
    dongphoi = thongtin.dongphoi
    if request.method == 'POST':
        formdp = FormDP(request.POST, instance=dongphoi)
        form = FormTT(instance=thongtin)
        if formdp.is_valid():
            formdp.save()
            dongphoi = DongPhoi.objects.all()
            data['html_dongphoi_preview'] = render_to_string('benhnhan/includes/dongphoi_preview.html', {
                'dongphoi': dongphoi, 'user': request.user
            })
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        formdp = FormDP(instance=dongphoi)
        form = FormTT(instance=thongtin)

    context = {'formdp': formdp, 'form': form}
    data['html_form'] = render_to_string('benhnhan/includes/dongphoi_edit.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def dongphoi_del(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    dongphoi = thongtin.dongphoi

    if request.method == 'POST':
        dongphoi.added = False
        dongphoi.save()
        data['form_is_valid'] = True
        dongphoi = DongPhoi.objects.all()
        data['html_dongphoi_preview'] = render_to_string('benhnhan/includes/dongphoi_preview.html', {
            'dongphoi': dongphoi, 'user': request.user
        })
    else:
        context = {'dongphoi': dongphoi}
        data['html_form'] = render_to_string('benhnhan/includes/dongphoi_del.html', context, request=request)
    return JsonResponse(data)


last_file_name = ''


def chochut_ex(request):
    data = dict()
    chochut = ChocHut.objects.filter(added=True)
    if request.method == 'POST':
        formch = FormExCH(request.POST)
        if formch.is_valid():
            document = Document('docx/landscape-template.docx')
            document._body.clear_content()
            document.add_heading(u"Ngày chọc hút: " + formch.cleaned_data['chonNgay'].strftime("%d/%m/%Y"), level=1)

            row = 0
            chdis = []
            for ch in chochut:
                if ch.gioCH.date() == formch.cleaned_data['chonNgay']:
                    chdis.append(1)
                    chdis[row] = ch
                    row += 1

            table = document.add_table(rows=row, cols=0, style='Table1')
            table.add_column(width=Cm(0.83))
            table.add_column(width=Cm(7.66))
            table.add_column(width=Cm(3.83))
            table.add_column(width=Cm(3.42))
            table.add_column(width=Cm(5.75))
            table.add_column(width=Cm(3.11))
            for i in range(row):
                ci = chdis[i]
                cell = table.cell(i, 0)
                cell.text = str(i + 1)
                cell.paragraphs[0].style = document.styles['Text2']

                cell = table.cell(i, 1)
                tv = ci.tt.tenVo.split()[-1]
                cell.text = tv
                cell.paragraphs[0].style = document.styles['Text2']
                cell.add_paragraph(ci.tt.tenVo + u' - ' + str(ci.tt.nsVo), style='Text3')
                cell.add_paragraph(ci.tt.tenChong + u' - ' + str(ci.tt.nsChong), style='Text3')

                cell = table.cell(i, 2)
                cell.text = 'HCG: ' + ci.HCG.strftime('%H:%M')
                cell.paragraphs[0].style = document.styles['Text4']
                # cell.paragraphs[0].paragraph_format = document.styles['Text4'].paragraph_format
                # cell.add_paragraph('HCG: ' + ci.HCG.strftime('%H:%m'), style='Text4')
                cell.add_paragraph('CH: ' + ci.gioCH.strftime('%H:%M'), style='Text4')
                cell.add_paragraph('BS: ' + ci.tt.bs.ten, style='Text4')
                cell.add_paragraph(str(ci.soNang) + 'N', style='Text2')

                cell = table.cell(i, 3)
                cell.text = '          M2'
                cell.paragraphs[0].style = document.styles['Text3']
                cell.add_paragraph('          M1', style='Text3')
                cell.add_paragraph('          GV', style='Text3')
                cell.add_paragraph('          TH', style='Text3')

                cell = table.cell(i, 5)
                cell.text = 'HS'
                cell.paragraphs[0].style = document.styles['Text4']
                cell.add_paragraph(ci.tt.maSo, style='Text4')

            data['form_is_valid'] = True

            document.save('docx/download.docx')
            global last_file_name
            last_file_name = 'attachment; filename="Choc-hut-' \
                             + formch.cleaned_data['chonNgay'].strftime("%d-%m-%Y") \
                             + '.docx"'
        else:
            data['form_is_valid'] = False
    else:
        formch = FormExCH()
    context = {'formch': formch}
    data['html_form'] = render_to_string('benhnhan/includes/chochut_ex.html', context, request=request)
    return JsonResponse(data)


def toColor(hexx):
    if hexx == '#ff0000':
        return u'Đỏ'
    elif hexx == '#00ff00':
        return u'Xanh lá'
    elif hexx == '#0000ff':
        return u'Xanh dương'
    elif hexx == '#ffff00':
        return u'Vàng'
    elif hexx == '#fcfbe3':
        return u'Kem'
    elif hexx == '#ffffff':
        return u'Trắng'
    elif hexx == '#ffa500':
        return u'Cam'
    else:
        return u'Đã chuyển'


def trudongphoi(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    dongphoi = thongtin.dongphoi
    if request.method == 'POST':
        formch = FormExCH(request.POST)
        if formch.is_valid():
            document = Document('docx/trudongphoi.docx')
            table = document.tables[0]
            table.cell(0, 0).paragraphs[3].add_run(thongtin.maSo, 't1')
            table.cell(0, 1).paragraphs[0].add_run(u'Hà Nội, ngày ' + formch.cleaned_data['chonNgay'].strftime('%d') +
                                                   u' tháng ' + formch.cleaned_data['chonNgay'].strftime('%m') +
                                                   u' năm ' + formch.cleaned_data['chonNgay'].strftime('%Y'), 't2')
            table.cell(3, 0).paragraphs[0].add_run(thongtin.tenVo, 't3')
            table.cell(3, 0).paragraphs[1].add_run(thongtin.tenChong, 't3')
            table.cell(3, 0).paragraphs[2].add_run(thongtin.lienHe, 't3')
            table.cell(3, 0).paragraphs[4].add_run(dongphoi.ngayDongPhoi.strftime('%d/%m/%Y'), 't3')
            cassettle = toColor(thongtin.truphoi.label00) + ', ' + toColor(thongtin.truphoi.label01)
            table.cell(3, 0).paragraphs[6].add_run(cassettle, 't1')
            table.cell(3, 5).paragraphs[0].add_run(str(thongtin.nsVo), 't1')
            table.cell(3, 5).paragraphs[1].add_run(str(thongtin.nsChong), 't1')
            table.cell(4, 3).paragraphs[0].add_run(str(thongtin.phoi.soPhoiN2), 't3')
            table.cell(4, 3).paragraphs[1].add_run(str(thongtin.phoi.soPhoiN3), 't3')
            table.cell(4, 3).paragraphs[2].add_run(str(thongtin.phoi.soPhoiN4), 't3')
            table.cell(4, 3).paragraphs[3].add_run(str(thongtin.phoi.soPhoiN5), 't3')
            table.cell(4, 5).paragraphs[0].add_run(str(thongtin.phoi.soCryotop2), 't3')
            table.cell(4, 5).paragraphs[1].add_run(str(thongtin.phoi.soCryotop3), 't3')
            table.cell(4, 5).paragraphs[2].add_run(str(thongtin.phoi.soCryotop4), 't3')
            table.cell(4, 5).paragraphs[3].add_run(str(thongtin.phoi.soCryotop5), 't3')

            document.save('docx/download.docx')
            data['form_is_valid'] = True
            global last_file_name
            last_file_name = 'attachment; filename="Phieu-nhan-tru-dong-phoi-' \
                             + formch.cleaned_data['chonNgay'].strftime("%d-%m-%Y") \
                             + '.docx"'
        else:
            data['form_is_valid'] = False
    else:
        formch = FormExCH()
    context = {'formch': formch, 'thongtin': thongtin}
    data['html_form'] = render_to_string('benhnhan/includes/trudongphoi.html', context, request=request)
    return JsonResponse(data)


def chuyenphoi_ex(request):
    data = dict()
    chuyenphoi = ChuyenPhoi.objects.filter(added=True)
    if request.method == 'POST':
        formcp = FormExCH(request.POST)
        if formcp.is_valid():
            document = Document('docx/cpdl.docx')
            document.add_paragraph(formcp.cleaned_data['chonNgay'].strftime("%d/%m/%Y"), style='t1')

            table = document.add_table(rows=0, cols=0, style='Table1')
            table.add_column(width=Cm(1))
            table.add_column(width=Cm(11.75))
            table.add_column(width=Cm(5.75))

            i = 1
            for cp in chuyenphoi:
                if cp.ngayRaPhoi == formcp.cleaned_data['chonNgay']:
                    row = table.add_row()
                    cell = row.cells[0]
                    cell.text = str(i)
                    cell.paragraphs[0].style = document.styles['t2']

                    cell = row.cells[1]
                    cell.text = cp.tt.tenVo.split()[-1]
                    cell.paragraphs[0].style = document.styles['t2']
                    cell.add_paragraph(cp.tt.tenVo + u' - ' + str(cp.tt.nsVo), style='t3')
                    cell.add_paragraph(cp.tt.tenChong + u' - ' + str(cp.tt.nsChong), style='t3')
                    cell.add_paragraph(' ', style='t3')
                    cell.add_paragraph(' ', style='t3')
                    cell.add_paragraph(u'BS ' + cp.tt.bs.ten, style='t4')

                    cell = row.cells[2]
                    cell.text = 'HS: ' + cp.tt.maSo
                    cell.paragraphs[0].style = document.styles['t3']
                    cell.add_paragraph(' ', style='t3')
                    cell.add_paragraph(' ', style='t3')
                    cell.add_paragraph(u'RÃ ' + str(cp.soPhoiRa) + u'P', style='t4')
                    cell.add_paragraph(u'KT ' + cp.ngayKiemTra.strftime('%d/%m'), style='t4')
                    cell.add_paragraph(u'CP ' + cp.ngayChuyenPhoi.strftime('%d/%m'), style='t4')

            data['form_is_valid'] = True

            document.save('docx/download.docx')
            global last_file_name
            last_file_name = 'attachment; filename="Cpdl-' \
                             + formcp.cleaned_data['chonNgay'].strftime("%d-%m-%Y") \
                             + '.docx"'
        else:
            data['form_is_valid'] = False
    else:
        formcp = FormExCH()
    context = {'formcp': formcp}
    data['html_form'] = render_to_string('benhnhan/includes/chuyenphoi_ex.html', context, request=request)
    return JsonResponse(data)


def ketquaphoi(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    if request.method == 'POST':
        formch = FormExCH(request.POST)
        if formch.is_valid():
            document = Document('docx/ketquaphoi.docx')
            table = document.tables[0]
            table.cell(0, 4).paragraphs[0].add_run(thongtin.maSo, 't2')
            table.cell(0, 6).text = str(thongtin.chochut.stt)
            table.cell(0, 6).paragraphs[0].style = document.styles['t1']

            table.cell(2, 1).paragraphs[0].add_run(thongtin.tenVo, 't2')
            table.cell(3, 1).paragraphs[0].add_run(thongtin.tenChong, 't2')
            table.cell(2, 6).paragraphs[0].add_run(str(thongtin.nsVo), 't2')
            table.cell(3, 6).paragraphs[0].add_run(str(thongtin.nsChong), 't2')
            cell = table.cell(4, 0)
            cell.paragraphs[0].add_run('?', 't2')
            cell.paragraphs[1].add_run(str(thongtin.trung.tongSoTrungICSI), 't2')
            cell.paragraphs[2].add_run(str(thongtin.trung.tongSoTrungTT), 't2')
            cell.paragraphs[4].add_run(str(thongtin.trung.tongSoTrungTT), 't2')
            cell.paragraphs[6].add_run(str(thongtin.phoi.loai1), 't2')
            cell.paragraphs[7].add_run(str(thongtin.phoi.loai2), 't2')
            cell.paragraphs[8].add_run(str(thongtin.phoi.loai3), 't2')
            cell.paragraphs[11].add_run(str(thongtin.phoi.tongSoPhoiChuyen), 't2')
            cell.paragraphs[12].add_run(str(thongtin.phoi.tongSoPhoiTiepTucTheoDoi), 't2')
            cell.paragraphs[13].add_run(str(thongtin.phoi.tongSoPhoiLuuTruLanh), 't2')
            cell.paragraphs[14].add_run(str(thongtin.phoi.tongSoPhoiHuy), 't2')
            table.cell(6, 4).paragraphs[0].insert_paragraph_before(
                u'Ngày ' + formch.cleaned_data['chonNgay'].strftime('%d') +
                u' tháng ' + formch.cleaned_data['chonNgay'].strftime('%m') +
                u' năm ' + formch.cleaned_data['chonNgay'].strftime('%Y'), 't3')

            document.save('docx/download.docx')
            data['form_is_valid'] = True
            global last_file_name
            last_file_name = 'attachment; filename="Phieu-thong-bao-ve-ket-qua-phoi-' \
                             + formch.cleaned_data['chonNgay'].strftime("%d-%m-%Y") \
                             + '.docx"'
        else:
            data['form_is_valid'] = False
    else:
        formch = FormExCH()
    context = {'formch': formch, 'thongtin': thongtin}
    data['html_form'] = render_to_string('benhnhan/includes/ketquaphoi.html', context, request=request)
    return JsonResponse(data)


def theodoiphoi(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    if request.method == 'POST':
        formch = FormExCH(request.POST)
        if formch.is_valid():
            document = Document('docx/theodoiphoi.docx')
            table = document.tables[0]
            table.cell(0, 3).paragraphs[0].add_run(str(thongtin.maSo), 't1')
            table.cell(1, 4).paragraphs[0].add_run(str(thongtin.chochut.stt), 't3')
            table.cell(2, 0).paragraphs[0].add_run(thongtin.tenVo, 't1')
            table.cell(2, 0).paragraphs[1].add_run(thongtin.tenChong, 't1')
            table.cell(2, 2).paragraphs[0].add_run(str(thongtin.nsVo), 't1')
            table.cell(2, 2).paragraphs[1].add_run(str(thongtin.nsChong), 't1')
            table.cell(2, 3).paragraphs[0].add_run(thongtin.chochut.gioCH.strftime('%d/%m/%Y'), 't1')
            table.cell(2, 3).paragraphs[1].add_run(thongtin.bs.ten, 't1')
            table.cell(2, 3).paragraphs[2].add_run(thongtin.chochut.HCG.strftime('%H:%M'), 't1')
            table.cell(2, 3).paragraphs[3].add_run(thongtin.chochut.gioCH.strftime('%H:%M'), 't1')

            document.save('docx/download.docx')
            data['form_is_valid'] = True
            global last_file_name
            last_file_name = 'attachment; filename="Phieu-theo-doi-phoi-' \
                             + thongtin.maSo \
                             + '.docx"'
        else:
            data['form_is_valid'] = False
    else:
        formch = FormExCH()
    context = {'formch': formch, 'thongtin': thongtin}
    data['html_form'] = render_to_string('benhnhan/includes/theodoiphoi.html', context, request=request)
    return JsonResponse(data)


def truraphoi(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    if request.method == 'POST':
        formch = FormExCH(request.POST)
        if formch.is_valid():
            document = Document('docx/truraphoi.docx')
            table = document.tables[0]
            table.cell(0, 10).paragraphs[0].add_run(thongtin.maSo, 't1')
            table.cell(1, 12).paragraphs[0].add_run(str(thongtin.chochut.stt), 't2')
            table.cell(3, 0).paragraphs[0].add_run(thongtin.tenVo, 't1')
            table.cell(3, 0).paragraphs[1].add_run(thongtin.tenChong, 't1')
            table.cell(3, 7).paragraphs[0].add_run(str(thongtin.nsVo), 't1')
            table.cell(3, 7).paragraphs[1].add_run(str(thongtin.nsChong), 't1')
            table.cell(3, 11).paragraphs[1].add_run(str(thongtin.phoi.tongSoPhoiLuuTruLanh), 't1')
            table.cell(4, 0).paragraphs[0].add_run(thongtin.chochut.gioCH.strftime('%d/%m/%Y'), 't1')

            document.save('docx/download.docx')
            data['form_is_valid'] = True
            global last_file_name
            last_file_name = 'attachment; filename="Phieu-theo-doi-tru-ra-phoi-' \
                             + thongtin.maSo \
                             + '.docx"'
        else:
            data['form_is_valid'] = False
    else:
        formch = FormExCH()
    context = {'formch': formch, 'thongtin': thongtin}
    data['html_form'] = render_to_string('benhnhan/includes/truraphoi.html', context, request=request)
    return JsonResponse(data)


def IVF(request, pk):
    data = dict()
    thongtin = get_object_or_404(ThongTin, pk=pk)
    if request.method == 'POST':
        formch = FormExCH(request.POST)
        if formch.is_valid():
            document = Document('docx/IVF.docx')
            table = document.tables[0]
            table.cell(0, 8).paragraphs[0].add_run(str(thongtin.chochut.stt), 't2')
            table.cell(2, 0).paragraphs[0].add_run(thongtin.tenVo, 't1')
            table.cell(2, 0).paragraphs[1].add_run(thongtin.tenChong, 't1')
            table.cell(2, 7).paragraphs[0].add_run(str(thongtin.nsVo), 't1')
            table.cell(2, 7).paragraphs[1].add_run(str(thongtin.nsChong), 't1')
            table.cell(3, 0).paragraphs[0].add_run(thongtin.chochut.gioCH.strftime('%d/%m/%Y'), 't1')
            table.cell(3, 0).paragraphs[1].add_run(thongtin.bs.ten, 't1')

            document.save('docx/download.docx')
            data['form_is_valid'] = True
            global last_file_name
            last_file_name = 'attachment; filename="Bang-kiem-cac-quy-trinh-thuc-hien-IVF-' \
                             + thongtin.maSo \
                             + '.docx"'
        else:
            data['form_is_valid'] = False
    else:
        formch = FormExCH()
    context = {'formch': formch, 'thongtin': thongtin}
    data['html_form'] = render_to_string('benhnhan/includes/IVF.html', context, request=request)
    return JsonResponse(data)


def download(request):
    fs = FileSystemStorage()
    filename = 'docx/download.docx'
    global last_file_name
    with fs.open(filename) as docx:
        response = HttpResponse(docx,
                                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = last_file_name
        return response


def change_password(request):
    data = dict()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            data['password_is_valid'] = 2
        else:
            data['password_is_valid'] = 0
    else:
        form = PasswordChangeForm(request.user)
        data['password_is_valid'] = 1
    return render(request, 'registration/change_password.html', {
        'form': form, 'data': data
    })
