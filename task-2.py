function solution(A, B) {
    const N = A.length;

    // Initialize a 2xN grid to store the minimum maximum values.
    let dp = Array.from({length: 2}, () => Array(N).fill(Infinity));

    // The upper-left corner value is the starting point.
    dp[0][0] = A[0];

    // Fill the dp table.
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < N; j++) {
            // For the first row, we can only move right.
            if (i === 0 && j > 0) {
                dp[i][j] = Math.max(dp[i][j - 1], A[j]);
            }
            // For the second row, we can move right or come from the above cell.
            if (i === 1) {
                let fromAbove = Math.max(dp[i - 1][j], B[j]);
                let fromLeft = j > 0 ? Math.max(dp[i][j - 1], B[j]) : fromAbove;
                dp[i][j] = Math.min(fromAbove, fromLeft);
            }
        }
    }

    // The value in the bottom-right corner is the answer.
    return dp[1][N - 1];
}

// Test cases
console.log(solution([3, 4, 6], [6, 5, 4])); // Should return 5
console.log(solution([1, 2, 1, 7, 1, 4], [1, 1, 1, 3, 1, 1])); // Should return 2
console.log(solution([-5, -1, -3], [-5, 5, -2])); // Should return -1
