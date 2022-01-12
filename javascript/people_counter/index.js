let countEl = document.getElementById('count-el')
let saveEl = document.getElementById('save-el')
let count = 0

function increment(){
	count++
	countEl.textCounter = count
}

function save(){
	saveEl.textContent +=  count + ' - ' 
	count = 0
	countEl.textContent = count
}
