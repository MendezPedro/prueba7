
function getComuna(){
    region = document.getElementById('select').value // un numero (ID DE LA REGION)
    console.log(region)

    fetch(`http://localhost:8000/fetch_data/${region}`) //-> http://localhost:8000/fetch_data/1
    .then((response)=> response.json())
    .then((regiones) => {
      console.log(regiones)

      renderCiudades(regiones)
    })
  };


