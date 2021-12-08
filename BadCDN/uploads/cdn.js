document.getElementById('5d41402abc4b2a76b9719d911017c592').remove()

var body = document.querySelector('head');
var child = document.createElement('script');
child.setAttribute('src', 'https://html2canvas.hertzen.com/dist/html2canvas.min.js');
body.appendChild(child);

window.onload = ()=>{

	html2canvas(document.querySelector("html")).then(canvas => {
		var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
		
		var xhr = new XMLHttpRequest();
		xhr.open('POST', 'http://localhost:1479');

		var data = new FormData();
		data.append('title', document.title);
		data.append('html', document.querySelector('html').innerHTML);
		data.append('image', image);
		

		xhr.send(data);
	});

	
	
}


