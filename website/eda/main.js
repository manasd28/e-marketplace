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
    "tv-btn1" : "Bar Graph depicting the relation between resolution and Price",
    "tv-btn2" : "Graph depicting relation between different TV brands and their ratings",
    "tv-btn3" : "Graph depicting the relation between different TV brands and their price",
    "tv-btn4" : "Graph depicting which brands of TV are most frequent",
    "tv-btn5" : "Correlation-Heatmap",
    "tv-btn6" : "Graph depicting BoxPlot of Price",
    "tv-btn7" : "Graph depicting relations between ratings between and no. of products of a brand",
    "tv-btn8" : "Graph depicting the relation between ratings and Price",
    "tv-btn9" : "Graph depicting the relation between refresh rate and Price",
    "tv-btn10" : "Graph depicting the relation between audio and Price",
    "ac-btn1" : "Graph depicting BoxPlot of Price",
    "ac-btn2" : "Graph depicting budget of Split/Windows AC",
    "ac-btn3" : "Word Cloud of most popular AC brands",
    "ac-btn4" : "HeatMap of different AC brands and their power consumptions",
    "ac-btn5" : "Graph depicting heatmap of various AC brands",
    "ac-btn6" : "Graph depicting the heatmap of various sizes of different brands of AC",
    "ac-btn7" : "Graph depicting the CountPlot of Noise Level",
    "fridge-btn1" : "Graph depicting the relation between various brands of Fridge and Price of them",
    "fridge-btn2" : "Graph depicting which brands of TV are most frequent",
    "fridge-btn3" : "Graph depicting the relation between capacity and Price",
    "fridge-btn4" : "Correlation-Heatmap",
    "fridge-btn5" : "Graph depicting the relation between Doube-Door Fridges and their respective Prices",
    "fridge-btn6" : "Graph depicting BoxPlot of Price",
    "fridge-btn7" : "Graph depicting the relation between ratings and Price",
    "fridge-btn8" : "Graph depicting the relation between Star Ratings and Prices",
    "mobile-btn1" : "Graph depicting the relation between budgets and their ratings",
    "mobile-btn2" : "Graph depicting the relation between brands and budget",
    "mobile-btn3" : "Graph depicting which brands of mobile are most frequent",
    "mobile-btn4" : "Graph depicting the relation between brands and Prices",
    "mobile-btn5" : "Graph depicting the relation between brands and RAM",
    "mobile-btn6" : "Graph depicting the relation between brands and their ratings",
    "mobile-btn7" : "Graph depicting BoxPlot of Price",
    "mobile-btn8" : "Graph depicting the relation between RAM and Prices",
    "mobile-btn9" : "Graph depicting the relation between RAM and Storage",
    "camera-btn1" : "Word Cloud Of most popular brand names",
    "camera-btn2" : "Graph depicting the relation between Budget and Pixels",
    "camera-btn3" : "Graph depicting BoxPlot of Price",
    "camera-btn4" : "Graph depicting the relation between Budgets and Ratings",
    "camera-btn5" : "Graph depicting the CountPlot of Top 10 Camera Brands",
    "camera-btn6" : "Graph depicting the CountPlot of All Camera Brands",
    "camera-btn7" : "Top 10 Camera brands",
    // Camera Info (Seperate by commas!)
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