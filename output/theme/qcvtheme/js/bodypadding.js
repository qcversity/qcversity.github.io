$(document).ready(function(){
    $('body').css('padding-top', $('.navbar').height()+'px');
});

$(document).ready(function(){
    let navbarHeight = $('.navbar').height();
    let desiredMargin = 50; // The desired margin top in pixels

    // Adjust the top padding of the body based on the navbar's height
    $('body').css('padding-top', navbarHeight + 'px');

    // Set the top margin of the content
    $('.content').css('margin-top', desiredMargin + 'px');
});