function loadData(){
    $('#thongtin-table').DataTable({
        "order": [[ 0, "desc" ]],
        columnDefs: [
            { orderable: false, targets: [1, 2, 3, 4, 5, 6, 7, 8, 9] }
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
    $('#thongtin-table').bootstrapTable({});
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
      "timeOut": "4400",
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
      success: function (data) {
        if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_thongtin_preview);  // <-- Replace the table body
            $("#modal-thongtin").modal("hide");
            //loadData();
            location.href = location.href;
            toastr.success('Thêm thành công');
        }
        else {
          $("#modal-thongtin .modal-content").html(data.html_form);
        }
      }
    });
    return false;
});

  $("#modal-thongtin").on("submit", ".js-chochut-add-form", function(){
    var formch = $(this);
    $.ajax({
      url: formch.attr("action"),
      data: formch.serialize(),
      type: formch.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-thongtin").modal("hide");  // <-- Close the modal
            toastr.success('Mã số: ' + data.maso + ' thêm thành công vào bảng chọc hút');
        }
        else {
          $("#modal-thongtin .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

  $("#modal-thongtin").on("submit", ".js-chuyenphoi-add-form", function(){
    var formcp = $(this);
    $.ajax({
      url: formcp.attr("action"),
      data: formcp.serialize(),
      type: formcp.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-thongtin").modal("hide");  // <-- Close the modal
            toastr.success('Mã số: ' + data.maso + ' thêm thành công vào bảng chuyển phôi');
        }
        else {
          $("#modal-thongtin .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

  $("#modal-thongtin").on("submit", ".js-dongphoi-add-form", function(){
    var formdp = $(this);
    $.ajax({
      url: formdp.attr("action"),
      data: formdp.serialize(),
      type: formdp.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-thongtin").modal("hide");  // <-- Close the modal
            toastr.success('Mã số: ' + data.maso + ' thêm thành công vào bảng đông phôi');
        }
        else {
          $("#modal-thongtin .modal-content").html(data.html_form);
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
            //loadData();
            location.href = location.href;
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
            // loadData();
            location.href = location.href;
            toastr.success('Đã xóa');
          }
          else {
            $("#modal-thongtin .modal-content").html(data.html_form);
          }
        }
      });
      return false;
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
                    },
                    success: function (data) {
                        if (data.added) {
                            // $("#modal-thongtin").modal("hide");
                            toastr.error('Mã số: ' + data.maso + ' đã được thêm trước đó')
                        }
                        else
                            $("#modal-thongtin").modal("show");
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
                    "addch": {name: "Bảng chọc hút"},
                    "addcp": {name: "Bảng chuyển phôi"},
                    "adddp": {name: "Bảng đông phôi"}
                }
            },
            "sep1": "---------",
            "del": {name: "Xóa", className: "context_del"}
        }
    });

    $.contextMenu({
        selector: '.left-pick',
        trigger: 'left',
        zIndex: 100,
        callback: function (key, opt){
                    $(this).css('background-color', key);
                    var target = opt.$trigger.attr("targetchange");
                    target = '#' + target;
                    $(target).val(key);
                },
        items: {
            "#ff0000": {name: 'Đỏ'},
            "#00ff00": {name: 'Xanh lá'},
            "#0000ff": {name: 'Xanh dương'},
            "#ffff00": {name: 'Vàng'},
            "#fcf0b0": {name: 'Kem'},
            "#ffffff": {name: 'Trắng'},
            "#ffa500": {name: 'Cam'},
            "rgba(0, 0, 0, 0)": {name: 'Đã chuyển'}
        }
    });

for (var i = 0; i < 3; i++)
    for (var j = 1; j < 4; j++) {
        (function() {
            var ij = String(i) + String(j);
            $.contextMenu({
                selector: '#pick_id_label' + ij,
                trigger: 'left',
                events: {
                    show: function (options) {
                        $("ul li label input").addClass("form-control input-sm");
                        $(".okok").hover(function () {
                            $(this).css("background-color", "transparent");
                        }, function () {
                            $(this).css("background-color", "transparent");
                        });
                        $(".okok").append("<button class='btn btn-primary btn-sm' style='float: right'>Đồng ý</button>");
                        $(".context-menu-input").hover(function () {
                            $(this).css("background-color", "transparent");
                        }, function () {
                            $(this).css("background-color", "transparent");
                        });
                    }
                },
                build: function ($triggerElement, e) {
                    var loai1 = document.getElementById("id_loai" + ij + "1").value;
                    var loai2 = document.getElementById("id_loai" + ij + "2").value;
                    var loai3 = document.getElementById("id_loai" + ij + "3").value;
                    return {
                        zIndex: 100,
                        callback: function (key, opt) {
                            $(this).css('background-color', key);
                            var target = opt.$trigger.attr("targetchange");
                            target = '#' + target;
                            $(target).val(key);
                        },
                        items: {
                            "#ff0000": {name: 'Đỏ'},
                            "#00ff00": {name: 'Xanh lá'},
                            "#0000ff": {name: 'Xanh dương'},
                            "#ffff00": {name: 'Vàng'},
                            "#fcf0b0": {name: 'Kem'},
                            "#ffffff": {name: 'Trắng'},
                            "#ffa500": {name: 'Cam'},
                            "rgba(0, 0, 0, 0)": {name: 'Đã chuyển'},
                            "sep1": "---------",
                            "l00": {
                                name: "Loại 1",
                                type: "text",
                                value: loai1,
                                callback: function (key, opt) {
                                },
                                events: {
                                    keyup: function (e) {
                                        loai1 = Number(e.currentTarget.value);
                                        //window.console.log(Number(e.currentTarget.value));
                                    }
                                }
                            },
                            "l10": {
                                name: "Loại 2",
                                type: "text",
                                value: loai2,
                                callback: function (key, opt) {
                                },
                                events: {
                                    keyup: function (e) {
                                        loai2 = Number(e.currentTarget.value);
                                    }
                                }
                            },
                            "l20": {
                                name: "Loại 3",
                                type: "text",
                                value: loai3,
                                callback: function (key, opt) {
                                },
                                events: {
                                    keyup: function (e) {
                                        loai3 = Number(e.currentTarget.value);
                                    }
                                }
                            },
                            "ok": {
                                name: "",
                                callback: function (key, opt) {
                                    $("#id_loai" + ij + "1").val(loai1);
                                    $("#id_loai" + ij + "2").val(loai2);
                                    $("#id_loai" + ij + "3").val(loai3);
                                    window.console.log(ij);
                                },
                                className: "okok"
                            }
                        }
                    }
                }
            });
        })();
    }
});



$("#modal-thongtin").on("submit", ".js-trudongphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-thongtin").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-thongtin .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-thongtin").on("submit", ".js-ketquaphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-thongtin").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-thongtin .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-thongtin").on("submit", ".js-theodoiphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-thongtin").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-thongtin .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-thongtin").on("submit", ".js-truraphoi-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-thongtin").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-thongtin .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});

$("#modal-thongtin").on("submit", ".js-IVF-ex-form", function(){
    var formch = $(this);
        $.ajax({
            url: formch.attr("action"),
            data: formch.serialize(),
            type: formch.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-thongtin").modal("hide");
                    toastr.success('Xuất thành công');
                    location.href = "/quanly/download/";
                }
                else {
                  $("#modal-thongtin .modal-content").html(data.html_form);
                }
            }
        });
    return false;
});