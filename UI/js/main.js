document.addEventListener('DOMContentLoaded', function(){
//Get Modal
var modal = document.getElementById('vd-modal');

//Get button that opens modal
var btn_detail = document.getElementById('btn-detail');

//get close span 
var span_close = document.getElementsByClassName("close")[0];


// btn_detail onclick event
btn_detail.onclick = function(){
    modal.style.display = "block";
}


// span_close onclick event
 span_close.onclick = function(){
     modal.style.display = "none";
 }


//close when user clicks anywhere outside the modal
window.onclick = function(){
    if(event.target == modal){
        modal.style.display = "none";
    }
}
}, false);
