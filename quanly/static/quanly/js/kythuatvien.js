function loadData(){
   /* $('#kythuatvien-table').DataTable({
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
      "sLengthMenu": 'Số lượng hiển thị: <select name="kythuatvien-table_length" aria-controls="kythuatvien-table" class="form-control input-sm"">'+
        '<option value="10">10</option>'+
        '<option value="30">30</option>'+
        '<option value="50">50</option>'+
        '<option value="-1">Tất cả</option>'+
        '</select>'
    },
    "columnDefs": [ {
        "targets": [2],
        "type" : "datetime"

        "render": function (data) {
            if (data !== null) {
                var time = new Date(data);
                time = time.getHours()+':'+time.getMinutes();
                return time;
            } else {
                return "";
            }
        }
    } ]
   });*/
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
  $(".js-kythuatvien-add").click(function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-kythuatvien").modal("show");
      },
      success: function (data) {
        $("#modal-kythuatvien .modal-content").html(data.html_form);
      }
    });
  });

});

  $("#modal-kythuatvien").on("submit", ".js-kythuatvien-add-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#kythuatvien-table').DataTable().destroy();
			$("#kythuatvien-table tbody").html(data.html_kythuatvien_preview);  // <-- Replace the table body
            $("#modal-kythuatvien").modal("hide");
            loadData();
            toastr.success('Thêm thành công');
        }
        else {
          $("#modal-kythuatvien .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


  $("#modal-kythuatvien").on("submit", ".js-kythuatvien-edit-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#kythuatvien-table').DataTable().destroy();
			$("#kythuatvien-table tbody").html(data.html_kythuatvien_preview);  // <-- Replace the table body
            $("#modal-kythuatvien").modal("hide");
            loadData();
            toastr.success('Sửa thành công');
        }
        else {
          $("#modal-kythuatvien .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

    $("#modal-kythuatvien").on("submit", ".js-kythuatvien-del-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $('#kythuatvien-table').DataTable().destroy();
			$("#kythuatvien-table tbody").html(data.html_kythuatvien_preview);  // <-- Replace the table body
            $("#modal-kythuatvien").modal("hide");
            loadData();
            toastr.success('Đã xóa');
          }
          else {
            $("#modal-kythuatvien .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    });



$(function() {
    $.contextMenu({
        selector: '.context-button',
        trigger: 'left',
        callback: function (key, opt) {
            if (opt.$trigger.attr("data-url"))
                $.ajax({
                    url: opt.$trigger.attr("data-url") + key,
                    type: 'get',
                    dataType: 'json',
                    beforeSend: function () {
                        $("#modal-kythuatvien").modal("show");
                    },
                    success: function (data) {
                        $("#modal-kythuatvien .modal-content").html(data.html_form);
                    }
                });
        },
        items: {
            "edit": {name: 'Sửa'},
            "sep1": "---------",
            "del": {name: "Xóa", className:"context_del"}
        }
    });
});