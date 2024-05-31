function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return rect.top > window.innerHeight // || rect.bottom < 0 
}

function addClassToVisibleElements() {
    var elements = document.querySelectorAll("#movie .movie");
    elements.forEach(function (e) {
        if (!isElementInViewport(e)){
            e.classList.add("active");
            setTimeout(
                function(){
                    e.querySelector("h3").classList.add("active");
                },
                300
            )
            setTimeout(
                function(){
                    e.querySelector("p").classList.add("active");
                },
                100
            )
            setTimeout(
                function(){
                    e.querySelector("img").classList.add("active");
                },
                100
            )
        }
        else {
            e.classList.remove("active");
            e.querySelector("h3").classList.remove("active");
            e.querySelector("p").classList.remove("active");
            e.querySelector("img").classList.remove("active");
        };
    });
}

document.addEventListener("scroll", addClassToVisibleElements);
addClassToVisibleElements();