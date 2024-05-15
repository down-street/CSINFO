document.addEventListener('DOMContentLoaded', function () {
    var navToggle = document.getElementById('nav_toggle');
    var navMenu = document.getElementById('nav_menu');

    navToggle.addEventListener('click', function () {
        if (navMenu.style.display === 'block') {
            navMenu.style.display = 'none';
        } else {
            // 获取按钮的位置和大小
            var rect = navToggle.getBoundingClientRect();
            // 设置菜单的位置
            navMenu.style.top = (rect.bottom + window.scrollY) + 'px';
            navMenu.style.display = 'block';
        }
    });

    window.addEventListener('resize', function () {
        if (window.innerWidth > 1000) {
            navMenu.style.display = 'none';
        }
    });
    window.addEventListener('scroll', function() {
        if (navMenu.style.display === 'block') {
            var rect = navToggle.getBoundingClientRect();
            navMenu.style.top = (rect.bottom + window.scrollY) + 'px';
        }
    });
});
