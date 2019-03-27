$('.text-danger').hide()

function lengthGood() {
    if ($('#password').val().length >= 8) {
        return true
    } else {
        return false
    }
}

function containsNum(word) {
    // for loop, check each character, if it's a number, break the loop word.charAt()
    let hasNum
    if (word === undefined) {
        return false
    } else {
        for (i = 0; i < word.length; i++) {
            if (isNaN(word.charAt(i)) ) {
                hasNum = false
            } else {
                hasNum = true
                break
            }
        }
        return hasNum
    }
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
    if (lengthGood()) {
        $('#passwordLength').hide()
    } else {
        $('#passwordLength').show()
    }
    
    if (containsNum()) {
        $('#passwordContains').show()
    } else {
        $('#passwordContains').hide()
    }
    
    if (passMatch()) {
        $('#passwordMatch').hide()
    } else {
        $('#passwordMatch').show()
    }
    
    if (boxesFilled()) {
        $('#boxFill').hide()
    } else {
        $('#boxFill').show()
    }
    // if (all functions return whatever they're supposed to) { alert() }
})
if (lengthGood === true && containsNum === true && passMatch === true && boxesFilled === true) {
    alert('Congratulations, you have successfully filled out the form. Thanks for signing up!')
}
