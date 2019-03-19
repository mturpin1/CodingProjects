function curfewRequirements(age, time) {
    if (age < 12 && time > 8) {
        console.log('Go home, kid')
    } else if (age >= 12 && age < 18 && time > 10) {
        console.log('You should probably be getting home')
    } else if (age >= 18) {
        console.log('You can do whatever the heck you want')
    } else if (time < 8) {
        console.log('You are good, my dude. Make sure you get home before curfew')
    }
}

curfewRequirements(13, 7)