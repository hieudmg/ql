# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import ThongTin, Trung, BacSi, TruPhoi, Phoi, TinhDichDoNgayCH, KyThuatVien, ChocHut, ChuyenPhoi, DongPhoi
from .forms import FormTT, FormTR, FormP, FormTP, FormTD, FormBS, FormKTV, FormCH, FormCP, FormDP, FormExCH
from datetime import *
from dateutil.relativedelta import relativedelta
from docx import Document
from django.core.files.storage import FileSystemStorage
from docx.shared import *


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
                'dongphoi': dongphoi
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
            'dongphoi': dongphoi
        })
    else:
        context = {'dongphoi': dongphoi}
        data['html_form'] = render_to_string('benhnhan/includes/dongphoi_del.html', context, request=request)
    return JsonResponse(data)


def chochut_ex(request):
    data = dict()
    chochut = ChocHut.objects.filter(added=True)
    if request.method == 'POST':
        formch = FormExCH(request.POST)
        if formch.is_valid():
            print (formch.cleaned_data['chonNgay'])
            document = Document('landscape-template.docx')
            document._body.clear_content()
            document.add_heading(u"Ngày chọc hút: " + formch.cleaned_data['chonNgay'].strftime("%d/%m/%Y"), level=1)

            row = 0
            chdis = []
            for ch in chochut:
                if ch.gioCH.date() == formch.cleaned_data['chonNgay']:
                    print (ch.tt.tenVo)
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
            table.allow_autofit = True
            for i in range(row):
                ci = chdis[i]
                cell = table.cell(i, 0)
                cell.text = str(i+1)
                cell.paragraphs[0].style = document.styles['Text2']

                cell = table.cell(i, 1)
                tv = ci.tt.tenVo.split()[-1]
                print (tv)
                cell.text = tv
                cell.paragraphs[0].style = document.styles['Text2']
                cell.add_paragraph(ci.tt.tenVo + u' - ' + str(ci.tt.nsVo), style='Text3')
                cell.add_paragraph(ci.tt.tenChong + u' - ' + str(ci.tt.nsChong), style='Text3')

                cell = table.cell(i, 2)
                cell.text = 'HCG: ' + ci.HCG.strftime('%H:%m')
                cell.paragraphs[0].style = document.styles['Text4']
                # cell.paragraphs[0].paragraph_format = document.styles['Text4'].paragraph_format
                # cell.add_paragraph('HCG: ' + ci.HCG.strftime('%H:%m'), style='Text4')
                cell.add_paragraph('CH: ' + ci.gioCH.strftime('%H:%m'), style='Text4')
                cell.add_paragraph('BS: ' + ci.tt.bs.ten, style='Text4')
                cell.add_paragraph(str(ci.soNang)+'N', style='Text2')

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

            response = HttpResponse(
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=download.docx'
            document.save('download.docx')
            # data['file'] = response
        else:
            data['form_is_valid'] = False
    else:
        formch = FormExCH()
    context = {'formch': formch}
    data['html_form'] = render_to_string('benhnhan/includes/chochut_ex.html', context, request=request)
    return JsonResponse(data)


def download(request):
    fs = FileSystemStorage()
    filename = 'download.docx'
    with fs.open(filename) as docx:
        response = HttpResponse(docx,
                                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="download.docx"'
        return response
