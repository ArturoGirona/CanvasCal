//Scripts used for webpages!
//Luke Baker

function checkSignIn(){

	var name = document.getElementById('emailIn').value;
	var password = document.getElementById('pswrdIn').value;
	
	if( name=="test@gmail.com" && password=="testing"){
		window.location.href = "MainPage.html";
		//If email & password match redirect to mainpage!
	}
	else{
		document.getElementById('wrongValue').style.visibility= "visible";
		document.getElementById('wrongValue').style.height="10px";
		document.getElementById('wrongValue').style.paddingBottom="5px";
		//Else display that something is wrong!
	}
}