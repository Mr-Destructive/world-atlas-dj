let tab = document.getElementById("tab");
let row;
let rowcount = 0;
let points,com,ply;
let win = document.querySelector(".alert");
document.getElementById("submit").addEventListener("click",()=>{
    plyplace= document.getElementById("place").value;	
    plyplace=plyplace.toLowerCase();


    validate(plyplace, ()=> {
    
        points+=1;
        row = tab.insertRow(rowcount);
    if(toss === 0){
        ply = row.insertCell(0);
    }
    else{
        com = row.insertCell(0);
        ply = row.insertCell(1);
    }
        ply.innerHTML = plyplace;
        document.getElementById("place").value = "";
        scroller();
        plylast = getLast(plyplace);
        botplace = givePlace(plylast);
        botlast = getLast(botplace);
    })
    console.log(points);
});

document.getElementById("place").addEventListener("keyup",function(event){
	if(event.keyCode === 13){
		event.preventDefault();
		document.getElementById("submit").click();
	}});

let place="";
let a=[],b=[],c=[],e=[],f=[],d=[],g=[],h=[],i=[],j=[],k=[],l=[],m=[];
let n=[],o=[],p=[],q=[],r=[],s=[],t=[],u=[],v=[],w=[],x=[],y=[],z=[];
let valid = false;

coms = document.getElementById('tab');

observer = new MutationObserver(function(mutationsList, observer) {
    complast = getLast(place);
    if(points > 0){
    document.getElementById("info").innerHTML = "Enter a Place beginning with : " + complast;
    }
});

observer.observe(coms, {characterData: false, childList: true, attributes: false});

function scroller(){
	let scrop = document.getElementById('tab');
	scrop.scrollTop =scrop.scrollHeight;
}

function toss()
{
    document.getElementById("start").style.visibility="hidden";
    let toss=Math.floor(Math.random()*2);
    console.log(toss);
    document.getElementById("info").innerHTML='';
    var Parent = document.getElementById('tab');
    rowcount = 0;
    points=0;
    while(Parent.hasChildNodes())
    {
       Parent.removeChild(Parent.firstChild);
    }
    a=[],b=[],c=[],e=[],f=[],d=[],g=[],h=[],i=[],j=[],k=[],l=[],m=[];
    n=[],o=[],p=[],q=[],r=[],s=[],t=[],u=[],v=[],w=[],x=[],y=[],z=[];
    tab = document.getElementById("tab");
    row = tab.insertRow(0);
    com = row.insertCell(0);
    rowcount = 0;
    play(toss);
    
}

function play(toss)
{
    if( toss === 0)
    {
        document.getElementById("info").innerHTML='The Bot enters the place first';
        let letter ="abcdefghijklmnopqrstuvwxyz";
		let random_index=Math.floor(Math.random()*26);
		let random_char=letter[random_index];
		botplace=givePlace(random_char);
		//validate(botplace);
    }
    else{
        document.getElementById("info").innerHTML='You will enter the place first';
    }
}

// gets last character of the given place
function getLast(place)
{
    let last = place.length
    return place[last-1];
}

// random place generator for bot
function givePlace(letter)
{
    let url = "https://world-atlas-api.herokuapp.com/get/"+letter;
    axios.get(url) 
    .then(function (response)
    {
        place = response["data"][letter];
        console.log(place);
        if(validate_comp(place)){
            rowcount+=1;
            com.innerHTML = place;
            botlast=getLast(place);
            scroller();
            document.getElementById("info").innerHTML="Enter a Place beginning with : " + botlast;
        }
        return place;
    })
    .catch(function (error) {
        console.log(error);
    })
    return place;
}

//validate a user input place
function validate(place, _callback)
{
    let first = place[0];
    let placelist = [];
    let exists = 0, repeated = 0, count = 0;
    let url = "https://world-atlas-api.herokuapp.com/list/"+first;
    _callback(axios.get(url) 
    .then(function (response)
    {
        placelist= response["data"][first];

    let len = placelist.length;

    for(let i=0; i<len; i++)
    {
        if( place == placelist[i] )
        {
            exists=1;
            break;
        }
    }

    let dict = [];

    if(first == 'a') { dict = a; }
       
    if(first == 'b') { dict = b; }
       
    if(first == 'c') { dict = c; }
       
    if(first == 'd') { dict = d; }
       
    if(first == 'e') { dict = e; }
       
    if(first == 'f') { dict = f; }
       
    if(first == 'g') { dict = g; }
       
    if(first == 'h') { dict = h; }
       
    if(first == 'i') { dict = i; }
       
    if(first == 'j') { dict = j; }
       
    if(first == 'k') { dict = k; }
       
    if(first == 'l') { dict = l; }
       
    if(first == 'm') { dict = m; }
       
    if(first == 'n') { dict = n; }
       
    if(first == 'o') { dict = o; }
       
    if(first == 'p') { dict = p; }
       
    if(first == 'q') { dict = q; }
       
    if(first == 'r') { dict = r; }
       
    if(first == 's') { dict = s; }
       
    if(first == 't') { dict = t; }
       
    if(first == 'u') { dict = u; }
       
    if(first == 'v') { dict = v; }
       
    if(first == 'w') { dict = w; }
       
    if(first == 'x') { dict = x; }
       
    if(first == 'y') { dict = y; }
       
    if(first == 'z') { dict = z; }

    let dictlen =dict.length;

    for(let i=0; i<dictlen; i++)
    {
        if(place == dict[i])
        {
            repeated=1;
            break;
        }
        else
        {
            count+=1;
        }
    }

    //console.log(exists + " " + count + " " + dictlen + " " + repeated);
    if(exists === 1 && count === dictlen && repeated === 0){
        valid=true;
        add_to_list(place);
        document.querySelector(".points").innerHTML = points + " Points";
    }

    else{
        valid=false;
        win.innerHTML="You Lost";
        win.style.backgroundColor="#ff4436";
        win.style.visibility="visible";
        document.getElementById("start").style.visibility="visible";
    }
    return valid;
    })
    .catch(function (error) {
        console.log(error);
    }))
}

function validate_comp(place)
{
    let first = place[0];
    let repeated = 0, count = 0;
    let dict = [];

    if(first == 'a') { dict = a; }
       
    if(first == 'b') { dict = b; }
       
    if(first == 'c') { dict = c; }
       
    if(first == 'd') { dict = d; }
       
    if(first == 'e') { dict = e; }
       
    if(first == 'f') { dict = f; }
       
    if(first == 'g') { dict = g; }
       
    if(first == 'h') { dict = h; }
       
    if(first == 'i') { dict = i; }
       
    if(first == 'j') { dict = j; }
       
    if(first == 'k') { dict = k; }
       
    if(first == 'l') { dict = l; }
       
    if(first == 'm') { dict = m; }
       
    if(first == 'n') { dict = n; }
       
    if(first == 'o') { dict = o; }
       
    if(first == 'p') { dict = p; }
       
    if(first == 'q') { dict = q; }
       
    if(first == 'r') { dict = r; }
       
    if(first == 's') { dict = s; }
       
    if(first == 't') { dict = t; }
       
    if(first == 'u') { dict = u; }
       
    if(first == 'v') { dict = v; }
       
    if(first == 'w') { dict = w; }
       
    if(first == 'x') { dict = x; }
       
    if(first == 'y') { dict = y; }
       
    if(first == 'z') { dict = z; }

    let dictlen =dict.length;

    for(let i=0; i<dictlen; i++)
    {
        if(place == dict[i])
        {
            repeated=1;
            break;
        }
        else
        {
            count+=1;
        }
    }

    //console.log(exists + " " + count + " " + dictlen + " " + repeated);
    if(count === dictlen && repeated === 0){
        valid=true;
        add_to_list(place);
    }

    else{
        document.getElementById("info").innerHTML = "You Won!!";
        win.style.backgroundColor = "#00dd00";
        win.innerHTML="You Won!"
        win.style.visibility="visible";
        valid=false;
    }
    return valid;
}

// add a valid place to dicts
function add_to_list(place)
{
   if ( place[0] == 'a' )
   { a.push(place); }

   if ( place[0] == 'b' )
   { b.push(place); }

   if ( place[0] == 'c' )
   { c.push(place); }

   if ( place[0] == 'd' )
   { d.push(place); }

   if ( place[0] == 'e' )
   { e.push(place); }

   if ( place[0] == 'f' )
   { f.push(place); }

   if ( place[0] == 'g' )
   { g.push(place); }

   if ( place[0] == 'h' )
   { h.push(place); }

   if ( place[0] == 'i' )
   { i.push(place); }

   if ( place[0] == 'j' )
   { j.push(place); }

   if ( place[0] == 'k' )
   { k.push(place); }

   if ( place[0] == 'l' )
   { l.push(place); }

   if ( place[0] == 'm' )
   { m.push(place); }

   if ( place[0] == 'n' )
   { n.push(place); }

   if ( place[0] == 'o' )
   { o.push(place); }

   if ( place[0] == 'p' )
   { p.push(place); }

   if ( place[0] == 'q' )
   { q.push(place); }

   if ( place[0] == 'r' )
   { r.push(place); }

   if ( place[0] == 's' )
   { s.push(place); }

   if ( place[0] == 't' )
   { t.push(place); }

   if ( place[0] == 'u' )
   { u.push(place); }

   if ( place[0] == 'v' )
   { v.push(place); }

   if ( place[0] == 'w' )
   { w.push(place); }

   if ( place[0] == 'x' )
   { x.push(place); }

   if ( place[0] == 'y' )
   { y.push(place); }

   if ( place[0] == 'z' )
   { z.push(place); }

}
