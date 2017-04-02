var $ = jQuery;

function loadData(){
    $('#thongtin-table').DataTable({
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

$(function () {
  $(".js-thongtin-add").click(function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-thongtin-setup").removeClass("modal-lg");
        $("#modal-thongtin").modal("show");
      },
      success: function (data) {
        $("#modal-thongtin .modal-content").html(data.html_form);
      }
    });
  });
});

$("#modal-thongtin").on("submit", ".js-thongtin-add-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_thongtin_preview);  // <-- Replace the table body
            $("#modal-thongtin").modal("hide");
            loadData();
            toastr.success('Thêm thành công');
                /*$.ajax({
                    url: "add/trung",
                    type: 'get',
                    dataType: 'json',
                    beforeSend: function () {
                        $("#modal-trung").modal("show");
                    },
                    success: function (data) {
                        $("#modal-trung .modal-content").html(data.html_formtr);
                    }
                });*/
        }
        else {
          $("#modal-thongtin .modal-content").html(data.html_form);
        }
      }
    });
    return false;
});

  $("#modal-trung").on("submit", ".js-trung-add-form", function(){
    var formtr = $(this);
    $.ajax({
      url: formtr.attr("action"),
      data: formtr.serialize(),
      type: formtr.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.formtr_is_valid) {
          $("#modal-trung").modal("hide");  // <-- Close the modal
        }
        else {
          $("#modal-trung .modal-content").html(data.html_formtr);
        }
      }
    });
    return false;
  });

  $("#modal-thongtin").on("submit", ".js-thongtin-info-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_thongtin_preview);  // <-- Replace the table body
          $("#modal-thongtin").modal("hide");
            loadData();
            toastr.success('Sửa thành công');
        }
        else {
          $("#modal-thongtin .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


  $("#modal-thongtin").on("submit", ".js-thongtin-edit-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_thongtin_preview);  // <-- Replace the table body
          $("#modal-thongtin").modal("hide");
          loadData();
            toastr.success('Sửa thành công');
        }
        else {
          $("#modal-thongtin .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

    $("#modal-thongtin").on("submit", ".js-thongtin-del-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_thongtin_preview);  // <-- Replace the table body
            $("#modal-thongtin").modal("hide");
            loadData();
            toastr.success('Đã xóa');
          }
          else {
            $("#modal-thongtin .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    });


$( ".dropdown-submenu" ).click(function(event) {
    event.stopPropagation();
    $( this ).find(".dropdown-submenu").removeClass('open');
    $( this ).parents(".dropdown-submenu").addClass('open');
    $( this ).toggleClass('open');
});

$(function() {
    $.contextMenu({
        selector: '.context-button',
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
                            $("#modal-thongtin-setup").addClass("modal-lg");
                        else
                            $("#modal-thongtin-setup").removeClass("modal-lg");
                        $("#modal-thongtin").modal("show");
                    },
                    success: function (data) {
                        $("#modal-thongtin .modal-content").html(data.html_form);
                    }
                });
        },
        items: {
            "info": {name: 'Cập nhật thông tin'},
            "edit": {name: 'Thông tin bệnh nhân'},
            "addto": {
              name: 'Thêm vào',
                items: {
                    "normalsub1": { name: "Bảng chọc hút",
                    callback: function (key, opt){alert('Đang phát triển')}},
                    "normalsub2": { name: "Bảng chuyển phôi",
                    callback: function (key, opt){alert('Đang phát triển')}},
                    "normalsub3": { name: "Bảng đông phôi",
                    callback: function (key, opt){alert('Đang phát triển')}}
                }
            },
            "sep1": "---------",
            "del": {name: "Xóa", className:"context_del"}
        }
    });
});

