$('.text-danger').hide()

function lengthGood() {
    if ($('#password').val().length >= 8) {
        return true
    } else {
        return false
    }
}

function containsNum() {

}

function passMatch() {
    if ($('#password').val() === $('#confirmPassword').val()) {
        return true
    } else {
        return false
    }
}

function boxesFilled() {
    if ($('#fullName').val() === '' || $('#username').val() === '' || $('#password').val() === '' || $('#confirmPassword').val() === '') {
        return false
    } else {
        return true
    }
}

$('#submitBoi').click(function() {

})