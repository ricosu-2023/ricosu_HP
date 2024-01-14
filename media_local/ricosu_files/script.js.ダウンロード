/*jslint browser: true*/
/*global $ */

/* SPメニュー */
$(function () {
  "use strict";
  $(".menu").click(function () {
    $(this).toggleClass("menuOpen").next().slideToggle();
  });

  $("#gnav a").click(function () {
    $("#menu").removeClass("menuOpen");
    $("#gnav").hide();
  });

  $(window).scroll(function () {
    if ($(this).scrollTop() > 768) {
      $("#header").addClass('top');
    } else {
      $("#header").removeClass('top');
    }
  });
});

//#pagelink
$(function () {
  "use strict";
  var headerHight = 80;
  $('a[href^=#]').click(function () {
    var href = $(this).attr("href");
    var target = $(href === "#" || href === "" ? 'html' : href);
    var position = target.offset().top - headerHight;
    $("html, body").animate({
      scrollTop: position
    }, 550, "swing");
    return false;
  });
});

$(document).ready(function () {
  $("#pagetop").hide();
  $(window).on("scroll", function () {
    if ($(this).scrollTop() > 100) {
      $("#pagetop").fadeIn("fast");
    } else {
      $("#pagetop").fadeOut("fast");
    }
    scrollHeight = $(document).height(); //ドキュメントの高さ 
    scrollPosition = $(window).height() + $(window).scrollTop(); //現在地 
    footHeight = $("footer").innerHeight(); //footerの高さ（＝止めたい位置）
    if (scrollHeight - scrollPosition <= footHeight) { //ドキュメントの高さと現在地の差がfooterの高さ以下になったら
      $("#pagetop").css({
        "position": "absolute", //pisitionをabsolute（親：wrapperからの絶対値）に変更
        "bottom": footHeight + 20 //下からfooterの高さ + 20px上げた位置に配置
      });
    } else { //それ以外の場合は
      $("#pagetop").css({
        "position": "fixed", //固定表示
        "bottom": "20px" //下から20px上げた位置に
      });
    }
  });
  $('#pagetop').click(function () {
    $('body,html').animate({
      scrollTop: 0
    }, 400);
    return false;
  });
});
