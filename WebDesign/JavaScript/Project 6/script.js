$('#triangleBoi').click(function() {
    console.log('clicked!')
    $('#triangleBoi').attr('animation', 'property: components.material.material.color; type: color; to: red; dur: 1500;');
    $('#button').attr('animation', 'property: opacity;  to: 1; dur: 1500;');
    $('#btnText').attr('animation', 'property: opacity;  to: 1; dur: 1500;');
    console.log('yeet!')
})

$('#button').hover(function() {
    $('#button').attr('animation', 'property: components.material.material.color; type: color; to: cyan; dur: 1500;')
})
