// Michaella Schaszberger
// mls2290
// UI Design, HW8
var displayitems = function(data){
    //empty old data
    $("#link").empty()

    //insert all new data
    $.each(data, function(i, datum){
        var new_name= $("<div>"+datum["Name"]+"</div>")
        // console.log("DATUM ",datum["Name"])
        $("#link").append(new_name)
    })
}

var displayJson = function(data){
    $.each(data, function () {
        $.each(this, function (name, value) {
            console.log(name + '=' + value);
        });
    });
}
var test;
var saveitem = function (name, picture, description, price, brand, size, type, email, seller, profpic) {
    // id_num = id_num + 1

    var data_to_save =
        {"Id":id_num,
        "Name": name,
        "Picture": picture,
        "Description": description,
        "Price": price,
        "Brand": brand,
        "Size": size,
        "Type": type,
        "Email": email,
        "Seller": seller,
        "Response_Time": "1 hour",
        "Profile_Picture":profpic
        }
    $.ajax({
        type: "POST",
        url: "add_item",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_to_save),
        success: [function (result) {
            var all_data = result["data"];
            test = result
            console.log(result)

        }],
        error: [function (request, status, error) {
            var error = $("<div>An error occurred!</div>")
            $("#link").append(error)
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error)
        }]
    });
}

$(document).ready(function(){
    $("#link").empty()
    id_num = curr_id

    $("#submit").click(function(){
        var name = $.trim($("#name").val());
        var picture = $.trim($("#picture").val());
        var description = $.trim($("#description").val());
        var Price = $.trim($("#Price").val());
        var brand = $.trim($("#brand").val());
        var Size = $.trim($("#Size").val());
        var type = $.trim($("#type").val());
        var Email = $.trim($("#email").val());
        var seller = $.trim($("#seller").val());
        var profpic = $.trim($("#seller_picture").val());


        var flag = "False"

        // for error check -- can't enter an empty entry
        if (name.length <=0 || description.length<=0 || Price.length<=0 || brand.length <=0|| Size.length <=0|| type.length <=0|| Email.length <=0|| seller.length <=0|| profpic.length <=0){
            flag = "True"
            // // $("#link").empty()
            var error = $("<div>Please fill out all of the fields before you submit!</div>")
            $("#link").append(error)
        }
        saveitem(name,picture,description,Price,brand,Size,type,Email,seller,profpic);
        $("#name").val("")
        $("#picture").val("")
        $("#description").val("")
        $("#Price").val("")
        $("#brand").val("")
        $("#Size").val("")
        $("#type").val("")
        $("#Email").val("")
        $("#seller").val("")
        $("#seller_picture").val("")

        $("#name").focus()
        id_num = id_num + 1
        // displayitems(clothes_data)
        // var new_name= $("<div>"+"http://127.0.0.1:5000/view_item/"+curr_id+"</div>")

        if ($.isNumeric(id_num) && flag == "False") {
            $("#link").empty()
            var success = $("<div style='font-size:25px;font-weight:bold;'>" + "You've successfully added a item entry! Below is the link to view your entry:" + "</div><br>")
            $("#link").append(success)
            var urllink=$("<div style='font-size:25px;font-weight:bold;'><a href='http://127.0.0.1:5000/view_item/"+ id_num +"'>http://127.0.0.1:5000/view_item/" + id_num + "</a></div>")
            $("#link").append(urllink)
        }
        else{
            $("#link").empty()
            alert("An error occurred! Make sure you fill out all of the fields before you submit!");
            // var error = $("<div style='font-size:25px;font-weight:bold;'>An error occurred! Make sure you fill out all of the fields before you submit!</div>")
            // $("#link").append(error)
        }

            //empty old data
        // displayJson(clothes_data)
        // //insert all new data
        // var success= $("<div>" + "You've successfully added a item entry! Below is the link to view your entry:" + "</div><br>")
        // var urllink=$("<div><a href='url'>" + "http://127.0.0.1:5000/view_item/" + curr_id + "</a></div>")
        // $("#link").append(success)
        // $("#link").append(link)
    })
});