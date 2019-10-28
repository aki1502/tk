function reloadTheFrame () {
    
    var iframe = document.getElementById("timeline_frame");

    iframe.contentWindow.location.reload(true);

}
function reloadThePhoneFrame () {
    
    var iframe = document.getElementById("phone_timeline_frame");

    iframe.contentWindow.location.reload(true);

}
window.addEventListener("load", function () {

    this.setInterval(reloadTheFrame, 5000);

})
window.addEventListener("load", function () {

    this.setInterval(reloadTheFrame, 5000);

});