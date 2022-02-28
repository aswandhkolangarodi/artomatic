$(document).ready(function(){



    function setProgress(elem, percent) {
    var
    degrees = percent * 3.6,
    transform = /MSIE 9/.test(navigator.userAgent) ? 'msTransform' : 'transform';
    elem.querySelector('.counter').setAttribute('data-percent', Math.round(percent));
    elem.querySelector('.progressEnd').style[transform] = 'rotate(' + degrees + 'deg)';
    elem.querySelector('.progress').style[transform] = 'rotate(' + degrees + 'deg)';
    if(percent >= 50 && !/(^|\s)fiftyPlus(\s|$)/.test(elem.className))
    elem.className += ' fiftyPlus';
    }
    
    (function() {
    var
    elem = document.querySelector('.circlePercent'),
    percent = 0;
    (function animate() {
    setProgress(elem, (percent += .25));
    if(percent < 100) setTimeout(animate, 15); })(); })(); });