function calculateTip(price, tip) {
    // this function returns the tip only (not the total with tip)
    return (price * tip).toFixed(2)
}
 
function splitBill (price, people, tip) {
    // this function returns the amount each person pays (full price divided between each person)
    return ((price * (tip + 1)) / people).toFixed(2)
}
 
function fullPrice (price, tip) {
    // this function returns the full price (total plus tip)
    return (price * (tip + 1)).toFixed(2)
}

 
/*  in the space below, create a click function that:
    grabs the new values inside the boxes (price, # of people, and tip %)
    changes the three result boxes to their new values
    this can all be done in 8 lines (or you can make a bunch of variables, which is fine too)
    the only jQuery-specific actions needed are .val() and .html() */
$('#cb').click(function() {
    let price = $('#opi').val()
    let people = $('#nopsi').val()
    let tip = $('#ti').val() / 100
    $('#tttgotb').html(`$${calculateTip(price, tip)}`)
    $('#wepp').html(`$${splitBill(price, people, tip)}`)
    fullPrice(price, tip)

})