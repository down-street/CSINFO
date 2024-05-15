document.addEventListener("DOMContentLoaded", function() {
    var backToTopButton = document.getElementById("back-to-top");

    // 监听滚动事件
    window.addEventListener("scroll", function() {
        if (window.scrollY > 300) {
            backToTopButton.style.display = "block";
        } else {
            backToTopButton.style.display = "none";
        }
    });

    // 监听按钮点击事件
    backToTopButton.addEventListener("click", function() {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
});
