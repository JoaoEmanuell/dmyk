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
    const div_to_body_request = document.createElement("div")
    const link_to_download = document.createElement('a')
    link_to_download.classList.add('text-success')

    if (data.message == "Not Found"){
        div_to_body_request.innerHTML = "<h2>Não existe lançamentos disponíveis!</h2>"
        div_to_body_request.classList.add('text-danger')
    } else{
        release_div.classList.add('shadow-lg', 'p-4', 'rounded', 'bg-light')
        div_to_body_request.innerHTML = `<pre>${data.body}</pre>`
        div_to_body_request.classList.add('text-dark')
        link_to_download.innerHTML = 'Clique aqui para baixar a nova versão!'
        link_to_download.href = data.assets[0].browser_download_url
    }
    release_div.append(div_to_body_request, link_to_download)
})