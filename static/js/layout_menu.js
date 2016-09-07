/**
 * Created by hellowgw on 16/8/22.
 */


/** left menu button **/

function SvnBtn(){
    window.location.href="/svn";
}

function PackageBtn(){
    window.location.href="/package";
}

function RollBack(){
    window.location.href="/rollback";
}

/** env choice select **/

//config production line select option
$('#id_PushTarget').change(function(){
    var s = $(this).val();
    if(s ==1){
        var option_str ='<option>'+'----请选择----'+'</option>';
        $('#production-line option').remove();
        $('#production-line').append(option_str);
        $('#production option').remove();
        $('#production').append(option_str);
    }else{
        $.ajax({
        url:"/get_pro_info/",
        data:{target_id:s},
        type:'GET',
        success:function(arg){
            var callbac_dic= $.parseJSON(arg);
                $('#production-line option').remove();
                    var option_str ='<option>'+'----请选择----'+'</option>';
                        $('#production-line').append(option_str);
            $.each(callbac_dic,function(i){
                var option_str ='<option value="'+i+'">'+callbac_dic[i]+'</option>';
                    $('#production-line').append(option_str)
            });
        } //end callback function
    });//end ajax
    }//end else
    var option_str ='<option>'+'----请选择----'+'</option>';
        $('#production-line option').remove();
        $('#production-line').append(option_str);
        $('#production option').remove();
        $('#production').append(option_str);
});

//config production select option
$('#production-line').change(function(){
    var s = $(this).val();
    if(s =='----请选择----'){
        $('#production option').remove();
        var option_str ='<option>'+'----请选择----'+'</option>';
            $('#production').append(option_str);
    }else{
        $.ajax({
            url:"/get_pro_info/",
            data:{production_line_id:s},
            type:'GET',
            success:function(arg){
            var callbac_dic= $.parseJSON(arg);
                $('#production option').remove();
            var option_str ='<option>'+'----请选择----'+'</option>';
                $('#production').append(option_str);
                $.each(callbac_dic,function(i){
                    var option_str ='<option value="'+i+'">'+callbac_dic[i]+'</option>';
                    $('#production').append(option_str)
            });
        }
    });
    }

});
