// alert("This website is under continuous development... \nThere are still many features yet to be completed.")

let data_path = "./data.json";

async function get_data(){
    try{
        const responce = await fetch(data_path);
        if(!responce.ok){
            throw new Error("抓取資料錯誤!")
        };
        const data = await responce.json();
        let movieList = document.querySelector(".movieList");
        document.querySelector('.movie .movieName').textContent = data[0].name;
        document.querySelector('.movie img').src = data[0].img;
        document.querySelector('.movie img').onload = function(){
            this.style.width = this.naturalWidth / 4 + "px";
        };
        for(let i=1; i<5; i++){
            let movieTemplate = document.querySelector('.movie').cloneNode(true);
            movieTemplate.querySelector('.movieName').textContent = data[i].name;
            movieTemplate.querySelector('img').src = data[i].img;
            movieTemplate.querySelector('img').onload = function(){
                this.style.width = this.naturalWidth / 4 + "px";
            }
            movieList.appendChild(movieTemplate);
        };
    }catch(error){
        console.error(error);
    };
};
get_data()
// fetch(data_path).then(function(responce){
//     return responce.json();
// }).then(function(json){
//     console.log(json)
// }).catch(function(error){
//     console.log(error);
// })

// let greet = new Promise(function(resolve, reject){
//     try{
//         resolve((function(){
//             console.log("你好!")
//             console.log(水嗎)
//             return "你叫什麼名子?"
//         })());
//     }catch{
//         reject("發生錯誤");
//     };
// });

// greet.then(function(responce){

//     console.log(responce);

// }).catch(function(error){

//     console.log(error);
// });