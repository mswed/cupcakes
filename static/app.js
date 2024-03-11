const addCupcakeBtn = document.querySelector('button')
const cupcakeList = document.querySelector('ul')

document.addEventListener('DOMContentLoaded', async function(evt) {
    const cupcakes = await axios.get('/api/cupcakes');
    for (let cc of cupcakes.data.cupcakes) {
        const li = document.createElement('li')
        const card = document.createElement('div')
        card.classList.add('card');
        card.style.width = '18rem';
        const img = document.createElement('img')
        img.src = cc.image
        img.classList.add('card-img-top')
        const cardBody = document.createElement('div')
        cardBody.classList.add('card-body')
        const cardTitle = document.createElement('h5')
        cardTitle.classList.add('card-title')
        cardTitle.innerText = cc.flavor
        const cardDetails = document.createElement('ul')
        const size = document.createElement('li')
        size.innerText = cc.size
        const rating = document.createElement('li')
        rating.innerText = cc.rating
        cardDetails.append(rating)
        cardDetails.append(size)
        card.append(img)
        card.append(cardBody)
        cardBody.append(cardTitle)
        cardBody.append(cardDetails)
        li.append(card)
        cupcakeList.append(li)

    }
})

addCupcakeBtn.addEventListener("click", async function(evt) {
    evt.preventDefault()
    
    const newCupcake = await axios.post('/api/cupcakes');
})

