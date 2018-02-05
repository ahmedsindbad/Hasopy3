var toggle = function() {
	var mydiv = document.getElementById('newpost');
	if (mydiv.style.display === 'block' || mydiv.style.display === '')
		mydiv.style.display = 'none';
	else
		mydiv.style.display = 'block'
}
