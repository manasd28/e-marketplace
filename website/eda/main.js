var info = {
    // Laptop Info (Seperate by commas!)
    'laptop-btn1': 'Graph depicting a Heatmap brand, budget and rating where brand is on X-axis, Budget on Y-axis and rating as colors',
    'laptop-btn2': 'Graph depicting a Stacked Bar Plot showing relationship between Brand and the Budgets',
    'laptop-btn3': '',
    'laptop-btn4': '',
    'laptop-btn5': '',
    'laptop-btn6': '',
    'laptop-btn7': '',
    'laptop-btn8': '',
    // Mobile Info (Seperate by commas!)
}

document.querySelectorAll(".btn").forEach((item) => {
    item.addEventListener("click", (event) => {
        let image = document.getElementById("image");
        let href = event.target.getAttribute("img-src");
        let id = event.target.getAttribute("id")
        document.getElementById("text-block").innerHTML = info[id];
        image.setAttribute("src", href);
    });
  });