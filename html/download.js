const release_api_endpoint = "https://api.github.com/repos/JoaoEmanuell/dmyk/releases/latest"
const release_div = document.querySelector("#div-last-download")

async function request_get(url=''){
    const response = await fetch(url, {
        method: "GET",
        mode: "cors",
        cache: "default",
        credentials: "same-origin",
        headers: {
            "Content-type": "application/json"
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
    })
    return response.json()
}

request_get(release_api_endpoint).then((data) => {

    if (data.message == "Not Found"){
        window.alert("Não existe lançamentos!")
    } else{
        const div_to_body_request = document.createElement("div")
        div_to_body_request.classList.add()
        div_to_body_request.innerHTML = `<pre>${data.body}</pre>`

        const link_to_download = document.createElement('a')
        link_to_download.innerHTML = 'Clique aqui para baixar a nova versão!'
        link_to_download.href = data.assets[0].browser_download_url
        
        release_div.append(div_to_body_request, link_to_download)
    }
})