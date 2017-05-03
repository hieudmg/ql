var table;

function loadData(){
    table = $('#thongtin-table').DataTable({
    "order": [8, 'asc'],
        columnDefs: [
            { orderable: false, targets: [0, 1, 2, 3, 4, 5, 6] }
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
      "timeOut": "4400",
      "extendedTimeOut": "300",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
    }
});


    $("#modal-dongphoi").on("submit", ".js-dongphoi-edit-form", function(){
    var formdp = $(this);
    $.ajax({
      url: formdp.attr("action"),
      data: formdp.serialize(),
      type: formdp.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_dongphoi_preview);  // <-- Replace the table body
            $("#modal-dongphoi").modal("hide");
            loadData();
            toastr.success('Sửa thành công');
        }
        else {
          $("#modal-dongphoi .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


    $("#modal-dongphoi").on("submit", ".js-dongphoi-del-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $('#thongtin-table').DataTable().destroy();
            $("#thongtin-table tbody").html(data.html_dongphoi_preview);  // <-- Replace the table body
            $("#modal-dongphoi").modal("hide");
            loadData();
            toastr.success('Đã xóa');
          }
          else {
            $("#modal-dongphoi .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    });


    $.contextMenu({
        selector: '.context-dongphoi',
        trigger: 'left',
        zIndex: 100,
        items: {
            "editdp": {name: 'Sửa',
                    callback: function (key, opt){
                            if (opt.$trigger.attr("data-url"))
                                $.ajax({
                                    url: opt.$trigger.attr("data-url") + key,
                                    type: 'get',
                                    dataType: 'json',
                                    beforeSend: function () {
                                        $("#modal-dongphoi-setup").removeClass("modal-lg");
                                        $("#modal-dongphoi").modal("show");
                                    },
                                    success: function (data) {
                                        $("#modal-dongphoi .modal-content").html(data.html_form);
                                    }
                                });
                            }},
            "sep1": "---------",
            "deldp": {name: "Xóa",
                    callback: function (key, opt){
                            if (opt.$trigger.attr("data-url"))
                                $.ajax({
                                    url: opt.$trigger.attr("data-url") + key,
                                    type: 'get',
                                    dataType: 'json',
                                    beforeSend: function () {
                                        $("#modal-dongphoi-setup").removeClass("modal-lg");
                                        $("#modal-dongphoi").modal("show");
                                    },
                                    success: function (data) {
                                        $("#modal-dongphoi .modal-content").html(data.html_form);
                                    }
                                });
                            },
            className:"context_del"}
        }
    });

$.fn.dataTable.ext.search.push(
    function( settings, data, dataIndex ) {
        var min = parseInt( $('#min-date').val(), 10 );
        var max = parseInt( $('#max-date').val(), 10 );
        var age = parseFloat( data[8] ) || 0; // use data for the age column

        return ( isNaN(min) && isNaN(max) ) ||
            ( isNaN(min) && age <= max ) ||
            ( min <= age && isNaN(max) ) ||
            ( min <= age && age <= max );

    }
);

$(document).ready(function() {

    // Event listener to the two range filtering inputs to redraw on input
    $('#min-date, #max-date').keyup( function() {
        table.draw();
        var min = $('#min-date').val();
        var max = $('#max-date').val();

    } );
} );