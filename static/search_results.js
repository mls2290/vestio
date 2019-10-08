// Michaella Schaszberger
// mls2290

var checkDB = function (data, searchQ){
    var check = "False"
    var field = ""

    $.each(clothes_data, function(i, item){
        check = "False"
       if(item["Price"].toString(10).indexOf(searchQ)>=0 && check === "False") {
           if($("#high").val() != ""){
               if(item["Price"] <= $("#high").val()){
                   if($("#low").val() != "") {
                       if (item["Price"] >= $("#low").val()) {
                           check = "True"
                       }
                   }
                   else{
                      check = "True"

                   }
               }
           }
           else {
               (item["Price"].toString(10).indexOf(searchQ) >= 0 && check == "False")
               {
                   check = "True"
               }
           }
        }

        if(document.getElementById("formal").checked === true){
            console.log("formal");
            if(item["Type"].toLowerCase().indexOf("formal")>=0 && check == "False") {
                check = "True"
             }
        }
        if(document.getElementById("work").checked === true){
            console.log("work");

            if(item["Type"].toLowerCase().indexOf("work")>=0 && check == "False") {
                check = "True"
             }
        }
        else {
           if(item["Price"].toString(10).indexOf(searchQ)>=0 && check === "False") {
               if($("#high").val() != ""){
                   if(item["Price"] <= $("#high").val()){
                       check = "True"
                   }
               }
               else {
                   (item["Price"].toString(10).indexOf(searchQ) >= 0 && check == "False")
                   {
                       check = "True"
                   }
               }
            }
            if (item["Name"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                console.log(item["Name"])
                check = "True"
            }
            if (item["Description"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                check = "True"
            }
            // if (item["Price"].toString(10).indexOf(searchQ) >= 0 && check == "False") {
            //     check = "True"
            // }

            if (item["Brand"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                check = "True"
            }
            if (item["Size"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                check = "True"

            }
            if (item["Type"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                check = "True"
            }
            if (item["Email"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                check = "True"
            }
            if (item["Seller"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                check = "True"
            }
            if (item["Response_Time"].toLowerCase().indexOf(searchQ) >= 0 && check == "False") {
                check = "True"
            }
        }
        if(check == "True") {
            // var container = $("<div class='container' style='border-style: solid;background-color:lightskyblue'>");
            // $("#search_results").append(container);
            // var picture = $("<div align='left' id = 'entry'><img src='" + item["Picture"] + "' style='height:300px;width:400px;'></div>");
            // $("#search_results").append(picture);

            var name_item = item['Name'];
            var post = $("<div class='container' style='border-style:solid; border-color:lightgrey;'>" +
                "<div class='row'></div>" +
                // "<div class='col-md-2'>" +
                "<div class='col-md-5'>" +
                "<div align='left' id = 'entry' style='font-size:40px;margin-left: 0px;margin-bottom:-35px;margin-top:20px;'><a href='http://127.0.0.1:5000/view_item/" + item["Id"] + "' style='font-size:40px;margin-top: 20px; margin-left:15px; margin-bottom:-10px; color:black;'><b>" + item["Name"] + "</b></a></div>" +
                "<br><div align='right' id = 'entry' style='font-size:30px;margin-right: 25px;'><b>$</b>" + item["Price"] + "</div><br>" +
                "<div align='center' id = 'entry'><img src='" + item["Picture"] + "' style='height:300px;width:400px;margin-left: -10px;margin-top: -20px;' border='2'></div>" +
                "<div align='center' id = 'entry' style='font-size:22px;margin-left: -15px;margin-top:10px;'>" + item["Description"] + "</div><br>" +
                "<div align='center' id = 'entry' style='font-size:26px;margin-left: -15px;margin-bottom:20px;margin-top:-20px;'><b>size </b>" + item["Size"] + "</div></div>" +


                // 'item['Name'], item['Picture'], item['Description'], item['Price'],item['Brand'], item['Size'], item['Type'], item['Email'], item['Seller'], item['Response_Time'],item['Profile_Picture']
                "<div class='col-md-7' align='right' style='margin-left:-20px;'>" +
                "<div align='right' id = 'entry' style='font-size:22px;margin-top:10px;'><b>sold by </b>" + item["Seller"] + "</div><br>" +
                "<div align='right' style='font-size:25px; margin-top:-10px;margin-bottom:-20px;'><a href=mailto:" + item["Email"] + "><button>email seller</button></a></div>" +

                "<div align = 'right' style='margin-top:20px;'><iframe src=\"https://calendar.google.com/calendar/b/1/embed?height=300&amp;wkst=1&amp;bgcolor=%23ffffff&amp;ctz=America%2FNew_York&amp;src=NjQ1ZnE5ZHFobWVrNjQ5dmZzcmlmOGowaXNAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ&amp;color=%237CB342&amp;showNav=1&amp;showTabs=0&amp;title=my%20availability&amp;mode=WEEK&amp;showDate=1&amp;showCalendars=1&amp;showPrint=0&amp;showTz=0\" style=\"border-width:0\" width=\"420\" height=\"300\" frameborder=\"0\" scrolling=\"no\"></iframe>" +

                // "<div align='right' id = 'entry'><img src='" + item["Profile_Picture"] + "' style='height:300px;width:375px;'></div><br>" +
                // "<div align='right' id = 'entry' style='font-size:22px;'>" + item["Email"] + "</div><br>" +
                "<div align='right' id = 'entry' style='font-size:22px;'><b>average response time: </b>" + item["Response_Time"] + "</div></div>");


                // "<div align='right' style='font-size:30px; padding-top:10px;margin-bottom:20px;'><button type='button' id="fave" onclick=\"favoriteFn()\";>add to favorites</button></div></div>");

          // var id = item['Id'];
          //   var name_item = item['Name'];
          //   var description = item['Description'];
          //   var email = item['Email'];
          //   var seller = item['Seller'];
          //   var response_time = item['Response_Time'];
          //   var price = item['Price'];
          //   var size = item['Size'];
          //   var brand = item['Brand'];
          //   var picture = item['Picture'];
          //   var prof_pic = item['Profile_Picture']
            $(".grid-container").empty();

            $("#search_results").append(post);

            var space = $("<div><br><br></div>")
            $("#search_results").append(space);

            // var description = $("<div id = 'entry' style='font-size:22px;'><b>Description: </b>" + item["Description"] + "</div><br>");
            // $("#search_results").append(description);
            // var sci_name = $("<div id = 'entry' style='font-size:22px;'><b>Price: $</b>" + item["Price"] + "</div><br>");
            // $("#search_results").append(sci_name)
            // var Size = $("<div id = 'entry' style='font-size:22px;'><b>Size: </b>" + item["Size"] + "</div><br><br>");
            // $("#search_results").append(Size);

        }
    });
    if (check == "False"){
        var error = $("<div>Sorry! No results were found for your search.</div>")
        $("#search_results").append(error)
    }
};




var displayResults = function(data, searchResult){
    console.log("Search ", searchResult)
    var new_name= $("<div id = 'entry'>"+data+"</div>")
    $("#search_results").append(new_name)

    // $.each(data, function(i, datum){
    //     var new_name= $("<div>"+datum[searchResult]+"</div>")
    //     $("#search_results").append(new_name)
    // })
};



$(document).ready(function() {
    $("#search_results").empty()
    $("#fave").click(function(){

    })
    //search_results stores all of the search results after search_submit has been clicked
    $("#search_submit").click(function() {
        $("#search_results").empty()
        var result = $("#searchQ").val()
        //searchQ is the input value from user
        if($.trim($("#searchQ").val()) == ""){
            var error = $("<div>An error occurred! Make sure you enter a search query!</div>")
            $("#search_results").append(error)
        }
        else {
            var searchquery = $.trim($("#searchQ").val().toLowerCase());
            $("#searchQ").focus()
            $("#searchQ").val("")
            var feedback = $("<div>Your search results for '" + result + "':</div><br>")
            $("#search_results").append(feedback)
            checkDB(clothes_data, searchquery)
        }
    });
    //help from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_trigger_button_enter
    var input = document.getElementById("searchQ");
    input.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        $("#search_results").empty()
        var result = $("#searchQ").val()
        //searchQ is the input value from user
        if ($.trim($("#searchQ").val()) == "") {
            var error = $("<div>An error occurred! Make sure you enter a search query!</div>")
            $("#search_results").append(error)
        } else {
            var searchquery = $.trim($("#searchQ").val().toLowerCase());
            $("#searchQ").focus()
            $("#searchQ").val("")
            var feedback = $("<div style='font-size:25px;font-weight:bold;'>Your search results for '" + result + "':</div><br>")
            $("#search_results").append(feedback)
            checkDB(clothes_data, searchquery)
        }
    }
    });
    $("#search_results").empty()


        // displayNames(clothes_data)
        // $.each(clothes_data, function(i, item){
        //     var name= $("<div>"+datum[i]["Name"]+"</div>")
        //     $("#search_results").append(name)
        //     var sci_name= $("<div>"+datum[i]["Type"]+"</div>")
        //     $("#search_results").append(sci_name)
        //     var sci_name= $("<div>"+datum[i]["Picture"]+"</div>")
        //     $("#search_results").append(sci_name)
        // });

            // $.each(clothes_data, function(i, item){
            //     var check = "False"
            //     if(item["Name"].toLowerCase().indexOf(searchquery)>=0 && check == "False") {
            //         var new_name = $("<div>" + item["Name"] + "</div>")
            //         $("#search_results").append(new_name)
            //         check = "True"
            //     }
            // });

});