function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return rect.bottom < 0 || rect.top > window.innerHeight;
}

function addClassToVisibleElements() {
    var elements = document.querySelectorAll("#movie .movie");
    elements.forEach(function (e) {
        if (!isElementInViewport(e)){
            e.classList.add("ed");
        }
        else {
            e.classList.remove("ed");
        };
    });
}

document.addEventListener("scroll", addClassToVisibleElements);
addClassToVisibleElements();