var pic_src;
var title;
var text;

function takeText(event) {
	pic_src = event.getElementsByTagName('img')[0].src;
	title = event.getElementsByTagName('h1')[0].innerText;
	text = event.getElementsByTagName('p')[0].innerText;
	window.location.href = "../html/point.html?src=" + pic_src + "&title=" + title + "&text=" + text;
}

// 当用户滚动时，显示或隐藏回到顶部按钮
window.addEventListener("scroll", function() {
	var backToTopButton = document.getElementById("back-to-top");
	if (window.pageYOffset > 100) { // 当滚动距离大于100像素时显示按钮
	  backToTopButton.style.display = "block";
	} else {
	  backToTopButton.style.display = "none";
	}
  });
  
  // 当用户点击回到顶部按钮时，滚动到页面顶部
  function scrollToTop() {
	window.scrollTo({
	  top: 0,
	  behavior: "smooth"
	});
  }
  
  // 绑定点击事件到回到顶部按钮
  document.getElementById("back-to-top").addEventListener("click", scrollToTop);