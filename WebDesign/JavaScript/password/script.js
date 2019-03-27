function passwordMustContain() {
    var numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for (i = 0; i < $('#password'.val().length(); i ++) {

    }
}
function checkingStuff() {    
    if ($('#fullName').val() === '' || $('#username').val() === '' || $('#password').val() === '' || $('#confirmPassword').val() === '') {
        $('#boxFill').html('You forgot to fill in one or more boxes.')
    } else if ($('#password').val() != $('#confirmPassword').val()) {
        $('#passwordMatch').html('Your passwords must match.')
    } else if ($('#password').val().length() < 8 || $('#confirmPassword').val().length() < 8) {
        $('#passwordLength').html('Your password must be 8 or more characters.')
    } else if ($('#password').val().length() < 8 || $('#confirmPassword').val().length() < 8) {
        $('#passwordLength').html('Your password must be 8 or more characters.')
    }
}
// if then statements go here //