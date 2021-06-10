### CHALLENGE

Se tomaron varias decisiones en base a los requerimientos del documento.

* Para la funcionalidad de transformacion se decidio que cada unidad lleve una cuenta de cuantas monedas lleva gastadas(_spent_training_price), para asi 
  saber cuando habria transformar, en base al costo de transformacion definido en el documento.      
    
* Cada unidad se puede transformar y eso le da puntos de fuerza, sin embargo, para que se apliquen las transformaciones, los entrenamientos debern 
  ejecutarse a nivel ejercito(Army).  
    
* Para la caja de monedas del ejercito(_army_cash_register), se utilizo una lista ya que no se vio la necesidad de crear un objeto nuevo. Esto fue necesario para poder modificar la caja por referencia.  
   
* Se modelo los ataques en forma ofensiva, es decir, un ejercito recibe un ataque de otro ejercito(recieve_attack).   
   
* Para las batallas empatadas, se decidio que ambos ejercitos pierden la unidad con menos puntos.   
  Esto significa que:
      si el ejercito A tiene dos piqueros y 2 arqueros -> queda con 1 piquero y 2 arqueros
      si el ejercito B tiene 0 piqueros y 2 arqueros -> queda con 0 piqueros y 1 arquero.

  Esta misma logica se utiliza cuando el ejercito perdedor pierde las dos unidades con mas puntaje.
  
* Se implementaron test para los casos basicos e indispensables, podrian cubrirse mas casos.  
    
