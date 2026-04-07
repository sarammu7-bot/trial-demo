fetch("http://52.54.189.78:5000/api")
  .then(res => res.json())
  .then(data => {
    const el = document.createElement("h2");
    el.innerText = data.message;
    document.body.appendChild(el);
  });
