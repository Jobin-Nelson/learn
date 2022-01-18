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

console.log(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
console.log(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
console.log(canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
