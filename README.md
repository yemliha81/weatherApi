<b>Installation</b>

git clone https://github.com/yemliha81/weatherApi.git <br>
cd weatherApi <br>
docker-compose up --build <br>
 <br> <br>
After running these commands, app should be running at 127.0.0.1:8000
 <br> <br>
<b>Sample cURL request</b> <br>
curl --location --request GET '127.0.0.1:8000/get_temperature?location=istanbul' \
--header 'Authorization: fdxf523dxfdfd23242d34xf3ddx423'
 <br> <br>
<b>Sample response</b> <br> <br>
{
    "city_name": "istanbul",
    "current_temperature": 9.15,
    "today_min_temperature": 6.19,
    "today_max_temperature": 8.6,
    "this_week_min_temperature": 1.66,
    "this_week_max_temperature": 15.96
}
