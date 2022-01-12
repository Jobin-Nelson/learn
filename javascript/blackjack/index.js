let cards = []
let sum = 0
let hasBlackJack = false
let isAlive = false
let message = ''
let messageEl = document.getElementById('message-el')
let sumEl = document.querySelector('#sum-el')
let cardsEl = document.querySelector('#cards-el')
let playerEl = document.getElementById('player-el')

let player = {
	name: 'Jobin',
	chips: 10
}

function startGame(){
	isAlive = true
	let firstCard = getRandomCard()
	let secondCard = getRandomCard()
	cards = [firstCard, secondCard]
	sum = firstCard + secondCard
	renderGame()
}

function renderGame(){
	if (player.chips > 0){
		if (sum < 21) {
			message = 'Do you want to draw a new card?'
		} else if (sum ===21) {
			message = "You've got Blackjack"
			player.chips += 5
			hasBlackJack = true
		} else {
			message = "You're out of the game"
			player.chips --
			isAlive = false
		}
	} else {
		message = 'Sorry you have no chips to play'
	}

	messageEl.textContent = message
	sumEl.textContent = 'Sum: ' + sum
	cardsEl.textContent = 'Cards: '
	playerEl.textContent = player.name + ': $' + player.chips

	for (let i = 0;i < cards.length; i++){
		cardsEl.textContent += cards[i] + ' '
	}
}

function getRandomCard(){
	let randomCard = Math.floor(Math.random()*13) + 1

	if (randomCard > 10){
		randomCard = 10
	} else if (randomCard===1){
		randomCard = 11
	} 

	return randomCard
}

function newCard(){
	if (isAlive===true && hasBlackJack===false){
		let card = getRandomCard()
		sum += card
		cards.push(card)
		renderGame()
	}
}

