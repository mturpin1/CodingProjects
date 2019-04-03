$('#submit').click(function() {
    let city = $('#city').val()
    $.ajax({
        url: `http://api.openweathermap.org/data/2.5/weather?q=${city}&APPID=15e973e12d8a094880494330134dde20&units=imperial`,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            console.log(data)
            $('#result1').html( `${data.main.temp_max} degrees F`)
            $('#result2').html(`${data.main.temp_min} degrees F`)
            $('#result3').html(`${data.main.pressure} atm`)
            $('#result4').html(`${data.main.humidity}%`)

        }
    })
})