function show_more(){
    let xhr = new XMLHttpRequest()
    xhr.open('POST', `/show_more_projects`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var projects = xhr.response['projects']
            var html = ''

            for (var i=0;i<projects.length; i++){
                html += '<div id="pr-' + projects[i]['id'] + '" class="project"><div class="image-hold"><img class="proj-im" src="'+ projects[i]['photo'] +'" alt=""></div><div class="name-holder"><h3>'+ projects[i]['name'] +'</h3></div></div></div>'
            }

            document.getElementById('prjs').innerHTML = html

            for (var i=0;i<projects.length; i++){
                document.getElementById('pr-'+ projects[i]['id']).setAttribute('onclick', 'location.href="/ready_project/'+ projects[i]['id'] +'"')
            }
            document.getElementById('more').style.display = 'none'
        }
    };

    xhr.send();
}
