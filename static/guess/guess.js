let input = document.getElementById("user_guess");
let display = document.getElementById("display");
let guess1 = document.querySelector("body");

let guess_amount = -1;
let max = 0;
let num = 0;

function guess() {
    let input = document.getElementById("user_guess");
    
    let g_num = parseInt(input.value);
    if (guess_amount === -1) {
        max = input.value;
        num = Math.floor((Math.random() * max) + 1);
    }
    display.innerHTML = "I'm thinking of a number from 1 to " + max + "...";
    

    if(guess_amount >= 0) {
        if (g_num === num) {
            guess_amount++;
            display.innerHTML = g_num + " is Correct! It took you " + guess_amount + " guesses";
            
        }
        else if(g_num > num) {
            display.innerHTML = g_num + ' is too high. Try again!';
        }
        else {
            display.innerHTML = g_num + ' is too low. Try again!';
        }

    }
    guess_amount++;
}