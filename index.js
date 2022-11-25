

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
        document.getElementById("fertilizer").innerHTML = data2['fertilizer'];
        
});



// fetch("http://127.0.0.1:8000/getData", {
//     method: 'GET',
// }).then(res => res.json()).then(json => {
//     var data = json
//     document.getElementById("potassium").innerHTML = data['potassium'];
//     document.getElementById("nitrogen").innerHTML = data['nitrogen'];
//     document.getElementById("phosphorous").innerHTML = data['phosphorous'];
// });





    
    