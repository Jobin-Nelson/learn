// Write a function canConstruct(target, wordBank)
// The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array
// You may reuse elements of the wordBank as many times as necessary

function canConstruct(target, wordBank, memo={}) {
	if (target in memo) return memo[target]
	if (target==='') return true

	for (let word of wordBank) {
		if (target.indexOf(word) ===0) {
			let suffix = target.slice(word.length)
			if (canConstruct(suffix, wordBank, memo) === true) {
				memo[target] = true
				return true
			}
		}
	}

	memo[target] = false
	return false
}

// tabulation
function canConstructTab(target, wordBank) {
	let dp = Array(target.length + 1).fill(false)
	dp[0] = true

	for (let i=0; i<=target.length; i++) {
		if (dp[i] === true) {
			for (let word of wordBank) {
				let len = word.length
				if (target.slice(i, i + len) === word) {
					dp[i + len] = true
				}
			}
		}
	}

	return dp[target.length]
}

console.log(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
console.log(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
console.log(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))

console.log(canConstructTab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
console.log(canConstructTab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
console.log(canConstructTab('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
