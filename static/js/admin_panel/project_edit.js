function delete_photo(phid, pr){

    let xhr = new XMLHttpRequest();
    xhr.open('POST', `/admin_panel/delete_ph_proj/${phid}`, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.responseType = 'json';
    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            document.getElementById(`ph-${phid}`).remove()

        }
    }
    xhr.send(`pr=${pr}`);
}

function change_l(){
    document.getElementById(`l-1`).innerText = document.getElementById('1').value
}
