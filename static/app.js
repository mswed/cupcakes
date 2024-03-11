const flavorField = document.querySelector('#flavor')
const sizeField = document.querySelector('#size')
const ratingField = document.querySelector('#rating')
const imageField = document.querySelector('#image')
const addCupcakeBtn = document.querySelector('button')
const cupcakeList = document.querySelector('ul')

function renderCupcake(cc) {
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
    cardDetails.append(size)
    cardDetails.append(rating)
    card.append(img)
    card.append(cardBody)
    cardBody.append(cardTitle)
    cardBody.append(cardDetails)
    li.append(card)
    cupcakeList.append(li)
}
document.addEventListener('DOMContentLoaded', async function(evt) {
    const cupcakes = await axios.get('/api/cupcakes');
    for (let cc of cupcakes.data.cupcakes) {
        renderCupcake(cc)

    }
})

addCupcakeBtn.addEventListener("click", async function(evt) {
    evt.preventDefault()
    const data = {flavor: flavorField.value, size: sizeField.value,
        rating: ratingField.value, image: imageField.value}
    
    const newCupcake = await axios.post('/api/cupcakes', data);
    console.log(newCupcake);
    renderCupcake(newCupcake.data.cupcake);
})

