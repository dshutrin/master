function up_uitp_count(uid, pid) {
	let new_value = parseInt(document.getElementById(`p-${pid}`).value) + 1

	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/up_uitp_count`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
		if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            document.getElementById(`p-${pid}`).value = new_value
		}
	};

    xhr.send(`uid=${uid}&pid=${pid}`);
}


function down_uitp_count(uid, pid) {
	let new_value = document.getElementById(`p-${pid}`).value - 1

	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/down_uitp_count`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
		if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
		    if (xhr.response['in_trash'] === true) {
                document.getElementById(`p-${pid}`).value = new_value
		    } else {

		        document.getElementById(`dp-${pid}`).innerHTML = `<button type="button" onclick="add_product_to_trash(${uid}, ${pid})" class="catalog-product-link">В корзину</button>`

		    }
		}
	};

    xhr.send(`uid=${uid}&pid=${pid}`);
}


function add_product_to_trash(uid, pid) {

	let xhr = new XMLHttpRequest()
    xhr.open('POST', `/add_product_to_trash`, true)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.responseType = "json"

    xhr.onload = () => {
		if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {

			let div = document.getElementById(`dp-${pid}`)
			div.innerHTML = `<div class="prod-actions">
                                        <button type="button" onclick="down_uitp_count(${uid}, ${pid})">-</button>
                                        <input readonly="" id="p-${pid}" class="catalog-product-count" value="1" type="number">
                                        <button type="button" onclick="up_uitp_count(${uid}, ${pid})">+</button>
                                    </div>`

		}
	};

    xhr.send(`pid=${pid}`);

}




const btnUp = {
  el: document.getElementById('btn_up_id'),
  show() {
    // удалим у кнопки класс btn-up_hide
    this.el.classList.remove('btn-up_hide');
  },
  hide() {
    // добавим к кнопке класс btn-up_hide
    this.el.classList.add('btn-up_hide');
  },
  addEventListener() {
    // при прокрутке содержимого страницы
    window.addEventListener('scroll', () => {
      // определяем величину прокрутки
      const scrollY = window.scrollY || document.documentElement.scrollTop;
      // если страница прокручена больше чем на 400px, то делаем кнопку видимой, иначе скрываем
        console.log(scrollY)
      scrollY > 400 ? this.show() : this.hide();
    });
    // при нажатии на кнопку .btn-up
    document.getElementById('btn_up_id').onclick = () => {
      // переместим в начало страницы
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      });
    }
  }
}

btnUp.addEventListener();
