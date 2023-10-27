// Jquery to grab the document ready

$(document).ready(function() {
    const validate = $('#validate');
    // if (localStorage.getItem("email") != null)
    // {
    //     $('#email').val(localStorage.getItem("email"));
    // }
    const error = $('#error');

    error.hide();

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

    validate.on('click', function() {
        // Check all fields
        if (!validate_f())
            return;
        let data= {};
        if (order_type.val() === 'no_form') {
            // Get the data
            data = {
                'email': $('#email').val(),
                'order_type': order_type.val(),
                'no_form_product': $('#no_form_product').val()
            }
        }
        else
        {
            // Get the data
            data = {
                'email': $('#email').val(),
                'order_type': order_type.val(),
                'principal': $('#principal').val(),
                'secondary': $('#secondary').val(),
                'drink': $('#drink').val(),
                'no_form_product': $('#no_form_product').val()
            }

            data = JSON.stringify(data);
        }

        // Store email in localstorage
        localStorage.setItem("email", $('#email').val())
        // Send the data to the server
        $.ajax({
            url: '/order',
            type: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            data: data,
            success: function(response) {
                if (response === 'OK')
                {
                    window.location.replace('/success');
                }
                else
                {
                    error.text('Une erreur est survenue');
                    error.show();
                }
            },
            error: function(error) {
                error.text('Une erreur est survenue');
                error.show();
            }
        });
    });
});

/**
 * Check the email with regexp and check if it's an efrei email
 * @param email
 * @returns {boolean}
 */
function checkEmail(email) {
    // Regex to check the email
    if (email === '')
        return false;
    if (!email.includes('.'))
        return false;
    if (!email.includes('@efrei.net'))
        return false;
    let regex = /^[a-zA-Z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$/;
    return regex.test(email);
}

/**
 * Check all the fields
 * @returns {boolean}
 */
function validate_f()
{
    const error = $('#error');

    if ($('#order_type').val() === 'no_form') {
        if (!checkEmail($('#email').val()))
        {
            error.text('Votre email n\'est pas valide');
            error.show();
            return false;
        }
        else if($('#no_form_product').val() === null)
        {
            error.text('Veuillez remplir tous les champs');
            error.show();
            return false;
        }
    }
    else
    {
        if (!checkEmail($('#email').val()))
        {
            error.text('Votre email n\'est pas valide');
            error.show();
            return false;
        }
        else if ($('#principal').val() === null || $('#secondary').val() === null || $('#drink').val() === null)
        {
            error.text('Veuillez remplir tous les champs');
            error.show();
            return false;
        }
    }
    return true;
}