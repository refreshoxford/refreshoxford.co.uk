$(document).ready(function () {
    // js polyfil for html5 placeholder form text
    $('input, textarea').placeholder();

    font.setup();
    if(!font.isInstalled('Adobe Caslon Pro')) {
        $('.signup-greeting').addClass('smaller');
    }
});
