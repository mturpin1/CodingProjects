$('#Btn1').click(function() {
    $('#Result1').html("Look who knows some JS y'all!")
})

$('#Btn2').click(function() {
    let num1 = parseInt($('#Result2').val())
    let num2 = parseInt($('#Result3').val())
    let newSum = num1 + num2
    $('#Result4').html(`The sum is ${newSum}`)
})

$('#Btn3').click(function() {
    $('#Result5').html("Time to get swole")
    $('#Result5').animate({
        'font-size': +30,
        'letter-spacing': +5
    })
})