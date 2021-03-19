"""El Estudio Jurídico "Hecha la ley, hecha la trampa" se encarga de comprar distintos
tipos de yerba para distribuir a sus oficinas como beneficio para todos sus empleados. 
Para planificar las compras de febrero se van a procesar los consumos de enero.

Se cuentan con el archivo CONSUMOS.CSV, totalmente desordenado, que tiene la siguiente información:

Nro de oficina (número 1 hasta 23), día de apertura del paquete (string "DD"), marca de yerba
(string)
23,01,Amanda
02,02, Verdeflor
15,02,CBSé

Por otro lado, el archivo stock.py contiene una lista con el stock inicial del mes para cada
oficina en cada posición:
stock_yerba = [
{"Amanda": 50, "Rosamonte": 15, "Verdeflor": 5}, # oficina 1
{}, # oficina 2 sin stock de ninguna yerba!
{"Rosamonte": 25, "La Tranquera": 8}, # oficina 3
#...
]

Se requiere importar el archivo stock.py y procesar el archivo de consumos, leyéndolo una
Única vez, para:

1. Actualizar los stocks de paquetes de yerba en cada oficina. Imprimir el resultado final
por pantalla.

Para ello deben tomar el valor del stock inicial para cada oficina y restarle los
consumos que se encuentren en el archivo de CONSUMOS. Cada línea en el archivo
de CONSUMOS, equivale al consumo de 1 paquete de la marca de yerba que figura en
la línea, en la oficina informada.

2. Guardar en el archivo ERRORES.TXT si hay algún consumo inválido X (esto es, se
registró un consumo cuando el stock era cero) con un mensaje que diga “Consumo
inválido en la oficina Nro. {oficina} de yerba marca {marca} el día {dia}".

3. Guardar en otro archivo COMPRAS.CSV el total de paquetes a comprar para cada
marca de yerba basado en los consumos de todas las oficinas procesados, donde cada
línea contenga:

Marca de yerba (string), cantidad a comprar {número}"""