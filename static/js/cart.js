var updateBtns = document.getElementsByClassName('update-cart')

for(i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var itemId = this.dataset.item
        var action = this.dataset.action
        console.log('itemId:', itemId, 'action:', action)


        console.log('USER:' , user)
        if(user === 'AnonymousUser'){
            console.log('not logged in ')
        }
        else{
            updateUserOrder(itemId, action)
        }

    })
}

function updateUserOrder(itemId, action){
    console.log('sending data')
    var url = '/update-item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'itemId': itemId, 'action' :action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
    })
}