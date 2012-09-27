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

$("#hide_minor_sports").click(function(){
	$("#minor_sports").hide("slow")
            });

$("#show_minor_sports").click(function(){
	$("#minor_sports").show("slow")
            });

$("#hide_meetings_sports").click(function(){
	$("#meeting_sports").hide("slow")
            });

$("#show_meetings_sports").click(function(){
	$("#meeting_sports").show("slow")
            });

$("#hide_tournaments").click(function(){
	$("#tournament_table").hide("slow")
            });

$("#show_tournaments").click(function(){
	$("#tournament_table").show("slow")
            });



