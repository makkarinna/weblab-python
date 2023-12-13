function getPrice() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;

    const obj = {
        "method": "get-price",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        document.querySelector('#price').innerHTML = `Цена напитка: ${data.result} руб.`;
        document.querySelector('#pay').style.display = '';
        document.querySelector('#cancel_pay').style.display = 'block';
    })
}


function pay() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const cardNum = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;

    const obj = {
        "method": "pay",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            card_num: cardNum,
            cvv: cvv
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        if (data.error) {
            document.querySelector('#pay-status').innerHTML = `Ошибка: ${data.error}`;
        } else {
            document.querySelector('#pay-status').innerHTML = data.result;
            document.querySelector('#pay-status').style.display = 'block';
        }
    });
}

function cancel_pay() {
    const milk = document.querySelector('[name=milk]').checked;
    const sugar = document.querySelector('[name=sugar]').checked;
    const drink = document.querySelector('[name=drink]:checked').value;
    const cardNum = document.querySelector('[name=card]').value;
    const cvv = document.querySelector('[name=cvv]').value;

    const obj = {
        "method": "refund",
        "params": {
            drink: drink,
            milk: milk,
            sugar: sugar,
            card_num: cardNum,
            cvv: cvv
        }
    };

    fetch('/lab7/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(obj)
    })
    .then(function(resp) {
        return resp.json();
    })
    .then(function(data) {
        if (data.error) {
            document.querySelector('#pay-status').innerHTML = `Ошибка: ${data.error}`;
        } else {
            document.querySelector('#pay-status').innerHTML = data.result;
            document.querySelector('#pay-status').style.display = 'block';
        }
    });
}