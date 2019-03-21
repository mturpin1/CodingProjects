$('#changeBtn').click(function () {
    $('#result1').html('Button 1 clicked!')
})

$('#readBtn').click(function(){
    let newInput = $('#inputBox').val()
    $('#result2').html(`This box says ${newInput}`)
})

$('#animateBtn').click(function() {
    $('#result3').html("I'M FREEEE")
    $('#result3').animate({
        'opacity': 0,
        'letter-spacing': '+10'
    }, 1500)
})