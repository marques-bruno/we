var pageContent = document.getElementById("content"),
	pagecopy = pageContent.cloneNode(true),
	blurryContent = document.getElementById("blurryscroll");
	blurryContent.appendChild(pagecopy);
	window.onscroll = function() { blurryContent.scrollTop = window.pageYOffset; }