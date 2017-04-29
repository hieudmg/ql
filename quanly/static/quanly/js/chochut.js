function loadData(){
    $('#thongtin-table').DataTable({
    "order": [],
        columnDefs: [
            { orderable: false, targets: [0, 1, 2, 3, 4, 5, 6, 7, 9, 10] }
        ],
    "oLanguage": {
          "oPaginate": {
            "sFirst": "Đầu",
            "sLast": "Cuối",
            "sNext": "Sau",
            "sPrevious": "Trước"
          },
      "sInfo": "Hiển thị từ _START_ đến _END_ (Tổng số: _TOTAL_)",
      "sInfoEmpty": "Không tìm thấy dữ liệu phù hợp",
      "sInfoFiltered": "",
      "sSearch": "Tìm kiếm",
      "sZeroRecords": "Không tìm thấy dữ liệu phù hợp",
      "sLengthMenu": 'Số lượng hiển thị: <select name="thongtin-table_length" aria-controls="thongtin-table" class="form-control input-sm"">'+
        '<option value="10">10</option>'+
        '<option value="30">30</option>'+
        '<option value="50">50</option>'+
        '<option value="-1">Tất cả</option>'+
        '</select>'
    }
   });

}

$(document).ready(function() {
  loadData();
    toastr.options = {
      "closeButton": false,
      "debug": false,
      "newestOnTop": false,
      "progressBar": false,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "300",
      "timeOut": "2400",
      "extendedTimeOut": "300",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
    }
});


    $("#modal-chochut").on("submit", ".js-chochut-edit-form", function(){
    var formch = $(this);
    $.ajax({
      url: formch.attr("action"),
      data: formch.serialize(),
      type: formch.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_chochut_preview);  // <-- Replace the table body
            $("#modal-chochut").modal("hide");
            loadData();
            toastr.success('Sửa thành công');
        }
        else {
          $("#modal-chochut .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


    $("#modal-chochut").on("submit", ".js-chochut-del-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_chochut_preview);  // <-- Replace the table body
            $("#modal-chochut").modal("hide");
            loadData();
            toastr.success('Đã xóa');
          }
          else {
            $("#modal-chochut .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    });



    $.contextMenu({
        selector: '.context-chochut',
        trigger: 'left',
        zIndex: 100,
        callback: function (key, opt) {
            if (opt.$trigger.attr("data-url"))
                $.ajax({
                    url: opt.$trigger.attr("data-url") + key,
                    type: 'get',
                    dataType: 'json',
                    beforeSend: function () {
                        if (!(key.localeCompare('edit')))
                            $("#modal-chochut-setup").addClass("modal-lg");
                        else
                            $("#modal-chochut-setup").removeClass("modal-lg");
                        $("#modal-chochut").modal("show");
                    },
                    success: function (data) {
                        $("#modal-chochut .modal-content").html(data.html_form);
                    }
                });
        },
        items: {
            "editch": {name: 'Sửa',
                    callback: function (key, opt){
                            if (opt.$trigger.attr("data-url"))
                                $.ajax({
                                    url: opt.$trigger.attr("data-url") + key,
                                    type: 'get',
                                    dataType: 'json',
                                    beforeSend: function () {
                                        $("#modal-chochut-setup").removeClass("modal-lg");
                                        $("#modal-chochut").modal("show");
                                    },
                                    success: function (data) {
                                        $("#modal-chochut .modal-content").html(data.html_form);
                                    }
                                });
                            }},
            "ex": {
                name: 'Phiếu thông báo kết quả',
                items: {
                    "trudongphoi": {name: "Phiếu nhận trữ đông phôi"},
                    "ketquaphoi": {name: "Phiếu thông báo kết quả phôi"},
                    "theodoiphoi": {name: "Phiếu theo dõi phôi"},
                    "truraphoi": {name: "Phiếu theo dõi trữ - rã phôi"},
                    "IVF": {name: "Quy trình thực hiện IVF"}
                }
            },
            "sep1": "---------",
            "delch": {name: "Xóa",
                    callback: function (key, opt){
                            if (opt.$trigger.attr("data-url"))
                                $.ajax({
                                    url: opt.$trigger.attr("data-url") + key,
                                    type: 'get',
                                    dataType: 'json',
                                    beforeSend: function () {
                                        $("#modal-chochut-setup").removeClass("modal-lg");
                                        $("#modal-chochut").modal("show");
                                    },
                                    success: function (data) {
                                        $("#modal-chochut .modal-content").html(data.html_form);
                                    }
                                });
                            },
            className:"context_del"}
        }
    });



$(function () {
  $(".js-chochut-ex").click(function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-chochut-setup").removeClass("modal-lg");
        $("#modal-chochut").modal("show");
      },
      success: function (data) {
        $("#modal-chochut .modal-content").html(data.html_form);
      }
    });
  });
});


$("#modal-chochut").on("submit", ".js-chochut-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-chochut").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-chochut .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});




$("#modal-chochut").on("submit", ".js-trudongphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-chochut").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-chochut .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-chochut").on("submit", ".js-ketquaphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-chochut").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-chochut .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-chochut").on("submit", ".js-theodoiphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-chochut").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-chochut .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-chochut").on("submit", ".js-truraphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-chochut").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-chochut .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-chochut").on("submit", ".js-IVF-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-chochut").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-chochut .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});