
const url = '/api/cupcakes'
const list = document.getElementById('list');
const form = document.getElementById('cupcake-form');

function loadCupcakes(cupcakes){
    list.innerHTML = '';
    for(let cupcake of cupcakes){
        let li = document.createElement('li');
        let content = `flavor: ${cupcake.flavor} \n`;
        content += `rating: ${cupcake.rating} \n`
        content += `size: ${cupcake.size} \n`
        li.innerText = content;
        li.innerHTML += `<img style='max-width: 5vw; height: auto;' src='${cupcake.image}' />`;
        list.append(li);
    }
}


async function getCupcakes(){
    let cupcakes = await fetch(url)
        .then(resp => {
            if(!resp.ok){
                throw new Error(`Error! Status Code: ${resp.status}`);
            }
            return resp.json();
        })
        .then(data => {
            return data.cupcakes;    
        })
        .catch(err => {
            console.error(error);
        }); 

    loadCupcakes(cupcakes);
}

form.addEventListener('submit', async function(evt){
    evt.preventDefault(); 
    let body = {};
    const elements = form.querySelectorAll('input[type="text"]');
    for(let child of elements){
        body[child.name] = child.value; 
    }
    body = JSON.stringify(body);
    await fetch(url, {headers: {"Content-Type": "application/json"}, method: "POST", body})
        .then(resp => {
            if(!resp.ok){
                throw new Error(`Error! Status: ${resp.status}`);
            }
            else{
                getCupcakes(); 
            }
        })
        .catch(error => {
            console.error(error);
        })

    for(let child of elements){
        child.value='';
    }
});

getCupcakes();
 

