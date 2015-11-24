displayAjaxResult();
drawTokenCanvas();


function displayAjaxResult() {
	$.getJSON('/json/competitions', function (data) {
		$('#ajax').append(JSON.stringify(data));
	});
}


function drawTokenCanvas() {
	var canvas = $('#canvas')[0];
	var ctx = canvas.getContext('2d');


	ctx.fillStyle = 'yellow';
	ctx.fillRect(0, 0, 100, 100);


	var gradient = ctx.createLinearGradient(0, 0, 100, 100);
	gradient.addColorStop(0, '#000');
	gradient.addColorStop(1, '#111');

	ctx.font = '600 40px Arial';
	ctx.textAlign = 'right';
	ctx.textBaseline = 'ideographic';
	ctx.fillStyle = gradient;
	ctx.fillText('JS', 100, 100);
}
