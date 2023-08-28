var responseData = window.localStorage.getItem('myData');

var sound = new Audio('/static/sounds/music.mp3'); 

var houses = ["Hufflepuff", "Gryffindor", "Slytherin", "Ravenclaw"];
var randomhouse = houses.indexOf (responseData);

var audio = new Audio('/static/sounds/' + responseData + 'before.mp3');

var audioafter = new Audio('/static/sounds/' + responseData + 'after.mp3');

document.querySelector(".house a").addEventListener("click", housetext);

function housetext() {

  document.querySelector(".house a").remove();

  sound.pause();
  sound.currentTime = 0;
  sound.play();

  audio.pause();
  audio.currentTime = 0; //Sorting hat speech restarts each time the button is clicked
  audio.play();


  document.querySelector(".house").textContent = "Hmmm...";

  audio.onended = function() {
    audioafter.play();
    document.querySelector(".house").textContent = houses[randomhouse];
    document.querySelector(".housename").textContent = houses[randomhouse];
  }; //Name and voice of the alloted house shows up once the sorting hat's speech is over


  audioafter.onended = function() {
    setTimeout(function() {
      switch (randomhouse) {
        case 0:
          document.querySelector(".page2").style.backgroundImage = "url('/static/images/Hufflepuff.jpg')";
          break;

        case 1:
          document.querySelector(".page2").style.backgroundImage = "url('/static/images/Gryffindor.jpg')";
          break;

        case 2:
          document.querySelector(".page2").style.backgroundImage = "url('/static/images/Slytherin.jpg')";
          break;

        case 3:
          document.querySelector(".page2").style.backgroundImage = "url('/static/images/Ravenclaw.jpg')";
          break;
      }
      document.getElementById("eighth").remove();
      document.querySelector("#over").classList.remove("overlay");
      document.querySelector("#cont").classList.remove("container");
      document.querySelector("#over").classList.add("overlayactive");
      document.querySelector("#cont").classList.add("containeractive");
    }, 500);
  };
}
