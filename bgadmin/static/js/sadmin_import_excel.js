/**
 * Created by Administrator on 2017/6/16 0016.
 */
var BLG = window.BLG || {};
BLG.sadmin_import = function ($) {

    $(document).ready(function () {

        $(document).on("click","#import_btn",function(){
            BLG.sadmin_import.import_user();
        });

    });

    return{
        // 接口定义
        import_user:function(){
            console.log("-----------");
            var form_data = new FormData($("#import_excel_form")[0]);
            $.ajax({
                url: "/bgadmin/import_excel/",
                type: 'POST',
                data: form_data,
                dataType: 'json',
                cache: false,
                contentType: false,
                processData: false,
                success: function (data) {
                   if(data.status==1){
                       alert("导入成功");
                   }else{
                       alert("导入失败");
                   }
                },
                error: function () {
                    alert("网络异常，稍后刷新重试");
                }
            });
        }
    }

}($);