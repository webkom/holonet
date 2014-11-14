var growl = function(title, message, icon) {
    $.growl({
        icon: icon,
        title: title,
        message: message
    }, {
        template: '<div data-growl="container" class="alert" role="alert">' +
                    '<button type="button" class="close" data-growl="dismiss">' +
                        '<span aria-hidden="true">×</span>' +
                        '<span class="sr-only">Close</span>' +
                    '</button>' +
                    '<span data-growl="icon"></span> ' +
                    '<span data-growl="title"></span><br/>' +
                    '<span data-growl="message"></span>' +
                  '</div>'
    });
};

module.exports = growl;
