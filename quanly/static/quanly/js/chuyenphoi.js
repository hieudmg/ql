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


    $("#modal-chuyenphoi").on("submit", ".js-chuyenphoi-edit-form", function(){
    var formcp = $(this);
    $.ajax({
      url: formcp.attr("action"),
      data: formcp.serialize(),
      type: formcp.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_chuyenphoi_preview);  // <-- Replace the table body
            $("#modal-chuyenphoi").modal("hide");
            loadData();
            toastr.success('Sửa thành công');
        }
        else {
          $("#modal-chuyenphoi .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


    $("#modal-chuyenphoi").on("submit", ".js-chuyenphoi-del-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_chuyenphoi_preview);  // <-- Replace the table body
            $("#modal-chuyenphoi").modal("hide");
            loadData();
            toastr.success('Đã xóa');
          }
          else {
            $("#modal-chuyenphoi .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    });


    $.contextMenu({
        selector: '.context-chuyenphoi',
        trigger: 'left',
        zIndex: 100,
        items: {
            "editcp": {name: 'Sửa',
                    callback: function (key, opt){
                            if (opt.$trigger.attr("data-url"))
                                $.ajax({
                                    url: opt.$trigger.attr("data-url") + key,
                                    type: 'get',
                                    dataType: 'json',
                                    beforeSend: function () {
                                        $("#modal-chuyenphoi-setup").removeClass("modal-lg");
                                        $("#modal-chuyenphoi").modal("show");
                                    },
                                    success: function (data) {
                                        $("#modal-chuyenphoi .modal-content").html(data.html_form);
                                    }
                                });
                            }},
            "sep1": "---------",
            "delcp": {name: "Xóa",
                    callback: function (key, opt){
                            if (opt.$trigger.attr("data-url"))
                                $.ajax({
                                    url: opt.$trigger.attr("data-url") + key,
                                    type: 'get',
                                    dataType: 'json',
                                    beforeSend: function () {
                                        $("#modal-chuyenphoi-setup").removeClass("modal-lg");
                                        $("#modal-chuyenphoi").modal("show");
                                    },
                                    success: function (data) {
                                        $("#modal-chuyenphoi .modal-content").html(data.html_form);
                                    }
                                });
                            },
            className:"context_del"}
        }
    });
