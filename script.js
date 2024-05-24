let searchForm = document.querySelector(".search-form");

// 寫法1
// document.querySelector("#search-btn").onclick = function(){
//     searchForm.classList.toggle("active");
// }; // 在這裡只能放置"準備執行"的狀態，而不是立即執行。

// 寫法2
document.querySelector("#search-btn").addEventListener("click",function(){
    searchForm.classList.toggle("active");
});

let menuButton = document.querySelector(".icon #menu-btn");
menuButton.addEventListener("click",function(){
    let menu = document.querySelector(".header .menu");
    menu.classList.toggle("show");
});

window.onscroll = function(){
    let menu = document.querySelector(".header .menu");
    let searchForm = document.querySelector(".search-form");
    searchForm.classList.remove("active");
    menu.classList.remove("show");
    if(window.scrollY>0){
        document.querySelector(".header").classList.add("active");
    }else{
        document.querySelector(".header").classList.remove("active");
    }
}


window.onload = function(){
    let home_slider = document.querySelector("section .home-slider");
    let header = document.querySelector("header");
    let headerHeight = window.getComputedStyle(header).getPropertyValue('height');
    home_slider.style.marginTop = headerHeight;
};

window.onscroll = function(){
    let home_slider = document.querySelector("section .home-slider");
    let header = document.querySelector("header");
    let headerHeight = window.getComputedStyle(header).getPropertyValue('height');
    home_slider.style.marginTop = headerHeight;
};

let btn = document.querySelectorAll("section button")
for(let i of btn){
    i.addEventListener("click",function(){
        window.location = "https://www.google.com.tw/";
    });
};