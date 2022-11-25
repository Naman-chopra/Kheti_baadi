

const formData = new FormData();
formData.append('farm_id', 10);
fetch("http://127.0.0.1:8000/Fert/", {
    method: 'POST',
    body: formData,
}).then((res) => {
    var res = res.json();
    console.log(res)
    return res
    
}).then((res)=> {
        
        var data2 = res;
        document.getElementById("fertilizer").innerHTML = data2['fert'];
        
});



fetch("http://127.0.0.1:8000/getData", {
    method: 'GET',
}).then(res => res.json()).then(json => {
    var data = json
    document.getElementById("potassium").innerHTML = data['potassium'];
    document.getElementById("nitrogen").innerHTML = data['nitrogen'];
    document.getElementById("phosphorous").innerHTML = data['phosphorous'];
});

fetch("http://127.0.0.1:8000/rain", {
     method: 'GET',
    
}).then(res => res.json()).then(json => {
    
    var weather = json;
    console.log(json['status'])
    if (weather['status'] == "Rain"){
        document.getElementById("rain-rain").innerHTML = "It will Rain soon, watering the crops is not suggested";
    }
    else {
        document.getElementById("rain-rain").innerHTML = "No Rain Expected, Give them water!!";
        
    }

})



    
    