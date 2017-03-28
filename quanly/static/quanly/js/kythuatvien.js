
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
			$("#kythuatvien-table tbody").html(data.html_kythuatvien_preview);  // <-- Replace the table body
            $("#modal-kythuatvien").modal("hide");
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
          $("#kythuatvien-table tbody").html(data.html_kythuatvien_preview);
          $("#modal-kythuatvien").modal("hide");
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
            $("#kythuatvien-table tbody").html(data.html_kythuatvien_preview);
            $("#modal-kythuatvien").modal("hide");
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
            "del": {name: "Xóa"}
        }
    });
});