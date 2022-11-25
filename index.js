
fetch("http://127.0.0.1:8000/Fert/", {
    mode: "no-cors",
    method: 'POST',
    Headers: {
        Accept: 'application.json',
        'Content-Type': 'application/json'
    }
    // body: JSON.stringify({ farmId: 10 })
}).then(res => res.json()).then(json => {
    var data2 = json;
    document.getElementById("fertilizer").innerHTML = data2['fertilizer'];
});



// fetch("http://127.0.0.1:8000/getData", {
//     mode: "no-cors",
//     Method: 'GET',
//     Headers: {
//         Accept: 'application.json',
//         'Content-Type': 'application/json'
//     }
// }).then(res => res.json()).then(json => {
//     var data = json
//     document.getElementById("potassium").innerHTML = data['potassium'];
//     document.getElementById("nitrogen").innerHTML = data['nitrogen'];
//     document.getElementById("phosphorous").innerHTML = data['phosphorous'];
// });





    
    