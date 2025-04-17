<script>
	const grid = [
		[3, 7, 4, 7, 6, 5, 7, 9, 3, 9, 1, 3, 2, 6, 7],
		[7, 1, 1, 9, 1, 8, 4, 1, 2, 6, 4, 5, 9, 6, 3],
		[2, 9, 2, 1, 6, 6, 7, 1, 3, 6, 8, 1, 5, 1, 7],
		[9, 8, 5, 4, 1, 4, 3, 1, 9, 4, 6, 5, 8, 1, 2],
		[9, 6, 1, 4, 5, 8, 2, 1, 8, 5, 9, 6, 8, 1, 1],
		[2, 6, 5, 5, 4, 5, 4, 3, 9, 7, 3, 9, 8, 1, 5],
		[9, 1, 6, 2, 4, 3, 2, 7, 9, 9, 7, 4, 7, 6, 2],
		[7, 8, 4, 5, 5, 4, 1, 2, 3, 6, 5, 8, 2, 8, 7],
		[2, 1, 3, 7, 6, 5, 1, 7, 1, 3, 2, 4, 5, 1, 8],
		[3, 6, 3, 9, 6, 6, 6, 4, 1, 2, 4, 2, 5, 5, 2]
	];

	function findRectanglesWithSum10(grid) {
		const rows = grid.length;
		const cols = grid[0].length;

		// 2D prefix sum 배열 생성
		const prefix = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));

		for (let r = 0; r < rows; r++) {
			for (let c = 0; c < cols; c++) {
				prefix[r + 1][c + 1] = grid[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c];
			}
		}

		const results = [];

		// 모든 직사각형 탐색
		for (let r1 = 0; r1 < rows; r1++) {
			for (let c1 = 0; c1 < cols; c1++) {
				for (let r2 = r1; r2 < rows; r2++) {
					for (let c2 = c1; c2 < cols; c2++) {
						const sum =
							prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1];

						if (sum === 10) {
							results.push({ topLeft: [r1, c1], bottomRight: [r2, c2] });
						}
					}
				}
			}
		}

		return results;
	}

	// 실행
	const matches = findRectanglesWithSum10(grid);
	console.log('총 결과 수:', matches.length);
	matches.forEach((rect, i) => {
		console.log(
			`#${i + 1}: From (${rect.topLeft[0]},${rect.topLeft[1]}) to (${rect.bottomRight[0]},${rect.bottomRight[1]})`
		);
	});
</script>
