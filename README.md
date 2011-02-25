---------------------
COLOMBIA TRANSPARENTE
---------------------
Descripción: 


-------
Modelos
-------

promesas
  id - int
  titulo - text
  descripción - text (parsed)
  estatus - int
  arriba - int
  abajo - int
  slug - text
  shared - int
  
// y los estados son:
ESTATUS_OPCIONES={0:"Estancado", 1:"En proceso", 2:"Incumplida", 3:"A medias", 4:"Cumplida"}

// el scorecard está formado por una lista de cinco elementos (uno por cada estado). Cada elemento es una lista con dos valores: un entero (cantidad) y un decimal (porcentaje). Un ejemplo a continuación:
SCORECARD=[[23,10],[40,20],[500,50],[30,15],[5,5]]

etiquetas // las etiquetas representan temáticas. Crowdsourced.
  titulo (PK) - text
  descripcion - text (parsed)

personajes // no es Crowdsourced.
  id (PK) - int
  nombre - text - unique
  slug - text
  descipción - text (parsed)
  image - text (path)

cargos // no es Crowdsourced.
  id (PK) - int
  personaje (FK) - int
  título - texto
  inicio - datetime
  termininacion - datetime (null)

// tenemos dos tablas intermedias: PromesaEtiqueta y PromesaCargo


------
Vistas
------

HOME -> /
- búsqueda única: utiliza etiquetas (autocomplete), texto libre, personajes (autocomplete), estatus (autocomplete)
- nota: reemplácese a continuación {algunas} por un número definido en backend
- marquee horizontal parecido al home de twitter de etiquetas, personajes-cargo que pasan de derecha a izquierda. Si el usuarios presiona cualquier promesa, se cargan (ajax) {algunas} promesas mas relevantes en el listado. Por defecto por el marquee pasan {algunas} etiquetas más relevantes.
- las más relevantes (etiquetas y promesas): eso lo define el algoritmo en backend de Julián.
- por defecto cargamos {algunas} promesas.
- (no para Hackathon) si el usuario se desplaza hacia abajo, obtenemos más promesas y las mostramos automáticamente

PERSONAJE -> /personaje/{nombre}
- cuando se presiona vinculo "otros cargos" se muestra un listado (scrollable) de los otros cargos ejercidos con sus periodos. Si se selecciona uno de los cargos, se cambia el scorecard y el listado de promesas respecto al cargo seleccionado (ajax).

ETIQUETA -> /etiqueta/{titulo}

PROMESA -> /promesa/{slug}


---------------------
Otras consideraciones
---------------------

- En las columnas tipo text con bandera "parsed" se filtrarán las etiquetas. Las únicas permitidas son: p, a, ref
- Las fuentes que soportan los textos de la descripción se incluyen como "ref elements" en la descripción. Dentro de un ref element hay otro markup especial para incluir el texto y el enlace. El enlace es opcional. Si no hay markup solo se utiliza el texto.

Django: 
- media folder -> e.g. <img src="{{MEDIA_URL}}img/miimage.jpg"></a>
  images: img
  javascripts: scripts