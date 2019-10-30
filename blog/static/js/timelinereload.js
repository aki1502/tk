function reloadTheFrame () {
    
    var iframe = document.getElementById("timeline_frame");

    iframe.contentWindow.location.reload(true);
    
    var iframe = document.getElementById("phone_timeline_frame");

    iframe.contentWindow.location.reload(true);

}
window.addEventListener("load", function () {

    this.setInterval(reloadTheFrame, 5000);

})