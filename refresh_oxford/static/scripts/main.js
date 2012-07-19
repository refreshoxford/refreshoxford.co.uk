$(function() {
    // Add a close button to all messages
    $('.messages li').prepend('<a href="#" class="message-close">&times;</button>');
    // Bind a click event to the close button, to the close the message
    $(document).on('click', '.message-close', function(e) {
        e.preventDefault();
        $(this).closest('li').hide();
    });
});

