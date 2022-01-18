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

console.log(bestSum(7, [5, 3, 4, 7]))
console.log(bestSum(8, [2, 3, 5]))
console.log(bestSum(8, [5, 4, 5]))
console.log(bestSum(7, [5, 3, 4, 7]))
console.log(bestSum(100, [1, 2, 5, 25]))

