// can sum with repetition
function canSum(arr, target, memo={}) {
	if (target in memo) return memo[target]
	if (target === 0) return true
	if (target < 0) return false

	for (let num of arr) {
		let remainder = target - num
		if (canSum(arr, remainder, memo)===true) {
			memo[target] = true
			return true
		}
	}
	memo[target] = false
	return false
}


console.log(canSum([2, 3], 7))
console.log(canSum([5, 3, 4, 7], 7))
console.log(canSum([2, 4], 7))
console.log(canSum([2, 3, 5], 7))
