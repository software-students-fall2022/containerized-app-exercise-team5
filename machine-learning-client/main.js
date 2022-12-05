// code for button from user Andrew White on codepen:
// https://codepen.io/aeewhite/pen/BjzbOL
// minor alterations for the purposes of this web app made by Charlie Xiang

$('#recButton').addClass("notRec");

$('#start').click(function(){
	$('#recButton').removeClass("notRec");
	$('#recButton').addClass("Rec");
	
});

$('#stop').click(function(){
	$('#recButton').removeClass("Rec");
	$('#recButton').addClass("notRec");
});

document.addEventListener("keyup", function(event) {
    if (event.code === "Enter") {
        $('#recButton').removeClass("Rec");
		$('#recButton').addClass("notRec");
    }
});
