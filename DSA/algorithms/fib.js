// recursion
function fibRec(ind) {
	if (ind <= 2) return 1
	return fibRec(ind-1) + fibRec(ind-2)
}

//memoization with no recursion
function fibMem(n) {
	let dp = [...Array(n)]
	dp[0] = 0
	dp[1] = 1

	for (i=2; i<=n; i++) {
		dp[i] = dp[i-1] + dp[i-2]
	}

	return dp[n]
}

// memoization with hashmap
function fibMemoization(n, memo={}){
	if (n in memo) return memo[n]
	if (n <= 2) return 1
	memo[n] = fibMemoization(n-1, memo) + fibMemoization(n-2, memo)
	return memo[n]
}

console.log(fibRec(6))
console.log(fibRec(7))
console.log(fibRec(8))

console.log(fibMem(6))
console.log(fibMem(7))
console.log(fibMem(8))

console.log(fibMemoization(6))
console.log(fibMemoization(7))
console.log(fibMemoization(8))
