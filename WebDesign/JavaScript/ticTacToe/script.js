let winArr = [
    ['#0-0', '#1-0', '#2-0'],       // top row
    ['#0-1', '#1-1', '#2-1'],       // middle row
    ['#0-2', '#1-2', '#2-2'],       // bottom row
    ['#0-0', '#0-1', '#0-2'],       // left column
    ['#1-0', '#1-1', '#1-2'],       // middle column
    ['#2-0', '#2-1', '#2-2'],       // right column
    ['#0-0', '#1-1', '#2-2'],       // back slash
    ["#0-2", "#1-1", "#2-0"]        // forward slash
]

let mark = 'X'
let marksOnBoard = 0

function markCell() {
    if (!this.innerText) {
        this.innerText = mark
        marksOnBoard++
        if (playerWon(mark)) {
            displayMessage(`${mark} won the game! Click anywhere to reset!`)
        } else if (marksOnBoard === 9) {
            displayMessage('Tie Game! Click anywhere to reset!')
        }
        if (mark === 'X') {
            mark = 'O'
        } else if (mark === 'O') {
            mark = 'X'
        }
    }
}

$('.cell').click(function() {
    $('.cell').click(markCell)
})

function elementContains(id, mark) {
    return $(id).text() === mark
}

function playerWon(mark) {
    for (let i = 0; i < winArr.length; i++) {
        let winCombo = winArr[i]
        let won = winCombo.every(
            function (id) {
                return elementContains(id, mark)
            }
        )
        if (won === true) return true
    }
    return false
}

function resetGame(msg) {
    $('#message').html(`${msg}`)
    $('#message').css('pointer-events', 'none')
    marksOnBoard = 0
    mark = 'X'
    $('.cell').html('')
    $('#message').html('')
}

function displayMessage(msg) {
    $('#message').html(`${msg}`)
    $('#message').css('pointer-events', 'all')
}

function listenForClickOnMessage() {
    $('#message').click(resetGame)
}

listenForClickOnMessage()