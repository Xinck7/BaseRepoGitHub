// H2O Social Tool Methods

function HideWindows(){
  var RevealPanes = document.getElementsByClassName("revealpane")
  var i;
  for (i = 0; i < RevealPanes.length; i++) {
    RevealPanes[i].style.display = "none";
  }

  var RevealPanesInner = document.getElementsByClassName("revealpaneinner")
  var i;
  for (i = 0; i < RevealPanesInner.length; i++) {
    RevealPanesInner[i].style.display = "none";
  }
}

function RevealWindow(id){      
  HideWindows()
  var RevealPane = document.getElementById(id);
  RevealPane.style.display = (RevealPane.style.display =="block") ? "none" : "block";
}

function RevealCheckBox(id){
  var RevealCheckBox = document.getElementById(id);
  RevealCheckBox.style.display = (RevealCheckBox.style.display =="block") ? "none" : "block";  
}

function ToggleModal(id){
  var modalwindow = document.getElementById(id);
  modalwindow.style.visibility = (modalwindow.style.visibility =="visible") ? "hidden" : "visible";
}

window.onclick = function(event) {
  var modal = document.getElementById('appauth');
  if (event.target == modal) {
    modal.style.visibility = "hidden"
  }
}

//state management and lazy loading?
//redux?