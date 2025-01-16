const selecter = document.querySelector("#max");
const add1 = document.querySelector("#one");
const add2 = document.querySelector("#two");
const reset = document.querySelector("#re");
const score = document.querySelector("#score");
const keeper = document.querySelector(".keeper")

let p1 = 0;
let p2 = 0;
let win = false;

let increaseScore = (p, amount) => {
    return p + amount;
};

let update = () => {
    score.innerHTML = p1 + " : " + p2;
};

let addOptions = max => {
    for(let i = 1; i <= max; i++) {
        let option = document.createElement("option");
        option.innerHTML = i;
        option.value = parseInt(i);
        selecter.appendChild(option);
    }
};

let checkWin = (m) => {
    if(selecter.value == m && win === false) {
        let p = document.createElement("p");
        p.innerText = "We have a winner!"
        keeper.appendChild(p);
        return true;
    }
    return false;
};

add1.addEventListener("click", () => {
    p1 = increaseScore(p1, 1);
    win = checkWin(p1);
    update();
})

add2.addEventListener("click", () => {
    p2 = increaseScore(p2, 1);
    win = checkWin(p2);
    update();
});

reset.addEventListener("click", () => {
    p1 = 0;
    p2 = 0;

    if(win) {
        keeper.removeChild(keeper.lastElementChild); 
        
    }
    win = false;
    
    update();
});

addOptions(101);