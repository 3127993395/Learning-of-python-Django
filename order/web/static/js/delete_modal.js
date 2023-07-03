$(function () {
    bindDeleteEvent();
    bindConfirmDeleteEvent();
});

function bindDeleteEvent() {
    $(".btn-delete").click(function () {
        $("#deleteError").empty();

        $("#deleteModal").modal('show');
        let cid = $(this).attr('cid');
        DELETE_ID = cid;
    });

    $("#btnCancelDelete").click(function () {
        $("#deleteModal").modal('hide');
    })
}

function bindConfirmDeleteEvent() {
    $("#btnConfirmDelete").click(function () {

        //ajax发送请求  /xxx/xxx/xxx?cid=...
        $.ajax({
            url: DELETE_URL,
            type: "GET",
            data: {cid: DELETE_ID},
            dataType: "JSON",
            success: function (res) {
                if (res.status) {
                    //删除成功
                    //方式一 页面刷新
                    //location.reload();
                    //方式二 找到当前页面中数据行进行删除
                    $("tr[row-id='" + DELETE_ID + "']").remove();
                    //隐藏对话框(如果时方法一就不需要，因为自动刷新)
                    $("#deleteModal").modal('hide');
                } else {
                    //删除失败
                    $("#deleteError").text(res.detail);
                }
            }
        })
    })
}