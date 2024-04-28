//generate number up to parameter
function fillupRoll(x) {
    return Math.floor(Math.random() * x) + 1; // Generates a random number of moves vanillaly
}

// update paragraph with the rolled number from fillupRoll()
function displayRoll(){
    var rollNumber=fillupRoll(3);
    document.getElementById('rollNumber').innerText = 'Number of moves: ' + rollNumber;
}

//event listen to roll button
document.getElementById('rollButton').addEventListener('click', displayRoll);

//event to display number from slider
var slider = document.getElementById("hpID");
var output = document.getElementById("sliderValue");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}

//event listen to coordinate button
document.getElementById('rollCoordinatesButton').addEventListener('click', displayCoordinateRoll);

// update paragraph with the rolled number from the coordinates()
function displayCoordinateRoll(){
  var rollNumberX=fillupRoll(11);
  var rollNumberY=fillupRoll(11);
  document.getElementById('rollCoordinates').innerText = 'Chosen Coordinates: ' + rollNumberX + ', ' + rollNumberY;
}