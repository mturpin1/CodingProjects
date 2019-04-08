$('#submit').click(function() {
    let thing = $('#search').val()
    $.ajax({
        url: "https://api.giphy.com/v1/gifs/search",
        dataType: "json",
        method: "GET",
        data: {
            api_key: "I2tzIWpoXIwIG5vgLS5tLSOyGa9rTrir",
            q: `${thing}`,
        },
        success: function(gif_response) {
            let url = gif_response.data[0].embed_url
           $('#result').html(`
           <iframe src=${url}></iframe>
           `)
        }
    })
})
