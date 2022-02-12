
$.getJSON("https://swapi-api.hbtn.io/api/people/5/?format=json", {}, (data) => {
  $('#character').append(data.name)
})

// $.get("https://swapi-api.hbtn.io/api/people/5/?format=json", {}, (data) => {
//   $('#character').append(data.gender)
// })