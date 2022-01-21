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

console.log(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
console.log(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
console.log(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
console.log(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
console.log(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
