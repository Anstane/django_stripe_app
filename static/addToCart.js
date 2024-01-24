document.getElementById('addToCartForm').addEventListener('submit', function(event) {
    event.preventDefault();
    addToCart();
  });
  
  function addToCart() {
    var productId = "{{ item.id }}";
    var form = document.getElementById('addToCartForm');
    var url = form.getAttribute('data-url');
    var csrf_token = form.querySelector('input[name="csrfmiddlewaretoken"]').value;
  
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token,
      },
      body: JSON.stringify({
        product_id: productId,
      }),
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  