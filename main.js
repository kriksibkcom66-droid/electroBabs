let imgContainer = document.querySelector('.img__conteiner')

setInterval(() => {
    let firstImg = imgContainer.firstElementChild;
    firstImg.remove();
    imgContainer.appendChild(firstImg);
}, 2500);