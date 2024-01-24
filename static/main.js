console.log("Sanity check!");

fetch("/config/")
.then((result) => { return result.json(); })
.then((data) => {
  const stripe = Stripe(data.publicKey);
  const buyNowBtn = document.getElementById("buy_now_btn");
  const productId = buyNowBtn.getAttribute("data-product-id")

  buyNowBtn.addEventListener("click", () => {
    fetch(`/buy/${productId}/`)
    .then((result) => { return result.json(); })
    .then((data) => {
      return stripe.redirectToCheckout({ sessionId: data.sessionId })
    })
    .then((res) => {
      console.log(res);
    })
  });
});
