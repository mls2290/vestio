$('.btn.grid').click(function() {
  if (!$(this).hasClass("active")) {
    $(this).addClass("active");
    $('.results-wrapper .grid_12').removeClass("grid_12").addClass("grid_3");
    $('.wrapper .results').addClass("grid-view-active");
    if ($(".btn.list").hasClass("active")) {
      $(".btn.list").removeClass("active");
      $('.wrapper .results').removeClass("list-view-active");
    }
  }
});
