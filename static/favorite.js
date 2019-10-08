var show_items = function (data) {
    var field = ""
    $.each(my_likes, function (i, item) {
        var post = $("<div class='container' style='border-style:solid; border-color:lightgrey;'>" +
                "<div class='row'></div>" +
                // "<div class='col-md-2'>" +
                "<div class='col-md-5'>" +
                "<div align='left' id = 'entry' style='font-size:40px;margin-left: 0px;margin-bottom:-35px;margin-top:20px;'><a href='http://127.0.0.1:5000/view_item/" + item["Id"] + "' style='font-size:40px;margin-top: 20px; margin-left:15px; margin-bottom:-10px; color:black;'><b>" + item["Name"] + "</b></a></div><br>" +
                "<br><div align='right' id = 'entry' style='font-size:30px;margin-right: 25px;'><b>$</b>" + item["Price"] + "</div><br>" +
                "<div align='center' id = 'entry'><img src='" + item["Picture"] + "' style='height:300px;width:400px;margin-left: -10px;margin-top: -20px;' border='2'></div>" +
                "<div align='center' id = 'entry' style='font-size:22px;margin-left: -15px;margin-top:10px;'>" + item["Description"] + "</div><br>" +
                "<div align='center' id = 'entry' style='font-size:26px;margin-left: -15px;margin-bottom:20px;margin-top:-20px;'><b>size </b>" + item["Size"] + "</div></div>" +


                //
                "<div class='col-md-7' align='right' style='margin-left:-20px;'>" +
                "<div align='right' id = 'entry' style='font-size:22px;margin-top:10px;'><b>sold by </b>" + item["Seller"] + "</div><br>" +
                "<div align='right' style='font-size:25px; margin-top:-10px;margin-bottom:-20px;'><a href='mailto:mls2290@columbia.edu' style='color:black;'><button>email seller</button></a></div>" +

                "<div align = 'right' style='margin-top:20px;'><iframe src=\"https://calendar.google.com/calendar/b/1/embed?height=300&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=America%2FNew_York&amp;src=NjQ1ZnE5ZHFobWVrNjQ5dmZzcmlmOGowaXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%237CB342&amp;showNav=1&amp;showTabs=0&amp;title=my%20availability&amp;mode=WEEK&amp;showDate=1&amp;showCalendars=1&amp;showPrint=0&amp;showTz=0\" style=\"border-width:0\" width=\"420\" height=\"300\" frameborder=\"0\" scrolling=\"no\"></iframe>"

                // "<div align='right' id = 'entry'><img src='" + item["Profile_Picture"] + "' style='height:300px;width:375px;'></div><br>" +
                // "<div align='right' id = 'entry' style='font-size:22px;'>" + item["Email"] + "</div><br>" +
                );
        $("#results").append(post);
    });
}

$(document).ready(function() {
    $("#results").empty();
    console.log(my_likes);
    show_items(my_likes);
});

