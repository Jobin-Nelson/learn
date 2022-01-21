// Write a function bestSum(targetSum, numbers)
// The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum

function bestSum(targetSum, numbers, memo={}) {
	if (targetSum in memo) return memo[targetSum]
	if (targetSum === 0) return []
	if (targetSum < 0) return null

	let shortestCombination = null

	for (let num of numbers) {
		let remainder = targetSum - num
		let remainderResult = bestSum(remainder, numbers, memo)
		
		if (remainderResult != null) {
			let combination = [...remainderResult, num]

			if (shortestCombination === null || combination.length < shortestCombination.length) {
				shortestCombination = combination
			}
		}
	}

	memo[targetSum] = shortestCombination
	return shortestCombination
}

// tabulation
function bestSumTab(targetSum, numbers) {
	dp = Array(targetSum+1).fill(null)
	dp[0] = []

	for (let i=0; i<=targetSum; i++) {
		if (dp[i] != null) {
			for (let num of numbers) {
				let combination = [...dp[i], num]

				if (!dp[i+num] || dp[i+num].length > combination.length) {
					dp[i+num] = combination
				}
			}
		}
	}

	return dp[targetSum]
}

console.log(bestSum(7, [5, 3, 4, 7]))
console.log(bestSum(8, [2, 3, 5]))
console.log(bestSum(8, [5, 4, 5]))
console.log(bestSum(7, [5, 3, 4, 7]))
console.log(bestSum(100, [1, 2, 5, 25]))

console.log(bestSumTab(7, [5, 3, 4, 7]))
console.log(bestSumTab(8, [2, 3, 5]))
console.log(bestSumTab(8, [5, 4, 5]))
console.log(bestSumTab(7, [5, 3, 4, 7]))
console.log(bestSumTab(100, [1, 2, 5, 25]))
