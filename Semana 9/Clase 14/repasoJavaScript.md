# JavaScript
## _Lenguaje de programación utilizado del lado del cliente para dinamizar páginas web._

A pesar de su propósito principal con la web, puedes utilizarlo en diversos campos de la programación y entornos de ejecución.

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/500px-JavaScript-logo.png" alt="Descripción" width="300"/>
</div>

## Funciones
Las funciones en JavaScript son similares a las de otros lenguajes. Permiten ejecutar cierto bloque de código cuando estas son 'invocadas' y reducen la repetición de código.

Como el paradigma de programación funcional está presente, puedes asignar funciones a variables o 'pasar' funciones como parámetros (callback).

Hay tres formas principales de definir una función en JavaScript:

- ### Palabra reservada: _function_
```js
    function sumar(a, b) {
        return a + b;
    }
```

- ### Asignar una función a una variable
```js
    const sumar = (a, b) => a + b;
```

- ### Función flecha anónima
El ejemplo más común es el de asignar una función flecha anónima como manejadora de un evento. Se les llama anónimas porque no cuentan con un nombre o identificador.

```js
etiqueta.addEventListener('event', () => {
    // Código que ejecuta la función
})
```
Puedes optar por utilizar funciones flecha cuando no requieras invocarlas en otras secciones del código.

> Nota: La actualización del estándard [**ES6**](https://www.w3schools.com/js/js_es6.asp) trajo consigo las funciones flecha, lo que permite la anterior sintaxis al escribir código JavaScript.

## Manipulación del DOM
JavaScript permite obtener referencias de etiquetas HTML para su lectura, modificación, creación e inserción en el DOM. Para esto, usualmente utilizarás el objeto 'document', que hace referencia al DOM.

### Crear etiquetas HTML con el método 'createElement'
Este método recibe como parámetro el nombre de la etiqueta HTML a crear. Retorna un objeto HTML que puede ser personalizado con las siguientes propiedades y métodos.

- **setAttribute('nombreAtributo', 'valor')**: Permite asignarle atributos como **id**, **class**, **name**, **disabled**, **style**, **href**, etc.

#### HTML
```html
    <h2>Agregar Elementos</h2>

    <input type="button" name="agregar" value="Agregar Elemento">

    <ul id="lista">
        <li>Elemento 1</li>
    </ul>
```

#### JavaScript
```js
    const lista = document.getElementById('lista');
    const btn = document.querySelector('input[name="agregar"]');
    let contador = 2; // Estado inicial

    // Modificar su contenido al presionar el botón
    btn.addEventListener('click', () => {
        // Crear Elemento
        let listItem = document.createElement('li');

        // Personalizar elemento
        listItem.setAttribute('style', "background-color: limegreen; border-radius: 3px; padding: 3px;");
        listItem.innerText = `Elemento ${contador}`;

        // Insertar elemento al DOM
        lista.appendChild(listItem);

        contador++;
    })
```
Puedes insertar elementos al DOM con mayor control haciendo uso del método [**insertBefore**](https://developer.mozilla.org/en-US/docs/Web/API/Node/insertBefore)





### Métodos de selección de etiquetas

- **document.getElementById('')**: Su parámetro corresponde al atributo **'id'** de la etiqueta HTML. Debe ser único.
- **document.querySelector('')**: El parámetro corresponde al nombre de la etiqueta **div**, una clase **'.clase'**, un ID **'#identificador'**, el tipo de la etiqueta **"input[type='text']"**, etc. Retorna el primer elemento que coincida, o **Null** si no hay coincidencias.
- **document.querySelectorAll('')**: Retorna una lista de nodos que cuentan con el atributo indicado en parámetro. Utilizado para manipular varios elementos a la vez.
- **document.getElementsByClassName('')**: El parámetro corresponde a la clase de los elementos a buscar. Retorna un arreglo de los nodos que cuenten con esa clase de atributo.

### Propiedades de los objetos
En JavaScript, gran parte de las entidades son objetos. Esto quiere decir que cuentan con propiedades y métodos específicas depediendo del tipo de objeto.
Los métodos de selección de etiquetas esencialmente retornan objetos, así que puedes acceder a propiedades del objeto correspondiente a una HTML.

- **(referenciaInputSubmit).disabled**: Retorna **true***/**false** dependiendo del estado del botón. Puedes deshabilitarlo al asignarle el estado **false**.
- **(objeto).length**: Retorna una medida específica según el tipo de objeto. En **arreglos** y **cadenas** representa la cantidad de elementos o caracteres, respectivamente. En **funciones**, indica cuántos parámetros están definidos en su declaración.
- **(referenciaEtiqueta).innerHTML**: Retorna una cadena de caracteres correspondiente al HTML interno a esa etiqueta. Usualmente utilizado para modificar su contenido.

#### HTML
```html
    <!-- Ejemplo de uso: Modificar el contenido de una etiqueta cuando se presione un botón. -->

    <h2>Agregar Elementos</h2>

    <input type="button" name="agregar" value="Agregar Elemento">
    
    <ul id="lista">
        <li>Elemento 1</li>
    </ul>


```
#### JavaScript
```js
    // Obtener referencia a la lista desordenada
    const lista = document.getElementById('lista');
    const btn = document.querySelector('input[name="agregar"]');
    let contador = 2; // Estado inicial

    // Observa su contenido inicial
    console.log(lista.innerHTML, btn);

    // Modificar su contenido al presionar el botón
    btn.addEventListener('click', () => {
        lista.innerHTML += `<li>Elemento ${contador}</li>`;
        contador++;
    })
```

> Nota: Tanto el método **'createElement'** o modificar la propiedad **'innerHTML'** permiten agregar elementos al DOM (o incluso eliminar, en el caso de **innerHTML**). Saber cuál deberías utilizar depende de cuántos elementos deseas insertar al DOM o el control que desees tener sobre los atributos del elemento.

## Programación basada en eventos
Consiste en que la ejecución del código se desencadena por eventos, como acciones del usuario (clics y pulsaciones de teclas) o eventos del navegador como ambios de estado de la página.

### addEventListener
Es un método que permite indicar qué sucederá dependiendo del tipo de evento que se especifique.

#### Sintaxis
```
    objeto.addEventListener('evento', funcion);
```

Crea una etiqueta **input** de tipo **button**. El **'Event Listenner'** es **'click'**, es decir, espera a que suceda ese evento. Mientras que el **'Event Handler'** es la función que se ejecuta cuando sucede ese evento.

#### JavaScript
```js
    let etiqueta = document.createElement('input');
    etiqueta.type = 'button';
    etiqueta.value = 'Send';

    etiqueta.addEventListener('click', () => {
        alert('Hello');
    });

    document.body.appendChild(etiqueta)
```
---

### 📌 Información adicional para autoestudio.
Recuerda consultar la [documentación de desarrolladores de Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript) para estudiar cualquier propiedad, método o característica del lenguaje.
