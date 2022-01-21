// Write a function(target, wordBank)
// The function should return a 2D array containing all of the ways that the target can be constructed by concatenting elements of the wordBank array. Each element of the 2D array should represent one combination that constructs the target
// You may reuse the elements of wordBank as many times as necessary


function allConstruct(target, wordBank, memo={}) {
	if (target in memo) return memo[target]
	if (target==='') return [[]]

	const result = []

	for (let word of wordBank) {
		if (target.indexOf(word) === 0) {
			const suffixWays = allConstruct(target.slice(word.length), wordBank, memo)
			const targetWays = suffixWays.map(way => [word, ...way])

			result.push(...targetWays)
		}
	}

	memo[target] = result
	return result
}

console.log(allConstruct('purple', ['purp', 'p', 'purpl', 'le', 'ur', 'e']))
console.log(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
console.log(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaz', ['a', 'aaa', 'aa', 'aaa', 'aaaa',]))
