function toggleDetails(element) {
    const players = element.querySelector('.players');
    if (players.style.display === 'flex') {
        players.style.display = 'none';
    } else {
        players.style.display = 'flex';
    }
}
function loadImage(imageId, webpSrc, fallbackSrc) {
    console.log(imageId)
    var imgElements = document.querySelectorAll(`[id='${CSS.escape(imageId)}']`);
        
    imgElements.forEach(function(imgElement) {
        console.log('x')
        var img = new Image();
        img.onload = function() {
            imgElement.src = webpSrc;
        };
        img.onerror = function() {
            imgElement.src = fallbackSrc;
        };
        img.src = webpSrc;
    });
}