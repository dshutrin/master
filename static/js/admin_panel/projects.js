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

function calc_change_tos(cpid){

    let xhr = new XMLHttpRequest();
    if (document.getElementById(`inp-${cpid}`).checked){
        xhr.open('POST', `/admin_panel/do_tos`, true);
    }
    else{
        xhr.open('POST', `/admin_panel/undo_tos`, true);
    }

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.responseType = 'json';

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {


        }
        else{
            if (document.getElementById(`inp-${cpid}`).checked){
                document.getElementById(`inp-${cpid}`).setAttribute('checked', '')
            }
            else{
                document.getElementById(`inp-${cpid}`).setAttribute('checked', 'checked')
            }
        }

    }
    xhr.send(`id=${cpid}&pr=c`)

}


function ready_change_tos(rpid){

    let xhr = new XMLHttpRequest();
    if (document.getElementById(`inp-${rpid}`).checked){
        xhr.open('POST', `/admin_panel/do_tos`, true);
    }
    else{
        xhr.open('POST', `/admin_panel/undo_tos`, true);
    }

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.responseType = 'json';

    xhr.onload = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

        }
        else{
            if (document.getElementById(`inp-${rpid}`).checked){
                document.getElementById(`inp-${rpid}`).setAttribute('checked', '')
            }
            else{
                document.getElementById(`inp-${rpid}`).setAttribute('checked', 'checked')
            }

        }

    }
    xhr.send(`id=${rpid}&pr=r`)

}
