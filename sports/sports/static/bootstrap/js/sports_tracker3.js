$(function(){
        $('.carousel').carousel('pause');
    });

$("#carousel_group_A").click(function(){
        var group_A = 0;
        $('.carousel').carousel(group_A);
        $('.carousel').carousel('pause');
        return false;
    });


$("#carousel_group_B").click(function(){
        var group_B = 1;
        $('.carousel').carousel(group_B);
        $('.carousel').carousel('pause');
        return false;
    });

$(function(){
        $('.nav-tabs').button('toggle');
    });

$("#hide_major_sports").click(function(){
        $("#major_sports").hide("slow")
            });

$("#show_major_sports").click(function(){
        $("#major_sports").show("slow")
            });