const link = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
const container = document.querySelector(".container");
const pokemon = document.querySelector(".pokemon");

const bod = document.body;
bod.style.background = "lightblue";

let all = () => {
    for(let i = 1; i <= 898; i++) {
        poke = create(i);
        container.appendChild(poke.pokemon);
    }
};



let get = () => {
    let input = document.querySelector("section input").value;
    poke = create(input);
    pokemon.replaceChild(poke.pokemon, pokemon.childNodes[0]);
};

let create = (i) => {
    let poke = {
        lin: link + i + ".png",
        num: i,
        pokemon: document.createElement("div"),
        img: document.createElement("img"),
        label: document.createElement("span")
    };
    
    poke.label.innerHTML = "#" + i;
    poke.pokemon.appendChild(poke.img);
    poke.pokemon.appendChild(poke.label);

    poke.img.src = poke.lin;
    return poke;
};
all()
