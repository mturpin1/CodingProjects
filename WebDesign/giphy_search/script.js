$('#submit').click(function() {
    $.ajax({
        url: "https://api.giphy.com/v1/gifs/search",
        dataType: "json",
        method: "GET",
        data: {
            api_key: "I2tzIWpoXIwIG5vgLS5tLSOyGa9rTrir",
            q: 'cat',
        },
        success: function(gif_response) {
            $('#result').html(`
            <iframe src="${gif_response.data.embed_url}"></iframe>
            `)
        }
    })
})
