# Trabajo sobre matriz de confusión
## 1.Introducción 
<p>En este trabajo vamos a analizar un dataset con 2 modelos diferentes para analizar su matriz de confusión, para ello primero vamos a justificar la toma de decisiones que tenemos que tomar a lo largo del trabajo <p>

<ul>
  <li>Dataset elegido: en un momento quise trabajo con los fraudes bancarios pero miré los datos y no me gustaron porque era todo V1,V2,etc... y no eran muy claro, en cambio del dataset del cancer ya tengo experiencia, recuerdo que la página de documentación era bastante clara y además eso ayuda mucho porque tenemos metodos que nos dan la descripción del propio dataset.</li>
  <li>Como tema elegido he tratado el segundo tema, ya que en ejemplos anteriores hemos tratado el desbalance de datos y supe como encararlo bien, y para mi gusto, es de las más interesantes de encarar con este tipo de dataset ya que estamos tratando datos médicos diferentes.</li>
</ul>

<p>Después del problema presentado debido a que el anterior dataset no cumplía el requisito de las filas, cambio la toma de decisiones.</p>
<ul> 
  <li>El nuevo dataset elegido es el de los vinos, aunque el contenido no me agrada tanto, creo que es muy interesante para tratar de hacer el problema que voy a presentar y analizarlo de la mejor forma posible, además de que las variables son bastante entendibles y la columna objetivo se me hace bastante clara y puede ayudar y la limpieza de los datos no tiene pinta de ser muy exhaustiva a priori.</li>
  <li>El problema que voy a tratar es el tercero de análisis de la matriz de confusión en clasificación multiclase, ya que este dataset presenta salidas clave con las notas de calidad y para mi opinión creo que tendrá una cierta enjundia por encima de los otros.</li>
</ul>

## 2.Descripción del dataset

<h3>Descripción inicial </h3>
<p>Son 2 datasets que contienen varios datos relacionados a variantes de vinos Portugueses, uno rojo y otro blanco. <p>
<p>En base a la documentación sabemos que las clases están ordenadas pero no balanceadas, el promedio mas alto está en los vinos de nota normal no en los muy buenos o en los mediocres.</p>
<p>No se sabe si todas las variables son relevantes, cosa que iremos viendo y documentado en la preparación y analisis del dataset, por lo que ahora procederemos a realizar la descripción mas en profundidas </p>

<h3> Descripción técnica </h3>
<p>Primero de todo, vamos a proceder a hacer un muy breve analisis de las variables </p>
<ul> 
  <li>fixed acidity: variable tipo float sin nulos </li>
  <li>volatile acidity: variable tipo float sin nulos </li>
  <li>citric acid: variable tipo float sin nulos </li>
  <li>residual sugar: variable tipo float sin nulos </li>
  <li>chlorides: variable tipo float sin nulos </li>
  <li>free sulfur dioxide: variable tipo float sin nulos </li>
  <li>total sulfur dioxide: variable tipo float sin nulos </li>
  <li>density: variable tipo float sin nulos </li>
  <li>pH: variable tipo float sin nulos </li>
  <li>sulphates: variable tipo float sin nulos </li>
  <li>alcohol: variable tipo float sin nulos </li>
  <li>quality: variable tipo entero y objetivo que expresa la calidad del vino con valores del 3 al 9 sin nulos </li>
</ul>

<p>En estas imágenes podemos ver la dimensión del dataset dividido, después de realizar la mezcla, que consta de 6495 filas y 12 columnas.</p>
<image src="Capturas/Captura1.png" alt="Descripción de filas y columnas del dataset dividido">
<image src="Capturas/Captura2.png" alt="Descripción de filas y columnas del dataset conjunto">

<p>En esta imagen podemos ver la información del dataset, como se puede observar no hay nulos, todas las variables son numéricas y la variable objetivo es de tipo entero, lo que nos va a facilitar el trabajo a la hora de realizar la clasificación, además de que no hay variables categóricas que nos puedan complicar el trabajo a la hora de realizar la preparación de los datos.</p>
<image src="Capturas/Captura3.png" alt="Información del dataset">


<p>En la imagen podemos ver uno de los datos curiosos que se comentaba y había visto en la documentación del dataset que comentaba que las clases estaban desbalanceadas, un dato que nos puede resultar muy interesante a la hora de realizar el análisis de la matriz de confusión.</p>
<image src="Capturas/Captura4.png" alt="Valores de calidad">


<p>En esta imagen podemos ver la correlación de las variables con la variable objetivo, como se comentaba en la documentacion del dataset, hay variables con muy poco impacto pero igulamente en un principio no voy a eliminar ninguna, es mas que nada por saber que quizás el modelo no da los mejores resultados.</p>
<image src="Capturas/Captura5.png" alt="Correlación de las variables con la variable objetivo">


<p>En esta imagen podemos ver la descripción estadística del dataset, como se puede observar hay algunas variables que tienen una gran diferencia entre el valor mínimo y el máximo, lo que nos puede indicar que hay algunos valores atípicos.</p>
<image src="Capturas/Captura6.png" alt="Descripción estadística del dataset">


## 3.Preparación de los datos

<p>Con toda la descripción anteriormente realizada, podemos ver que los datos de este dataset están muy limpios y la variable objetivo es bastante clara, por lo menos a mi parecer, por lo que lo único que tendriamos que hacer es definir la X y la Y <p>
<image src="Capturas/Captura7.png" alt="Preparación de los datos">

<p>Con esto realizado solo quedaría escalar los datos ya que es algo importante para los modelos de clasificación que utilizaremos</p>
<image src="Capturas/Captura8.png" alt="Escalado de los datos">

## 4.Modelos de clasificación

<p>En este apartado vamos a justificar la elección de los modelos de clasificación que vamos a utilizar. Dado que estamos trabajando con un problema de clasificación multiclase, es importante seleccionar modelos que sean capaces de manejar este tipo de problemas de manera efectiva. </p>

<p> El primer modelo que vamos a utilizar es el ramdon forest por los siguientes características</p>

<ul>
  <li>Es robusto ante los posibles outliers que comentamos anteriormente</li>
  <li>Tiene buen manejo de las relaciones no lineales </li>
  <li>Al tener un dataset pequeño no va a consumir tanta potencia</li>
</ul>

<image src="Capturas/Captura9.png" alt="Ramdon Forest Classifier">

<p> El segundo modelo a utilizar va a ser el SVM (Support Vector Machine) por las siguientes características<p>

<ul>
  <li>Es bastante bueno para todo tipo de casos, por lo que al ser un caso que se puede complicar por el desbalanceo, prefiero tirar a algo medianamente seguro</li>
  <li>Suele tener muy buena efectividad con el kernel RBF </li>
</ul>

<image src="Capturas/Captura10.png" alt="SVM">

## 5.Matriz de confusión y métricas

<h3> Random Forest </h3>

<p>El modelo de Random Forest obtiene un accuracy de 0.6882, aunque como veremos, esta métrica sola no cuenta todo</p>

<image src="Capturas/Captura11.png" alt="Ramdon forest metricas">

<h4>Análisis de falsos positivos y negativos (RF):</h4>

<p>La confusión se concentra entre clases adyacentes, lo que tiene sentido 
al tratarse de una escala ordinal de calidad:<p>

<ul>
<li> Clases 5 y 6: son las más confundidas entre sí. El modelo genera 
  111 FP de clase 5 predichos como 6, y 95 FP de clase 6 predichos como 5. 
  Es el error más frecuente y el que más penaliza el rendimiento global. </li>
<li>Clase 3: 0 predicciones correctas. Con solo 4 instancias en test, 
  el modelo no tiene suficiente información para aprenderla. Todos se 
  clasifican como 5 o 6, generando 4 falsos negativos de clase 3. </li>
<li>Clase 8: precision muy alta (0.93) pero recall bajo (0.37). El 
  modelo es muy conservador: solo predice calidad 8 cuando está muy 
  seguro, dejando 22 falsos negativos. 13 de ellos los confunde con 
  calidad 7.</li>
<li>Clase 4: recall del 11%, lo que significa que 33 de 37 vinos de 
  calidad 4 no son reconocidos como tal.</li>
</ul>

<h3> SVM </h3>

<p>El modelo SVM obtiene un accuracy de 0.5881, notablemente inferior 
al Random Forest. </p>

<h4>Análisis de falsos positivos y negativos (SVM):</h4>

<ul>
<li>El SVM agrava los errores entre clases adyacentes respecto al RF. 
  La confusión entre clases 5 y 6 es aún mayor: 139 casos de clase 6 
  se clasifican como 5 y 128 de clase 5 como 6.</li>
<li>Clase 7: el modelo arrastra muchos falsos negativos hacia clase 6 
  (142 instancias). Casi la mitad de los vinos de calidad 7 se 
  clasifican como 6.</li>
<li>Clase 8: prácticamente ignorada. Solo 1 de 35 vinos de calidad 8 
  se clasifica correctamente (recall 0.03). Esto es el peor resultado 
  individual del trabajo.</li>
<li>La diferencia entre macro avg (0.31) y weighted avg (0.57) es enorme, 
  lo que refleja que el modelo aprende bien las clases mayoritarias pero 
  fracasa sistemáticamente en las minoritarias.</li>
</ul>

## 6.Evaluación y comparación de métricas

## 7.Conclusiones

## 8.Lineas de mejora y trabajo futuro

## 9. Bibliografia

[Documentación dataset del cancer de Wisconsin](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)

[Documentacion dataset de vinos](https://archive.ics.uci.edu/dataset/186/wine+quality)

[Estudio del dataset en Kaggle](https://www.kaggle.com/code/yasserh/wine-quality-prediction-comparing-top-ml-models)

[Como interpretar una matriz de confusion](https://telefonicatech.com/blog/como-interpretar-la-matriz-de-confusion-ejemplo-practico)

## 10. Anexo A - Uso de herramientas de IA

<p>IA utilizada: Git hub copilot con motos de Claude Haiku 4.5 <p>
<p>Prompt realizado: Que modelos de clasificación podrían ser los más optimos para entrenar con estos datasets y explicame por que </p>
<p>Razón: tenia la idea justamente de usar los 2 que he utilizado, pero quería tener una base más sólida para defender el buen uso de estos modelos </p>