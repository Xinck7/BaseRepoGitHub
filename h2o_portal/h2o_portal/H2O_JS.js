// H2O Social Tool Methods
//var isAuth = ('{{ user.isauthenticated}}');

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
  var Modal = document.getElementsByClassName("Modal")
  var i;
  for (i = 0; i < Modal.length; i++) {
    Modal[i].style.display = "none";
  }  
}

function RevealWindow(id){      
    HideWindows()
    var RevealPane = document.getElementById(id);
    if (RevealPane.style.display === "none") {
      RevealPane.style.display = "block";
    } 
    else {
      RevealPane.style.display = "none";
    } 
}

function RevealCheckBox(id){
    var RevealCheckBox = document.getElementById(id);     
    if (RevealCheckBox.style.display === "none") {
        RevealCheckBox.style.display = "block";
    } 
    else{
        RevealCheckBox.style.display = "none";
    }  
}

function CloseModal(id){
    var modal = document.getElementById(id);
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}
//state management and lazy loading
//redux