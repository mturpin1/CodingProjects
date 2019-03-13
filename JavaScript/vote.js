function voteCheck(age) {
    if (age >= 18) {
        console.log('You can vote')
    } else if (age < 18) {
        console.log('You cannot vote, twerp.')
    }
}

voteCheck(18)