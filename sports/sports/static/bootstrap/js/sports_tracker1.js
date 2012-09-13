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
