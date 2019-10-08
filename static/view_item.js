// Michaella Schaszberger
// mls2290

function putFunction() {
    var newInput = {
        "Id": info["Id"],
        "Name": $("#name").val(),
        "Picture":$("#picture").val(),
        "Description":$("#description").val(),
        "Price" :$("#price").val(),
        "Brand":$("#brand").val(),
        "Size":$("#size").val(),
        "Type":$("#type").val(),
        "Email" :$("#email").val()}
    $.ajax({
    type: "POST",
    url: "/view_item/" + item_id-1,
    // dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(newInput),
    success: [function (result) {
        alert("You have successfully edited " + $("#name").val())
        window.location.href="http://127.0.0.1:5000/search"
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


$(document).ready(function() {
    $('#delete').click(function() {
        $.ajax({
            type: "DELETE",
            url: "/view_item/" + item_id - 1,
            contentType: "application/json; charset=utf-8",
            data: info,
            success: [function (result) {
                alert("You have successfully deleted " + info["Name"])
                console.log("success");
                location.replace("http://127.0.0.1:5000/search")


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
    });
        $('#edit').click(function () {
            $(".wrapper").empty()
            // var pic_edit = $("<img src = {{ info['Picture'] }} height='400' width='600'>")
            var name = info["Name"]
            var name_edit = $("<div style='font-size:25px;margin-bottom:10px;'> <b>Name:</b><input id='name' value ='" + info["Name"] + "' style=\"width: 300px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(name_edit)
            var picture_edit = $("<div style='font-size:25px;'> <b>Picture Link:</b><input id='picture' value ='" + info["Picture"] + "' style=\"width: 500px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(picture_edit)
            var description_edit = $("<div style='font-size:25px;'><b>Description: </b><input id='description' value ='" + info["Description"] + "' style=\"width: 300px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(description_edit)
            var price_edit = $("<div style='font-size:25px;'><b>Price: </b><input id='price' value ='" + info["Price"] + "' style=\"width: 100px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(price_edit)
            var size_edit = $("<div style='font-size:25px;'><b>Size: </b><input id='size' value ='" + info["Size"] + "' style=\"width: 100px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(size_edit)
            var brand_edit = $("<div style='font-size:25px;'><b>Brand:</b><input id='brand' value ='" + info["Brand"] + "' style=\"width: 300px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(brand_edit)
            var type_edit = $("<div style='font-size:25px;'><b>Type:</b><input id='type' value ='" + info["Type"] + "' style=\"width: 100px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(type_edit)
            var email_edit = $("<div style='font-size:25px;'><b>Email:</b><input id='email' value ='" + info["Email"] + "' style=\"width: 300px;font-size:25px;\"></input> </div><br><br>")
            $("#edit_item").append(email_edit)
            var button = $("<div><button onclick='putFunction()' style='font-size:25px;height:40px;width:80px;'>Save</button></div>")
            $("#edit_item").append(button)


       });
    $('#favorite').click(function(){
        alert("You've added this item to your favorites!");
            $.ajax({
                type: "POST",
                url: "favorites_add",
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(info),
                success: [function (result) {
                    test = result
                    console.log(result)

                }],
                error: [function (request, status, error) {
                    var error = $("<div>An error occurred!</div>")
                    $("#link").append(error)
                    console.log(request);
                    console.log(status);
                    console.log(error)
                }]
            });
        })
    });




    // $("#item_ info").empty()
    // $.each(info, function (name, value) {
    //     console.log("name ", name)
    //     var info_nugget = $("<div>" + bir + "</div>")
    //     $("#item_ info").append(info_nugget)
    // });
    // var name = $("<div> Name : " + info["Name"] + "</div>")
    // var Sci_Name = $("<div> Type : " + info["Type"] + "</div>")
    // var picture = $("<img src=''>")
    // $j('pic img').attr(src)
    // $('pic img').attr('src', info["Picture"]).show();
    // $j('pic img').attr('src', info["Picture"]).show();
    // var Description = $("<div> Description : " + info["Description"] + "</div>")
    // var Price = $("<div> Price : " + info["Price"] + "</div>")
    // var Consv_Status = $("<div> Brand : " + info["Brand"] + "</div>")
    // var Size = $("<div> Size : " + info["Size"] + "</div>")
    // var Email = $("<div> Email : " + info["Email"] + "</div>")

    // $("#item_ info").append(name)
    // $("#item_ info").append(Sci_Name)
    // $("#pic").append(picture)
    // $("#item_ info").append(Description)
    // $("#item_ info").append(Price)
    // $("#item_ info").append(Consv_Status)
    // $("#item_ info").append(Size)
    // $("#item_ info").append(Email)


