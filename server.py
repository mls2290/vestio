# Michaella Schaszberger
# mls2290
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)

curr_id = 35
link_returned = ""

my_likes = []

clothes_data = [
    {
        "Id": 1,
        "Name": "peplum top",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70222678_2528104177247302_5084416399930032128_n.jpg?_nc_cat=111&_nc_oc=AQnqWr-FmN-MZ-KkXbMHDNTyaR3TZ7XmOYswCPYVcz0LTKVf9HRkLqIIp1co1sX04pI&_nc_ht=scontent-lga3-1.xx&oh=9b19b89566676c6b987464462ba61849&oe=5DF8EB81",
        "Description": "potential work clothes!",
        "Price": 10,
        "Brand": "anthropologie",
        "Size": "4",
        "Type": "top work",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "mls2290@columbia.edu"
    },
    {
        "Id": 2,
        "Name": "purple dress",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70177383_2410752845657144_879760119997399040_n.jpg?_nc_cat=106&_nc_oc=AQlnOQQk__fLo-2SC7HXUn0Y7BomBW_GgjXyqwjZvD4jOC_jL1lDtgcyzYdy1w7X_PM&_nc_ht=scontent-lga3-1.xx&oh=a97b15edaf17980ba4cc9007cb88636f&oe=5E0E44D9",
        "Description": "Clothes & Fan",
        "Price": 25,
        "Brand": "Zara",
        "Size": "small",
        "Type": "dress formal",
        "Profile_Picture": "https://previews.123rf.com/images/michaeljung/michaeljung1406/michaeljung140600063/28971399-gorgeous-indian-female-university-student-portrait.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 3,
        "Name": "MATT & NAT vegan leather heels in ruby size 40",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69805300_1806806206118029_7655510026634657792_n.jpg?_nc_cat=103&_nc_oc=AQlwggQLoMTvl83y3Gwz99Ran9sMShSWs-d5Xm4Qej3g7lRMvs3k2urHEInLAF7ZTJg&_nc_ht=scontent-lga3-1.xx&oh=8aacc4a906d660ed17f25a5c50b542c4&oe=5DF13EB2",
        "Description": "MATT & NAT vegan leather heels in ruby size 40 (size 9 or so, would fit 8.5, slightly small on my wide 9) - $30 (og 110)",
        "Price": 30,
        "Brand": "MATT & NAT",
        "Size": "size 9 or so, would fit 8.5, slightly small on my wide 9",
        "Type": "heels work",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"

    },
    {
        "Id": 4,
        "Name": "Alo Yoga Airbrush Leggings in Dove Grey",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69942462_10216386181459485_5158741745290182656_n.jpg?_nc_cat=103&_nc_oc=AQl-dRlwYCtscMYpSB5cwsvLr0i2QJgFqd3ONGmCTDdneji4pGaK6i9vQnMZgQKzfXM&_nc_ht=scontent-lga3-1.xx&oh=f03b47e5175f24075766136906bde430&oe=5E11088A",
        "Description": "Alo Yoga Airbrush Leggings in Dove Grey - XS, worn once, originally $110, selling for $25 OBO",
        "Price": 25,
        "Brand": "Alo Yoga",
        "Size": "XS",
        "Type": "bottoms",
        "Profile_Picture": "https://cdn7.dissolve.com/p/D430_33_649/D430_33_649_1200.jpg",
        "Seller": "Kelsey",
        "Response_Time": "1 hour",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 5,
        "Name": "J. Crew white cami, size 0, new with tag",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70174028_10158103057461412_3870153755789885440_n.jpg?_nc_cat=108&_nc_oc=AQlGDw36yDNSIPNahK4KmbZA_yZN-FRjINAHISOQczQIq2csg7vg8IIJNPJJzccsAKE&_nc_ht=scontent-lga3-1.xx&oh=592f6ff5c95843d422956e454186bd70&oe=5E03EEA2",
        "Description": "J. Crew Factory off-white cami, size 0, never worn / new with tag. The color just didn’t look right on me and I never got around to returning it",
        "Price": 20,
        "Brand": "J.Crew",
        "Size": "0",
        "Type": "top work",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 6,
        "Name": "Floral Zara Dress",
        "Picture": "https://static.zara.net/photos///2019/I/0/1/p/7727/042/300/3/w/560/7727042300_1_1_1.jpg?ts=1562156033623",
        "Description": "very cute, but doesn't fit",
        "Price": 35,
        "Brand": "Zara",
        "Size": "M",
        "Type": "dress work formal",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 7,
        "Name": "hand-made earrings!",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69574240_10220948758008005_932372975452160_n.jpg?_nc_cat=102&_nc_oc=AQmKDPVLaU-8ydhG4hyUXGjBWhsIiAKJoMbkpRh0nsQxxp-5gWT7J3qFTZ1xrSyhzJs&_nc_ht=scontent-lga3-1.xx&oh=ada0afbfc1dd1d36513dad544d6408f2&oe=5DF9EF86",
        "Description": "Selling these cute hand-painted earrings:) $12 per pair, can deliver on campus!",
        "Price": 12,
        "Brand": "Maude House",
        "Size": "one size fits all",
        "Type": "earrings work",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 8,
        "Name": "Abercrombie Slim Overalls! (Size 26/2R)",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69878266_2262856564045080_1293943238192791552_n.jpg?_nc_cat=103&_nc_oc=AQl_voOFzSYKYpPEFAegbfYnSI7wakGU0Tk0tY3OPWvKyCgIvRa82X60H-R_EmaQhtQ&_nc_ht=scontent-lga3-1.xx&oh=702f1a61889b949254a2317384029cdd&oe=5DFD5120",
        "Description": "Retails for $50. Open to negotiation, WORN ONCE",
        "Price": 35,
        "Brand": "Abercrombie",
        "Size": "26/2R",
        "Type": "bottoms",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 9,
        "Name": "Zara Polka Dot Romper (worn once) - S/M - $25",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70091168_2939579276071100_1639472536817238016_n.jpg?_nc_cat=111&_nc_oc=AQmDQng_dD4leCa9NWroFlkTbxTra1hnYHFFyVz-7g93ROuVEPcS5ZzzrMfEjS5tOAA&_nc_ht=scontent-lga3-1.xx&oh=126c3e8ca2f2902d49b2c09078099ea2&oe=5E105D45",
        "Description": "I live in Brooklyn but will be on campus WEDNESDAY EVENING! (I can also do pickup in Bushwick). Price negotiable, dm me for details!",
        "Price": 25,
        "Brand": "Zara",
        "Size": "S/M",
        "Type": "romper",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 10,
        "Name": "Topshop Blouse (like new) - S - $10",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70284719_2939579756071052_4455943864254988288_n.jpg?_nc_cat=111&_nc_oc=AQkS-Zko9EQcVN5MfQiGCh8DS3B35Kg4G-euXOwQoUAFlrJyHWAzyeD_LnJI9KDsFog&_nc_ht=scontent-lga3-1.xx&oh=dec236b331d49a20ae2f02ad4d27215c&oe=5E069F94",
        "Description": "I live in Brooklyn but will be on campus WEDNESDAY EVENING! (I can also do pickup in Bushwick). Price negotiable, dm me for details!",
        "Price": 10,
        "Brand": "Topshop",
        "Size": "S",
        "Type": "top work",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 11,
        "Name": "Zara green leather overall dress - S/M - $15",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69806927_2939579566071071_8289211723647287296_n.jpg?_nc_cat=111&_nc_oc=AQkQl8tRp5iIJtdM_2fK5tpYRknHiU_i1dni7LyjLGxBNOTWlE-9VoamrJDo7uLrQnk&_nc_ht=scontent-lga3-1.xx&oh=ad8d19907a35f6dd13b69d1e91c9618b&oe=5E05806E",
        "Description": "I live in Brooklyn but will be on campus WEDNESDAY EVENING! (I can also do pickup in Bushwick). Price negotiable, dm me for details!",
        "Price": 15,
        "Brand": "Zara",
        "Size": "S/M",
        "Type": "dress",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 12,
        "Name": "Arc’teryx Gear",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70219008_10219692147159462_1625076794283524096_n.jpg?_nc_cat=103&_nc_oc=AQkm9IbFY4-VXgmY_89CzWwygbIceOUhFe0OpsHSYFD0rkqTWw2BHy86O9vafD5tQUk&_nc_ht=scontent-lga3-1.xx&oh=1cbb8dc3b64d4ec575c54ac81462242f&oe=5E0EF322",
        "Description": "Selling stuff for my boyfriend - everything is in perfect condition and prices are very negotiable!",
        "Price": 250,
        "Brand": "Arc’teryx",
        "Size": "Large",
        "Type": "jacket",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 13,
        "Name": "Floral Aritizia",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70319933_2378734762367481_4197185553688428544_n.jpg?_nc_cat=105&_nc_oc=AQlqxYc7dV62qlr7S72x9HFO-SyMrwOcixgZ3sRrtQoTreG0MYN_14npFLgPeB0mJQM&_nc_ht=scontent-lga3-1.xx&oh=239704e0b2b641b7c635f23baa80696e&oe=5DF5C72B",
        "Description": "originally 110 - selling 40. Selling clothes appropriate for internships, interviews and work!. Discounted Aritzia, J Crew, Loft- ***OBO",
        "Price": 40,
        "Brand": "Aritzia",
        "Size": "XS",
        "Type": "top work",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 14,
        "Name": "JCrew Rust Shirt",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69767926_2378734815700809_1537470314827481088_n.jpg?_nc_cat=111&_nc_oc=AQm2NJy4C-pfljo5j0MlLel56fvCA-7xUnqkMuascV153aeTQJiDXLRHLQRoJnTDWII&_nc_ht=scontent-lga3-1.xx&oh=96f48e2600097219ee53fa7a608c468e&oe=5E0B19CA",
        "Description": "originally 80 - selling 30. Selling clothes appropriate for internships, interviews and work!",
        "Price": 30,
        "Brand": "J Crew",
        "Size": "XXS",
        "Type": "top work",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 15,
        "Name": "Thrifted/H&M Wednesday Addams Dress",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/71031075_462805851233968_2540154773953314816_n.jpg?_nc_cat=108&_nc_oc=AQlxQ5zewEWculGfu11pZ0uqJ5-Bd5Ut0JAVOE0yCTmoWm5-RwvyKpUDtNySuyyi2M8&_nc_ht=scontent-lga3-1.xx&oh=a85277bcaffe588c0d14101ab9154b87&oe=5DFC248F",
        "Description": "Selling some things I either don't wear anymore or have pretty much never worn. Prices negotiable! I live in Plimpton but can meet on campus. Thrifted/H&M Wednesday Addams dress - tried to spice up my wardrobe to no avail. Never worn outside. Size 2, $7",
        "Price": 7,
        "Brand": "H&M",
        "Size": "2",
        "Type": "dress",
        "Profile_Picture": "https://cdn7.dissolve.com/p/D430_33_649/D430_33_649_1200.jpg",
        "Seller": "Kelsey",
        "Response_Time": "1 hour",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 16,
        "Name": "Purple print Levi's skinny jeans",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69879849_462805911233962_5659927762597576704_n.jpg?_nc_cat=110&_nc_oc=AQlYKK4CFDiQe00iLg89VLZHWElyMs4byZh1SZU67xJCst-fHqjNJp2QKEs6bNbpLng&_nc_ht=scontent-lga3-1.xx&oh=16f11515d7b60acbda9131606e63ae5a&oe=5E119E0C",
        "Description": "Purple print Levi's skinny jeans - bought these a loooong time ago and never wore them. Beautiful print but I could never fit into them. SIze 25. Originally $100 (yikes), asking for $35 but we can talk about that. ",
        "Price": 35,
        "Brand": "Levi's",
        "Size": "25",
        "Type": "bottom",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 17,
        "Name": "Denim Skirt from Topshop",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69659859_2481361231912381_8444494793060384768_n.jpg?_nc_cat=108&_nc_oc=AQnWVQEGvMbDrBriV5b7jpCgf7txWEiNDFf96KSCeso47rQ_gxfOT3hRp4Xy_QCA7-Q&_nc_ht=scontent-lga3-1.xx&oh=2b9bfefcdac467cd91ff02c3893a104a&oe=5DFE52DB",
        "Description": "Message me if you are interested! The size for all items is S/38 European.",
        "Price": 10,
        "Brand": "Top Shop",
        "Size": "S/38 European",
        "Type": "bottom",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 18,
        "Name": "Ripped Zara Jeans",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70011588_2481361171912387_8626078236444459008_n.jpg?_nc_cat=101&_nc_oc=AQl3eLG1zFfnvIy0wUZB7F1TaW-DuQWGHs1upcJh9cmZZ6nKuNoiELqJNav5yFIJOss&_nc_ht=scontent-lga3-1.xx&oh=4d358b139932e6b79807a157c676684e&oe=5DFF5AB5",
        "Description": "Message me if you are interested! The size for all items is S/38 European. ",
        "Price": 15,
        "Brand": "Zara",
        "Size": "S/38 European",
        "Type": "bottom",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 19,
        "Name": "Bershka Pants",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69702924_2481361158579055_789184340671070208_n.jpg?_nc_cat=111&_nc_oc=AQkHJJZsyVwV3MWomNxMjwt92wjNGnAzls1M0wBvml_lTZZxEZkSaejJk_6yaDmE88A&_nc_ht=scontent-lga3-1.xx&oh=2628842d943f004130b075d655d7177a&oe=5E12559D",
        "Description": "Message me if you are interested! The size for all items is S/38 European. ",
        "Price": 15,
        "Brand": "Bershka",
        "Size": "S",
        "Type": "bottom",
        "Profile_Picture": "https://previews.123rf.com/images/michaeljung/michaeljung1406/michaeljung140600063/28971399-gorgeous-indian-female-university-student-portrait.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 20,
        "Name": "Rag and Bone jean shorts",
        "Picture": "https://is4.revolveassets.com/images/p4/n/d/RAGA-WN32_V1.jpg",
        "Description": "super cute, just doesn't fit me anymore. perfect for summer!",
        "Price": 25,
        "Brand": "Rag and Bone",
        "Size": "37",
        "Type": "bottom",
        "Profile_Picture": "https://previews.123rf.com/images/michaeljung/michaeljung1406/michaeljung140600063/28971399-gorgeous-indian-female-university-student-portrait.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 21,
        "Name": "Bright green I.AM.GIA top",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69936175_1353237988159821_2250746052049108992_n.jpg?_nc_cat=107&_nc_oc=AQnRg_jvaGzO4-hhNnY1Q4rB2TNTdRVOHKdViQ1rDrV8dz17jbx5GUbe2Qc2MOkxfW4&_nc_ht=scontent-lga3-1.xx&oh=21484635c71a0dcb9fe339ae69fcdc4a&oe=5E0CDE6F",
        "Description": "Only worn once size XS. Price is negotiable.",
        "Price": 50,
        "Brand":"I.AM.GIA",
        "Size": "XS",
        "Type": "top",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 22,
        "Name": "Urban outfitters bodysuit",
        "Picture": "https://s7g10.scene7.com/is/image/UrbanOutfittersEU/0147265642009_065_b?$xlarge$&hei=900&qlt=80&fit=constrain",
        "Description": "only worn once size S. price is negotiable",
        "Price": 30,
        "Brand": "Urban Outfitters",
        "Size": "S",
        "Type": "bodysuit",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 23,
        "Name": "Beautiful Green Lesportsac backpack - pristine condition!",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70486587_10214155741107683_7357649320193032192_n.jpg?_nc_cat=108&_nc_oc=AQl9KrLQasCy5CwAZqI0BXJtn3IMZAB4At7wZtbN86T2kEdBaO_9HFodF2IwhIrPzPQ&_nc_ht=scontent-lga3-1.xx&oh=7a78b8f05a638e9c2007020cab3b8890&oe=5DF21E25",
        "Description": "Beautiful Green vintage Lesportsac backpack in perfect condition, like new! Asking $30 or best offer",
        "Price": 30,
        "Brand":"Lesportsac",
        "Size": "one size",
        "Type": "bag",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 24,
        "Name": "BRAND NEW Hunter Rain boots!",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70009375_2643225379054390_8720284315402895360_n.jpg?_nc_cat=101&_nc_oc=AQkFMqBGTpav-JIayMTsuHbNPpVeMtiZ6MgMuQ4cJJ-J08O-uIleigOeEFvzZKGOC7Y&_nc_ht=scontent-lga3-1.xx&oh=2fdf68c6b75d6c96d3f31a8e923182e5&oe=5DF09A53",
        "Description": "I just bought this brand new pair of black Hunter tall Rain boots ! I never worn it outside. Literally still in its original box. I only took it out to try on but it’s too tight on my calves and I lost the receipt to return it. Let me know if you’re interested and want them! I can drop it off to you too if you’re in the barnard area.",
        "Price": 90,
        "Brand": "Hunter",
        "Size": "US: 7, UK: 8, EU: 38",
        "Type": "shoes",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 25,
        "Name": "Brand New Old Navy Mid-Rise, Tall, Straight-Cut Jeans",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/70007548_1452059324959407_4959028282877018112_n.jpg?_nc_cat=108&_nc_oc=AQnt1KtEpaD6aDtmQ3gStfI8nJHNEvy9DcD_MpwPBiLWGYzK25AjFA2OuFWCebqYWKo&_nc_ht=scontent-lga3-1.xx&oh=d6f4b310f3004ff5aa079380550d8e83&oe=5DFA28A4",
        "Description": "I bought these jeans last year and just never got around to wearing them. They’re brand new and still have the tags on them!",
        "Price": 15,
        "Brand": "Old Navy",
        "Size": "4, Tall",
        "Type": "bottoms",
        "Profile_Picture": "https://previews.123rf.com/images/michaeljung/michaeljung1406/michaeljung140600063/28971399-gorgeous-indian-female-university-student-portrait.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 26,
        "Name": "Formal wear (Heels)",
        "Picture": "https://www.lulus.com/images/product/xlarge/1735832_285602.jpg?w=560",
        "Description": "Meet at Plimpton",
        "Price": 25,
        "Brand": "Bradelles",
        "Size": "7",
        "Type": "shoes",
        "Profile_Picture": "https://previews.123rf.com/images/michaeljung/michaeljung1406/michaeljung140600063/28971399-gorgeous-indian-female-university-student-portrait.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",

        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 27,
        "Name": "J Crew Top",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69988739_1359770710841234_6016098061741195264_n.jpg?_nc_cat=104&_nc_oc=AQluf21tI_EPlnQww7fLbFLgrizWNBbvBKuWYvhl6jo-5tEdotwy3RKZ--Km7U_YSBY&_nc_ht=scontent-lga3-1.xx&oh=5fbd843cb2fd5b192783770838b727ab&oe=5DF2A6F6",
        "Description": "",
        "Price": 15,
        "Brand": "J Crew",
        "Size": "S",
        "Type": "top",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 28,
        "Name": "Reformation Dress",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69696404_2692507380760948_4993430915083403264_n.jpg?_nc_cat=105&_nc_oc=AQkm7s7Gn_0SoqZDktkOYTri7InwJoKDRt2O8HHng12-K2r9eBzLe8GTJtFXdAbfc70&_nc_ht=scontent-lga3-1.xx&oh=e9371b93cf5fd22fa47cf7928f334785&oe=5E0C10A7",
        "Description": "Prices in photos, everything OBO, PM with any questions! I am at my apartment until 3 PM today for people to come try on; more clothing available that isn’t on this post.",
        "Price": 40,
        "Brand": "Reformation",
        "Size": "L",
        "Type": "dress work",
        "Profile_Picture": "https://media.istockphoto.com/photos/female-college-student-with-books-outdoors-picture-id813019744?k=6&m=813019744&s=612x612&w=0&h=KOVCwuaSUHgHdJDVNwhDwURiGadbg9AAP2xrPH76vXw=",
        "Seller": "Elizabeth",
        "Response_Time": "6 hours",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 29,
        "Name": "Thrifted vintage MiuMiu wool mini-skirt",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69706493_2692103334134686_2922747729081794560_n.jpg?_nc_cat=107&_nc_oc=AQkoRlhSl8VLuIM5HDU6puIQ7jAMPSGiT1Q3cmlIy-B7Rziw56JaIps0GdBdT7pFF90&_nc_ht=scontent-lga3-1.xx&oh=d6ddd3190ceb708dd4be6266b0dca60d&oe=5E10F8ED",
        "Description": "Prices in photos, everything OBO, PM with any questions! I am at my apartment until 3 PM today for people to come try on; more clothing available that isn’t on this post.",
        "Price": 35,
        "Brand": "MiuMiu",
        "Size": "S",
        "Type": "skirt work",
        "Profile_Picture": "https://cdn7.dissolve.com/p/D430_33_649/D430_33_649_1200.jpg",
        "Seller": "Kelsey",
        "Response_Time": "1 hour",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 30,
        "Name": "red wrap dress",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69728229_2487155734846190_8679368455486439424_n.jpg?_nc_cat=102&_nc_oc=AQl_grNYEClqzR9nM4fbTYxnrwcKuxredKH9_CboIlV1BFhpQoxTH0KPLWKboj-R9xE&_nc_ht=scontent-lga3-1.xx&oh=10e0075506b485f059b9e3f8d8908c34&oe=5E03914D",
        "Description": "Clothes!! Buy them!!",
        "Price": 8,
        "Brand": "Brandy Melville",
        "Size": "S",
        "Type": "dress work",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 31,
        "Name": "Blue and white floral H&M Skirt",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69493181_2468142626580473_1688256141164806144_n.jpg?_nc_cat=110&_nc_oc=AQkQ1f2FccL2rkK9gDs_xXsE6UsNFeePGxIaty9UlUuUVUYh7B3-1VEopiSyaJ3JuhE&_nc_ht=scontent-lga3-1.xx&oh=3197b0701aabdeed5e2df91dcd85e8d4&oe=5E3D4A5A",
        "Description": "All in great condition! You are welcome to try on! Prices negotiable 🙂 lmk if you have any questions",
        "Price": 5,
        "Brand": "H&M",
        "Size": "S",
        "Type": "skirt",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Response_Time": "2 hours",
        "Seller": "Maddy",

        "Email": "jane.doe@columbia.edu"
    },    {
        "Id": 32,
        "Name": "Black Lululemon sweatpants",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69795120_2468142669913802_3504446095218442240_n.jpg?_nc_cat=101&_nc_oc=AQljpFtIL9uhwqqXKnlzFeWRQzz0UrhBvdn1FH39tICgRHwImkPv1N-NMOJOcaSOTHk&_nc_ht=scontent-lga3-1.xx&oh=f1fc3b617dbd0aeba65ffbfdf7cb5543&oe=5E0F06E1",
        "Description": "All in great condition! You are welcome to try on! Prices negotiable 🙂 lmk if you have any questions",
        "Price": 50,
        "Brand": "Lululemon",
        "Size": "2",
        "Type": "bottoms",
        "Profile_Picture": "https://cdn7.dissolve.com/p/D430_33_649/D430_33_649_1200.jpg",
        "Seller": "Kelsey",
        "Response_Time":"1 hour",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 33,
        "Name": "Faux leather jacket with floral embroidery BlankNYC",
        "Picture": "https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/69470198_2468142979913771_6166779666402115584_n.jpg?_nc_cat=111&_nc_oc=AQnUjgRxbjy5jpFdFV0DZLzsO4ARVMRyo-SZnIqDlhqwKDj2-Abiv2zYFQG-hfoJlvk&_nc_ht=scontent-lga3-1.xx&oh=6a6560e1869fe142db91258e851999de&oe=5E113C21",
        "Description": "All in great condition! You are welcome to try on! Prices negotiable 🙂 lmk if you have any questions",
        "Price": 35,
        "Brand": "BlankNYC",
        "Size": "XS",
        "Type": "jacket",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 34,
        "Name": "blazer",
        "Picture": "data:image/jpeg;base64,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",
        "Description": "great for interviews",
        "Price": 15,
        "Brand": "lulus",
        "Size": "S",
        "Type": "blazer work",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",
        "Email": "jane.doe@columbia.edu"
    },
    {
        "Id": 35,
        "Name": "madewell blazer",
        "Picture": "https://i.s-madewell.com/is/image/madewell/AA305_WQ6063_d1?wid=700&hei=889&fmt=jpeg&fit=crop&qlt=75,1&resMode=bisharp&op_usm=0.5,1,5,0",
        "Description": "can be casual or for work",
        "Price": 20,
        "Brand": "madewell",
        "Size": "M",
        "Type": "blazer",
        "Profile_Picture": "https://previews.123rf.com/images/stockbroker/stockbroker1408/stockbroker140802531/31051048-portrait-of-female-university-student-outdoors-on-campus.jpg",
        "Seller": "Maddy",
        "Response_Time": "2 hours",
        "Email": "jane.doe@columbia.edu"
    },

]
dictionary = dict()
for item in clothes_data:
    dictionary[item["Id"]] = item


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    global clothes_data

    if request.method == 'GET':
        return render_template('add_page.html', clothes_data=clothes_data, curr_id=curr_id)

    if request.method == 'POST':

        json_data = request.get_json()
        id = json_data["Id"]
        name = json_data["Name"]
        picture = json_data["Picture"]
        description = json_data["Description"]
        Price = json_data["Price"]
        brand = json_data["Brand"]
        Size = json_data["Size"]
        type = json_data["Type"]
        Email = json_data["Email"]
        seller = json_data["Seller"]
        response_time = json_data["Response_Time"]
        profile_pic = json_data["Profile_Picture"]


        new_entry = {
            "Id": id,
            "Name": name,
            "Picture": picture,
            "Description": description,
            "Price": Price,
            "Brand": brand,
            "Size": Size,
            "Type": type,
            "Email": Email,
            "Seller":seller,
            "Response_Time": response_time,
            "Profile_Picture":profile_pic}


        #insert at start of list
        clothes_data.append(new_entry)

        # link_returned = "http://127.0.0.1:5000/view_item/" + curr_id

        return jsonify(clothes_data=clothes_data)

@app.route('/view_item/favorites_add', methods=['GET', 'POST'])
def favorite_item():
    global clothes_data

    if request.method == 'GET':
        return render_template('favorite.html', my_likes=my_likes, curr_id=curr_id)

    if request.method == 'POST':

        json_data = request.get_json(force=True)
        print(json_data["Id"])
        print("test")

        id = json_data["Id"]
        name = json_data["Name"]
        picture = json_data["Picture"]
        description = json_data["Description"]
        Price = json_data["Price"]
        type = json_data["Type"]
        brand = json_data["Brand"]
        Size = json_data["Size"]
        Email = json_data["Email"]
        seller = json_data["Seller"]

        # response_time = json_data["Response_Time"]
        # profile_pic = json_data["Profile_Picture"]


        new_entry = {
            "Id": id,
            "Name": name,
            "Picture": picture,
            "Description": description,
            "Price": Price,
            "Brand": brand,
            "Size": Size,
            "Type": type,
            "Email": Email,
            "Seller":seller,
        }


        #insert at start of list
        my_likes.append(new_entry)

        return jsonify(my_likes=my_likes)

@app.route('/search',methods=['GET', 'POST'])
def search():
    global clothes_data
    global my_likes
    global curr_id

    if request.method == 'POST':
        json_data = request.get_json()
        Id = json_data["Id"]

        name = json_data["Name"]

        picture = json_data["Picture"]
        description = json_data["Description"]
        Price = json_data["Price"]
        brand = json_data["Brand"]
        Size = json_data["Size"]
        type = json_data["Type"]
        Email = json_data["Email"]
        seller = json_data["Seller"]
        # response_time = json_data["Response_Time"]
        # profile_pic = json_data["Profile_Picture"]


        curr_id += 1

        new_entry = {
            "Id": curr_id,
            "Name": name,
            "Picture": picture,
            "Description": description,
            "Price": Price,
            "Brand": brand,
            "Size": Size,
            "Type": type,
            "Email": Email,
            "Seller": seller,

            }

        # insert at start of list
        my_likes.append(new_entry)

        # link_returned = "http://127.0.0.1:5000/view_item/" + curr_id

        return jsonify(my_likes=my_likes)

    if request.method == 'GET':
        return render_template('search_results.html', clothes_data=clothes_data)

@app.route('/favorites',methods=['GET', 'POST'])
def favorite():
    return render_template('favorite.html',my_likes=my_likes)

@app.route('/resultsTest',methods=['GET', 'POST'])
def resultsTest():
    return render_template('results.html')

@app.route('/view_item/<item_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def view_item(item_id=None):
    global clothes_data
    global curr_id
    index = int(item_id)
    index -=1
    info = clothes_data.pop(index)
    clothes_data.insert(index,info)
    if request.method == "DELETE":
        cloth = clothes_data.pop(index)
        print(cloth)
    if request.method == "POST":
        info = clothes_data.pop(index)
        json_data = request.get_json()
        info["Id"] = json_data["Id"]
        info["Name"] = json_data["Name"]
        info["Picture"] = json_data["Picture"]
        info["Description"] = json_data["Description"]
        info["Price"] = json_data["Price"]
        info["Brand"] = json_data["Brand"]
        info["Size"] = json_data["Size"]
        info["Type"] = json_data["Type"]
        info["Email"] = json_data["Email"]

        clothes_data.insert(index, info)

    return render_template('view_item.html', info=info, item_id=item_id, clothes_data=clothes_data )


if __name__ == '__main__':
    app.run()
