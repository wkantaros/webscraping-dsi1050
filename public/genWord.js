const API_URL = window.location.href

let jsbtn = document.getElementById('js-render-btn')

jsbtn.addEventListener("click", () => {
    fetch('http://localhost:8080/genword')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        if (document.getElementById('js-val')){
            document.getElementById('js-val').innerText = 'product: ' + data.keyword
        } else {
            let node = document.createElement('p'); // Create a <p> node
            node.setAttribute("id", "js-val");
            let textnode = document.createTextNode('product: ' + data.keyword);
            node.appendChild(textnode);
            document.getElementById("main").appendChild(node);
        }
    })
});