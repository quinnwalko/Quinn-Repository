var $tbody = document.querySelector("tbody");
var $Input = document.querySelector("#search");

var $searchButton1 = document.querySelector("#datetime");
var $searchButton2 = document.querySelector("#city");
var $searchButton3 = document.querySelector("#state");
var $searchButton4 = document.querySelector("#country");
var $searchButton5 = document.querySelector("#shape");

var $searchButton0 = document.querySelector("#reset");
$searchButton0.addEventListener("click", reset);


$searchButton1.addEventListener("click", datetime);
$searchButton2.addEventListener("click", city);
$searchButton3.addEventListener("click", state);
$searchButton4.addEventListener("click", country);
$searchButton5.addEventListener("click", shape);

var filter = dataSet;

renderTable();

function reset()

{
    $Input.value = "";
    renderTable();
}

function renderTable()

{
    $tbody.innerHTML = "";
    for (var i = 0; i < filter.length; i++)
    
    {
        var address = filter[i];
        var fields = Object.keys(address);
        var $row = $tbody.insertRow(i);
        for (var j = 0; j < fields.length, j++) 
        
        {
            
            var field = fields[j];
            var $cell = $row.insertCell(j);
            $cell.innerText = address[field];
        }
    }
}

function datetime() {
    var filteritem = $Input.value.trim();
    filter = filter.filter(function(address) {
        var addressState = address.datetime;
        return addressState === filteritem;
    });
    renderTable();
}

function city() {
    var filteritem = $Input.value.trim();
    filter = filter.filter(function(address) {
        var addressState = address.city;
        return addressState === filteritem;
    })
    renderTable();
}

function state() {
    var filteritem = $Input.value.trim();
    filter = filter.filter(function(address) {
        var addressState = address.state;
        return addressState === filteritem;
    })
    renderTable();
}

function country() {
    var filteritem = $Input.value.trim();
    filter = filter.filter(function(address) {
        var addressState = address.country;
        return addressState === filteritem;
    })
    renderTable();
}

function shape() {
    var filteritem = $Input.value.trim();
    filter = filter.filter(function(address) {
        var addressState = address.shape;
        return addressState === filteritem;
    })
    renderTable();
}