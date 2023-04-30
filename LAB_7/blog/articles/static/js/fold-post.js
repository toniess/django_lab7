function getArticle(el) {
   if (el.parentElement.parentElement.className == "one-post folded") {
      el.innerHTML = "Развернуть";
      el.parentElement.parentElement.className = "one-post";
   }
   else {
      el.innerHTML = "Свернуть";
      el.parentElement.parentElement.className = "one-post folded"
   }
}