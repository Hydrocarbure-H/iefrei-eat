// Jquery to grab the document ready
$(document).ready(function() {
    order_type = $('#order_type')
    // Check the order_type value
    if (order_type.val() === 'no_form') {
        $('#no_form').show();
        $('#with_form').hide();
    }
    else {
        $('#no_form').hide();
        $('#with_form').show();
    }

    // Add the listenners on order_type, principal, secondary, drink
    order_type.on('change', function() {
        if (this.value === 'no_form') {
            $('#no_form').show();
            $('#with_form').hide();
        }
        else {
            $('#no_form').hide();
            $('#with_form').show();
        }
    });

    let validate = $('#validate');
    let error = $('#error');
    validate.on('click', function() {
        // Check all fields
        if ($('#order_type').val() === 'no_form') {
            if (!checkEmail($('#email').val()) || $('#no_form_product').val())
            {
                error.text('Veuillez remplir tous les champs');
                error.show();
                return false;
            }
        }
        else {
            if (!checkEmail($('#email').val()) || $('#principal').val() === null || $('#secondary').val() === null || $('#drink').val() === null)
            {
                error.text('Veuillez remplir tous les champs');
                error.show();
                return false;
            }
        }
    });
});

/**
 * Check the email with regexp and check if it's an efrei email
 * @param email
 * @returns {boolean}
 */
function checkEmail(email) {
    // Regex to check the email
    let regex = /^[a-zA-Z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$/;
    return regex.test(email) === email.includes('@efrei.net');
}