<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	export let data = [];
	let canvas;
	let chart;

	$: if (chart && data) {
		chart.data.labels = data.map((reading) => {
			const date = new Date(reading.timestamp);
			return date.toLocaleTimeString();
		});
		chart.data.datasets[0].data = data.map((reading) => reading.temperature);
		chart.update();
	}

	onMount(() => {
		chart = new Chart(canvas, {
			type: 'line',
			data: {
				labels: [],
				datasets: [
					{
						label: 'Temperature (°C)',
						data: [],
						borderColor: '#3498db',
						tension: 0.4,
						fill: false
					}
				]
			},
			options: {
				responsive: true,
				animation: {
					duration: 0 // Disable animations for real-time updates
				},
				scales: {
					y: {
						beginAtZero: false,
						suggestedMin: 15,
						suggestedMax: 30
					}
				}
			}
		});

		return () => {
			if (chart) chart.destroy();
		};
	});
</script>

<canvas bind:this={canvas}></canvas>
