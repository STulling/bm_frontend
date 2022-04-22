function sendreq(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, true ); // false for synchronous request
    xmlHttp.send(null);
    console.log("test");
    return xmlHttp.responseText;
}
