$(document).ready(function() {
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
            "sLengthMenu": 'Số lượng hiển thị: <select name="thongtin-table_length" aria-controls="thongtin-table" class="form-control input-sm"">' +
            '<option value="10">10</option>' +
            '<option value="30">30</option>' +
            '<option value="50">50</option>' +
            '<option value="-1">Tất cả</option>' +
            '</select>'
        }
    });
});