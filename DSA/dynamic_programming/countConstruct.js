// Write a function countConstruct(target, wordBank)
// The function should return the number of ways that the target can be constructed by concatenating elements of the wordbank array
// You may resuse elements of the wordbank as many times as necessary

function countConstruct(target, wordBank, memo={}) {
	if (target in memo) return memo[target]
	if (target==='') return 1
	
	let totalCount = 0

	for (let word of wordBank) {
		if (target.indexOf(word)===0) {
			totalCount += countConstruct(target.slice(word.length), wordBank, memo)
		}
	}

	memo[target] = totalCount
	return totalCount
}

// tabulation
function countConstructTab(target, wordBank) {
	let dp = Array(target.length + 1).fill(0)
	dp[0] = 1

	for (let i=0; i<= target.length; i++) {
		if (dp[i] > 0) {
			for (let word of wordBank) {
				if (target.slice(i,i + word.length) === word) {
					dp[i + word.length] += dp[i]  
				}
			}
		}
	}

	return dp[target.length]
}

console.log(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
console.log(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
console.log(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
console.log(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
console.log(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))

console.log(countConstructTab('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
console.log(countConstructTab('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
console.log(countConstructTab('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
console.log(countConstructTab('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
console.log(countConstructTab('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
