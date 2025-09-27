
document.querySelector('.btn').addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector('#services').scrollIntoView({
        behavior: 'smooth'
    });
});


const header = document.getElementById('header');
const stickyClass = 'sticky';

window.onscroll = function() {
    if (window.pageYOffset > 100) {
        header.classList.add(stickyClass);
    } else {
        header.classList.remove(stickyClass);
    }
};


const serviceImages = document.querySelectorAll('.service img');
serviceImages.forEach((img) => {
    img.addEventListener('mouseenter', function () {
        img.style.transform = 'scale(1.05)';
        img.style.transition = 'transform 0.3s ease-in-out';
    });

    img.addEventListener('mouseleave', function () {
        img.style.transform = 'scale(1)';
    });
});
