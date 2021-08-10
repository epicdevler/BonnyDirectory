// search form validation?

const keywords = document.getElementById('keywords')
const locations = document.getElementById('locations')
const categories = document.getElementById('categories')
const SearchForm = document.getElementById('SearchForm')

function searchBtn(){
  SearchForm.addEventListener("submit", (e) => {
    if(keywords.value.trim().length > 0 || locations.value.trim().length > 0 || categories.value.trim().length > 0 ){
    }
    else{
      e.preventDefault()
    }
  });
}



// footer date
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// error and success message alert

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 5000);

// // step by step form

const formSteps = document.querySelectorAll("#AddForm");
const prevBtns = document.querySelectorAll("#back");
const nextBtns = document.querySelectorAll("#next");
const formTabs = document.querySelector("#Forms");
const important = document.querySelectorAll(".important");
const importantF = document.querySelectorAll(".importantF");


// formTabs.addEventListener("submit", (a) => {
//     a.preventDefault();
// });

let formStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum++;
    updateFormSteps();
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
  });
});

function updateFormSteps() {
  formSteps.forEach((formStep) => {
    formStep.classList.contains("first") &&
      formStep.classList.remove("first");
  });

  formSteps[formStepsNum].classList.add("first");
}


