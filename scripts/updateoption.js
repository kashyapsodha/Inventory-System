
function goback()
 {
  
        window.location = "admin.html";  
}


function isChecked()
{


 var radioSelected = document.querySelector('input[name="radioSelect"]:checked').value;
 
 if(radioSelected == 'price')
 	{

 		window.location = "update_admin1.html";  

 	}
 else if(radioSelected == 'count')
    { 
 	
 		window.location = "update_admin2.html";  

	} 

}	