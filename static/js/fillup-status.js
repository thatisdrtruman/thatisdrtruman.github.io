//generate 1, 2 or 3
function fillupRoll() {
    return Math.floor(Math.random() * 3) + 1; // Generates a random number of moves vanillaly
}

// update paragraph with the rolled number from fillupRoll()
function displayRoll(){
    var rollNumber=fillupRoll();
    document.getElementById('rollNumber').innerText = 'Number of moves: ' + rollNumber;
}

//event listen to button
document.getElementById('rollButton').addEventListener('click', displayRoll);

var slider = document.getElementById("hpID");
var output = document.getElementById("sliderValue");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}