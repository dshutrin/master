document.getElementById('id_video').addEventListener('change', () => {
    document.getElementById('label_id_video').innerText = document.getElementById('id_video').value
})

document.getElementById('id_video').setAttribute('accept', 'video/*')

function clear_vid() {
    document.getElementById('id_video').value = null
    document.getElementById('label_id_video').innerText = 'Видео'
}



function change_l(){
    document.getElementById(`l-1`).innerText = document.getElementById('1').value
}
