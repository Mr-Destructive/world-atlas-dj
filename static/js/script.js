let tab = document.getElementById("tab");
let row;
let rowcount = 0;
let points, com, ply;
let win = document.querySelector(".alert");
let pointdiv = document.querySelector(".points");
let info = document.querySelector("#info");
let placeinp = document.querySelector("#place");
let start = document.getElementById("start");
let submit = document.getElementById("submit");
let botlast;
let toss_flip;
placeinp.disabled = true;
submit.disabled = true;

document.getElementById("submit").addEventListener("click", () => {

    placeinp.disabled = true;
    plyplace = placeinp.value;
    if (plyplace == '') {
        placeinp.disabled = false;
    } else {
        plyplace = plyplace.toLowerCase();

        validate(plyplace, () => {

            row = tab.insertRow(rowcount);
            if (toss === 0) {
                ply = row.insertCell(0);
            } else {
                com = row.insertCell(0);
                ply = row.insertCell(1);
            }
            ply.innerHTML = plyplace;
            placeinp.value = "";
            scroller();
            plylast = getLast(plyplace);
            botplace = givePlace(plylast);
            botlast = getLast(botplace);
            submit.disabled = false;
        })
    }
});

document.getElementById("place").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("submit").click();
    }
});
document.querySelector(".closebtn").addEventListener("click", () => {
    document.querySelector(".alert").style.display = "none";
    document.querySelector(".closebtn").style.display = "none";
})
let place = "";
let a = [], b = [], c = [], e = [], f = [], d = [], g = [], h = [], i = [], j = [], k = [], l = [], m = [];
let n = [], o = [], p = [], q = [], r = [], s = [], t = [], u = [], v = [], w = [], x = [], y = [], z = [];
let valid = false;

coms = document.getElementById('tab');

observer = new MutationObserver(function(mutationsList, observer) {
    complast = getLast(place);
    if (points > 0) {
        info.firstChild.nodeValue = "Enter a Place beginning with : " + complast;
    }
});

observer.observe(coms, {
    characterData: false,
    childList: true,
    attributes: false
});

function scroller() {
    let scrop = document.getElementById('tab');
    scrop.scrollTop = scrop.scrollHeight;
}

function toss() {
    start.innerHTML = "Restart";
    start.style.top = "28%";
    start.style.left = "40%";
    win.style.visibility = "hidden";
    document.querySelector(".closebtn").style.visibility = "hidden";
    info.style.visibility = "visible";
    placeinp.disabled = true;
    toss_flip = Math.floor(Math.random() * 2);
    info.innerHTML = '';
    var Parent = document.getElementById('tab');
    rowcount = 0;
    points = 0;
    pointdiv.innerHTML = "Points : " + points;
    while (Parent.hasChildNodes()) {
        Parent.removeChild(Parent.firstChild);
    }
    a = [], b = [], c = [], e = [], f = [], d = [], g = [], h = [], i = [], j = [], k = [], l = [], m = [];
    n = [], o = [], p = [], q = [], r = [], s = [], t = [], u = [], v = [], w = [], x = [], y = [], z = [];
    tab = document.getElementById("tab");
    row = tab.insertRow(0);
    com = row.insertCell(0);
    rowcount = 0;
    play(toss_flip);

}

function play(toss) {
    if (toss === 0) {
        info.innerHTML = 'The Bot enters the place first';
        placeinp.disabled = true;
        let letter = "abcdefghijklmnopqrstuvwxyz";
        let random_index = Math.floor(Math.random() * 26);
        let random_char = letter[random_index];
        botplace = givePlace(random_char);
    } else {
        info.innerHTML = 'You will enter the place first';
        placeinp.disabled = false;
    }
    submit.disabled = false;
}

// gets last character of the given place
function getLast(place) {
    let last = place.length
    return place[last - 1];
}

// random place generator for bot
function givePlace(letter) {
    let url = `/api/places/get/${letter}/`;
    axios.get(url)
        .then(function(response) {
            place = response["data"][letter];
            if (validate_comp(place)) {
                rowcount += 1;
                com.appendChild(document.createTextNode(place));
                botlast = getLast(place);
                scroller();
                placeinp.disabled = false;
                info.firstChild.nodeValue = "Enter a Place beginning with : " + botlast;
            }
            return place;
        })
        .catch(function(error) {
            console.log(error);
        })
    return place;
}

//validate a user input place
function validate(place, _callback) {
    let exists = 0,
        repeated = 0,
        count = 0,
        last = 0,
        dictlen = 0;
    let first = place[0];
    if (toss_flip === 0 || toss_flip === 1 && points !== 0) {
        if (first !== botlast) {
            last = 1;
            valid = false;
            log_game_close(place, exists, count, repeated, dictlen, last, valid)
            return valid
        }
    }
    let placelist = [];
    let url = `/api/places/exists/${place}`;
    _callback(axios.get(url)
        .then(function(response) {
            is_valid = response.data["result"];

            if (is_valid) {
                exists = 1;
            }

            let dict = get_dict(first);
            dictlen = dict.length;

            for (let i = 0; i < dictlen; i++) {
                if (place == dict[i]) {
                    repeated = 1;
                    break;
                } else {
                    count += 1;
                }
            }

            log_game_close(place, exists, count, repeated, dictlen, last, valid);
            return valid;
        })
        .catch(function(error) {
            console.log(error);
        }))
}

function log_game_close(place, exists, count, repeated, dictlen, last, valid) {
    if (exists == 1 && count == dictlen && repeated == 0 && last == 0 && valid) {
        add_to_list(place);
        placeinp.disabled = false;
        submit.disabled = false;
        placeinp.focus();
        points += 1;
        pointdiv.innerHTML = "Points : " + points;
    } else {
        placeinp.disabled = true;
        submit.disabled = true;
        let message;
        if (repeated == 1) {
            message = `Place "${place}" is repeated`;
        } else if (last == 1) {
            message = `"${place}" has invalid first letter. Begin your place with "${botlast}"`;
        } else if (exists == 0) {
            message = `"${place}" not found. Invalid place`;
        }
        win.innerHTML = `You Lost: ${message}`;
        win.style.backgroundColor = "#ff4436";
        win.style.visibility = "visible";
        document.querySelector(".closebtn").style.visibility = "visible";
        info.style.visibility = "hidden";
        start.style.top = "75%";
        start.innerHTML = "Restart";
        start.style.visibility = "visible";
    }
}

function validate_comp(place) {
    let first = place[0];
    let repeated = 0,
        count = 0;
    let dict = get_dict(first);

    let dictlen = dict.length;

    for (let i = 0; i < dictlen; i++) {
        if (place == dict[i]) {
            repeated = 1;
            break;
        } else {
            count += 1;
        }
    }

    if (count === dictlen && repeated === 0) {
        valid = true;
        add_to_list(place);
    } else {
        placeinp.disabled = true;
        info.innerHTML = "You Won!!";
        win.style.backgroundColor = "#00dd14";
        win.innerHTML = "You Won!"
        win.style.visibility = "visible";
        document.querySelector(".closebtn").style.visibility = "visible";
        start.style.top = "75%";
        start.innerHTML = "Restart";
        start.style.visibility = "visible";
        info.style.visibility = "hidden";
    }
    return valid;
}

function get_dict(first) {
    switch (first) {
        case 'a':
            return a;
        case 'b':
            return b;
        case 'c':
            return c;
        case 'd':
            return d;
        case 'e':
            return e;
        case 'f':
            return f;
        case 'g':
            return g;
        case 'h':
            return h;
        case 'i':
            return i;
        case 'j':
            return j;
        case 'k':
            return k;
        case 'l':
            return l;
        case 'm':
            return m;
        case 'n':
            return n;
        case 'o':
            return o;
        case 'p':
            return p;
        case 'q':
            return q;
        case 'r':
            return r;
        case 's':
            return s;
        case 't':
            return t;
        case 'u':
            return u;
        case 'v':
            return v;
        case 'w':
            return w;
        case 'x':
            return x;
        case 'y':
            return y;
        case 'z':
            return z;
    }
}

// add a valid place to dicts
function add_to_list(place) {
    switch (place[0]) {
        case 'a':
            a.push(place);
        case 'b':
            b.push(place);
        case 'c':
            c.push(place);
        case 'd':
            d.push(place);
        case 'e':
            e.push(place);
        case 'f':
            f.push(place);
        case 'g':
            g.push(place);
        case 'h':
            h.push(place);
        case 'i':
            i.push(place);
        case 'j':
            j.push(place);
        case 'k':
            k.push(place);
        case 'l':
            l.push(place);
        case 'm':
            m.push(place);
        case 'n':
            n.push(place);
        case 'o':
            o.push(place);
        case 'p':
            p.push(place);
        case 'q':
            q.push(place);
        case 'r':
            r.push(place);
        case 's':
            s.push(place);
        case 't':
            t.push(place);
        case 'u':
            u.push(place);
        case 'v':
            v.push(place);
        case 'w':
            w.push(place);
        case 'x':
            x.push(place);
        case 'y':
            y.push(place);
        case 'z':
            z.push(place);
    }
}
