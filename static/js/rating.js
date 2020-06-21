let vote_value = Number(document.getElementById("user_rating").value);
let elements = document.querySelectorAll('.fa-star');
let star_count = 10;

function loadRating()
    {
      for (let i = 0; i < vote_value; i++) {
        elements[i].style.color = 'orange';
  }
   }
window.onload = loadRating;


function s(value) {

  let target = event.target;
  let i = 0;
  vote_value = value
  while (i != vote_value) {
    elements[i].style.color = 'orange';
    i++
  }
  document.getElementById("id_rating_value").value = value
  document.ratingScale.submit();
}

wrap.onmouseover = function (event) {

  let target = event.target;
  if (target != wrap)
  { let i = 0;

    while (i < star_count) {
     elements[i].style.color = '';
     i++
   }

    i = 0;
    while (elements[i] != target && i < star_count) {
      elements[i].style.color = 'orange';
      i++
    }
   target.style.color = 'orange';
  }
};

wrap.onmouseout = function (event) {
  let target = event.target;
  
  if (event.relatedTarget != wrap){
  for (let i = 0; i < star_count; i++) {
    elements[i].style.color = '';

  }
  
  for (let i = 0; i < vote_value; i++) {
    elements[i].style.color = 'orange';

  }
  }
};