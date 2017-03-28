
$(function () {
  $(".js-bacsi-add").click(function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-bacsi").modal("show");
      },
      success: function (data) {
        $("#modal-bacsi .modal-content").html(data.html_form);
      }
    });
  });

});

  $("#modal-bacsi").on("submit", ".js-bacsi-add-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
			$("#bacsi-table tbody").html(data.html_bacsi_preview);  // <-- Replace the table body
            $("#modal-bacsi").modal("hide");
        }
        else {
          $("#modal-bacsi .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


  $("#modal-bacsi").on("submit", ".js-bacsi-edit-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#bacsi-table tbody").html(data.html_bacsi_preview);
          $("#modal-bacsi").modal("hide");
        }
        else {
          $("#modal-bacsi .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });

    $("#modal-bacsi").on("submit", ".js-bacsi-del-form", function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#bacsi-table tbody").html(data.html_bacsi_preview);
            $("#modal-bacsi").modal("hide");
          }
          else {
            $("#modal-bacsi .modal-content").html(data.html_form);
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
                        $("#modal-bacsi").modal("show");
                    },
                    success: function (data) {
                        $("#modal-bacsi .modal-content").html(data.html_form);
                    }
                });
        },
        items: {
            "edit": {name: 'Sửa'},
            "sep1": "---------",
            "del": {name: "Xóa"}
        }
    });
});