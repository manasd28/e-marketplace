var info = {
    // Laptop Info (Seperate by commas!)
    'laptop-btn1': 'Graph depicting a Heatmap brand, budget and rating where brand is on X-axis, Budget on Y-axis and rating as colors',
    'laptop-btn2': 'Graph depicting a Stacked Bar Plot showing relationship between Brand and the Budgets',
    'laptop-btn3': 'Graph depicting count of products on the various e-commerce platform',
    'laptop-btn4': 'Graph depicting direct realtion between mean price of products of each brand',
    'laptop-btn5': 'Graph depicting relationship between Brands and Processors in Market',
    'laptop-btn6': 'Graph depicting the price distribution on various websites',
    'laptop-btn7': 'Graph showing heatmap of Processor on X-axis, RAM on y axis and count as colors',
    'laptop-btn8': 'Graph depicting relation between SSD availaible and Price Range',
    'ac-btn1': 'fadfa',
    'tv-btn1': 'j0fadffadf'
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