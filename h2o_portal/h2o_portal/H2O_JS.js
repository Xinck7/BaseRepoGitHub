// H2O Social Tool Methods
//var isAuth = ('{{ user.isauthenticated}}');
function HideWindows(){
  var RevealPanes = document.getElementsByClassName("revealpane")
  var i;
  for (i = 0; i < RevealPanes.length; i++) {
    RevealPanes[i].style.display = "none";
}  
}
function RevealWindow(windowidname){      
    HideWindows()
    var RevealPane = document.getElementById(windowidname);
    if (RevealPane.style.display === "none") {
      RevealPane.style.display = "block";
    } 
    else {
      RevealPane.style.display = "none";
    } 
}
//state management and lazy loading
//redux