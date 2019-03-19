function fizzbuzz(num) {
    if (num % 3 === 0 && num % 5 === 0) {
        return "fizzbuzz"
    } else if (num % 3 === 0) {
        return 'fizz'
    } else if (num % 5 === 0) {
        return 'buzz'
    } else {
        return 'dud'
    }
}


document.getElementById('submit').addEventListener('click', function() {
    let newNum = document.getElementById('fizzboi').value
    let fb_result = fizzbuzz(newNum)
    document.getElementById('result').innerHTML = `${newNum} results in ${fb_result}`
})

/* when the button is clicked fire a function */
/* grab the new value in the textbox */
/* run that new number through fizzbuzzery */
/* display the result on the page */