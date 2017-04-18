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
            toastr.success('Thêm thành công');
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
            toastr.success('Thêm thành công');
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
            toastr.success('Thêm thành công');
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
                    "addch": { name: "Bảng chọc hút" },
                    "addcp": { name: "Bảng chuyển phôi" },
                    "adddp": { name: "Bảng đông phôi" }
                }
            },
            "sep1": "---------",
            "del": {name: "Xóa", className:"context_del"}
        }
    });


    function count() {
        var loai1 = Number(document.getElementById("id_loai001").value)
            + Number(document.getElementById("id_loai101").value)
            + Number(document.getElementById("id_loai201").value);
        var loai2 = Number(document.getElementById("id_loai002").value)
            + Number(document.getElementById("id_loai102").value)
            + Number(document.getElementById("id_loai202").value);
        var loai3 = Number(document.getElementById("id_loai003").value)
            + Number(document.getElementById("id_loai103").value)
            + Number(document.getElementById("id_loai203").value);
        $('input[id="loai1"]').val(loai1);
        $('input[id="loai2"]').val(loai2);
        $('input[id="loai3"]').val(loai3);
    }

    $.contextMenu({
        selector: '.left-pick0',
        trigger: 'left',
        events: {
            show : function(options){
                $("ul li label input").addClass("form-control input-sm");
                $(".okok").hover(function(){
                    $(this).css("background-color", "transparent");
                    }, function(){
                    $(this).css("background-color", "transparent");
                });
                $(".okok").append("<button class='btn btn-primary btn-sm' style='float: right'>Đồng ý</button>");
                $(".context-menu-input").hover(function(){
                    $(this).css("background-color", "transparent");
                    }, function(){
                    $(this).css("background-color", "transparent");
                });
            }
        },
        build: function($triggerElement, e){
            var loai001 = document.getElementById("id_loai001").value;
            var loai002 = document.getElementById("id_loai002").value;
            var loai003 = document.getElementById("id_loai003").value;
            return {
                zIndex: 100,
                callback: function (key, opt){
                            $(this).css('background-color', key);
                            var target = opt.$trigger.attr("targetchange");
                            target = '#' + target;
                            $(target).val(key);
                            return false;
                        },
                items: {
                    "#ff0000": {name: 'Đỏ'},
                    "#00ff00": {name: 'Xanh lá'},
                    "#0000ff": {name: 'Xanh dương'},
                    "#ffff00": {name: 'Vàng'},
                    "#fcfbe3": {name: 'Kem'},
                    "#ffffff": {name: 'Trắng'},
                    "#ffa500": {name: 'Cam'},
                    "rgba(0, 0, 0, 0)": {name: 'Đã chuyển'},
                    "sep1": "---------",
                    "l00": {
                        name: "Loại 1",
                        type: "text",
                        value: loai001,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai001 = Number(e.currentTarget.value);
                                //window.console.log(Number(e.currentTarget.value));
                            }
                        }
                    },
                    "l10": {
                        name: "Loại 2",
                        type: "text",
                        value: loai002,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai002 = Number(e.currentTarget.value);
                            }
                        }
                    },
                    "l20": {
                        name: "Loại 3",
                        type: "text",
                        value: loai003,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai003 = Number(e.currentTarget.value);
                            }
                        }
                    },
                    "ok": {
                        name: "",
                        callback: function (key, opt) {
                            $("#id_loai001").val(loai001);
                            $("#id_loai002").val(loai002);
                            $("#id_loai003").val(loai003);
                            count();
                        },
                        className: "okok"
                    }
                }
            }
        }
    });

    $.contextMenu({
        selector: '.left-pick1',
        trigger: 'left',
        events: {
            show : function(options){
                $("ul li label input").addClass("form-control input-sm");
                $(".okok").hover(function(){
                    $(this).css("background-color", "transparent");
                    }, function(){
                    $(this).css("background-color", "transparent");
                });
                $(".okok").append("<button class='btn btn-primary btn-sm' style='float: right'>Đồng ý</button>");
                $(".context-menu-input").hover(function(){
                    $(this).css("background-color", "transparent");
                    }, function(){
                    $(this).css("background-color", "transparent");
                });
            }
        },
        build: function($triggerElement, e){
            var loai101 = document.getElementById("id_loai101").value;
            var loai102 = document.getElementById("id_loai102").value;
            var loai103 = document.getElementById("id_loai103").value;
            $("ul li label input").addClass("form-control input-sm");
            return {
                zIndex: 100,
                callback: function (key, opt){
                            $(this).css('background-color', key);
                            var target = opt.$trigger.attr("targetchange");
                            target = '#' + target;
                            $(target).val(key);
                            return false;
                        },
                items: {
                    "#ff0000": {name: 'Đỏ'},
                    "#00ff00": {name: 'Xanh lá'},
                    "#0000ff": {name: 'Xanh dương'},
                    "#ffff00": {name: 'Vàng'},
                    "#fcfbe3": {name: 'Kem'},
                    "#ffffff": {name: 'Trắng'},
                    "#ffa500": {name: 'Cam'},
                    "rgba(0, 0, 0, 0)": {name: 'Đã chuyển'},
                    "sep1": "---------",
                    "l00": {
                        name: "Loại 1",
                        type: "text",
                        value: loai101,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai101 = Number(e.currentTarget.value);
                                //window.console.log(Number(e.currentTarget.value));
                            }
                        }
                    },
                    "l10": {
                        name: "Loại 2",
                        type: "text",
                        value: loai102,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai102 = Number(e.currentTarget.value);
                            }
                        }
                    },
                    "l20": {
                        name: "Loại 3",
                        type: "text",
                        value: loai103,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai103 = Number(e.currentTarget.value);
                            }
                        }
                    },
                    "ok": {
                        name: "",
                        callback: function (key, opt) {
                            $("#id_loai101").val(loai101);
                            $("#id_loai102").val(loai102);
                            $("#id_loai103").val(loai103);
                            count();
                        },
                        className: "okok"
                    }
                }
            }
        }
    });

    $.contextMenu({
        selector: '.left-pick2',
        trigger: 'left',
        events: {
            show : function(options){
                $("ul li label input").addClass("form-control input-sm");
                $(".okok").hover(function(){
                    $(this).css("background-color", "transparent");
                    }, function(){
                    $(this).css("background-color", "transparent");
                });
                $(".okok").append("<button class='btn btn-primary btn-sm' style='float: right'>Đồng ý</button>");
                $(".context-menu-input").hover(function(){
                    $(this).css("background-color", "transparent");
                    }, function(){
                    $(this).css("background-color", "transparent");
                });
            }
        },
        build: function($triggerElement, e){
            var loai201 = document.getElementById("id_loai201").value;
            var loai202 = document.getElementById("id_loai202").value;
            var loai203 = document.getElementById("id_loai203").value;
            return {
                zIndex: 100,
                callback: function (key, opt){
                            $(this).css('background-color', key);
                            var target = opt.$trigger.attr("targetchange");
                            target = '#' + target;
                            $(target).val(key);
                            return false;
                        },
                items: {
                    "#ff0000": {name: 'Đỏ'},
                    "#00ff00": {name: 'Xanh lá'},
                    "#0000ff": {name: 'Xanh dương'},
                    "#ffff00": {name: 'Vàng'},
                    "#fcfbe3": {name: 'Kem'},
                    "#ffffff": {name: 'Trắng'},
                    "#ffa500": {name: 'Cam'},
                    "rgba(0, 0, 0, 0)": {name: 'Đã chuyển'},
                    "sep1": "---------",
                    "l00": {
                        name: "Loại 1",
                        type: "text",
                        value: loai201,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai201 = Number(e.currentTarget.value);
                                //window.console.log(Number(e.currentTarget.value));
                            }
                        }
                    },
                    "l10": {
                        name: "Loại 2",
                        type: "text",
                        value: loai202,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai202 = Number(e.currentTarget.value);
                            }
                        }
                    },
                    "l20": {
                        name: "Loại 3",
                        type: "text",
                        value: loai203,
                        callback: function (key, opt) {
                        },
                        events: {
                            keyup: function(e) {
                                loai0203 = Number(e.currentTarget.value);
                            }
                        }
                    },
                    "ok": {
                        name: "",
                        callback: function (key, opt) {
                            $("#id_loai201").val(loai201);
                            $("#id_loai202").val(loai202);
                            $("#id_loai203").val(loai203);
                            count();
                        },
                        className: "okok"
                    }
                }
            }
        }
    });



    $.contextMenu({
        selector: '.right-pick',
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
            "#fcfbe3": {name: 'Kem'},
            "#ffffff": {name: 'Trắng'},
            "#ffa500": {name: 'Cam'},
            "rgba(0, 0, 0, 0)": {name: 'Đã chuyển'}
        }
    });
});

