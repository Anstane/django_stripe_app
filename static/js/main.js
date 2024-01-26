fetch("/config/")
.then((result) => result.json())
.then((data) => {
  const stripe = Stripe(data.publicKey);
  const buyNowBtn = document.getElementById("buy_now_btn");
  const productId = buyNowBtn.getAttribute("data-product-id");
  const checkoutType = buyNowBtn.getAttribute("data-checkout-type")

  buyNowBtn.addEventListener("click", () => {
    let fetchEndpoint = '';

    if (checkoutType === "single") {
      fetchEndpoint = "/buy/";
    } else if (checkoutType === "cart") {
      fetchEndpoint = "/buy-cart/";
    }

    if (productId) {
      fetchEndpoint += productId;
    }

    fetch(fetchEndpoint)
      .then((result) => { return result.json(); })
      .then((data) => { return stripe.redirectToCheckout({ sessionId: data.sessionId }) })
      .then((res) => console.log(res))
      .catch((error) => console.error(error));
  });
});
