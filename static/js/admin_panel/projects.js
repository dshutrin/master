function delete_project(pid, pcode, pr) {
    document.getElementById('delete_modal').style.display = 'flex'
    document.getElementById('rm-modal-h').innerText = `Вы действительно хотите удалить проект с кодом ${pcode}?`
    document.getElementById('bns').innerHTML = '<button id="cancel-button" type="button" onclick="del_mod()">Отмена</button><button id="rm-button" type="button">Удалить</button>'
    document.getElementById('rm-button').setAttribute('onclick', 'confirm_delete_project('+ pid +', "'+ pr +'")')
}


function confirm_delete_project(pid, pr) {

    let xhr = new XMLHttpRequest();
    xhr.open('POST', `/admin_panel/delete_project`, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.responseType = 'json';

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

            document.getElementById(`delete_modal`).style.display = 'none'
            document.getElementById(`p-${pid}`).remove()

        }
        else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 224){
            document.getElementById('rm-modal-h').innerText = `Нельзя удалить этот проект`
            document.getElementById('bns').innerHTML = '<button id="cancel-button" type="button" onclick="del_mod()">Ок</button>'
        }

    }
    xhr.send(`pid=${pid}&pr=${pr}`)

}

function get_file(url){
    let xhr = new XMLHttpRequest();
    xhr.open('POST', `/get_file`, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.responseType = 'json';
    xhr.send(`url=${url}`)
}
