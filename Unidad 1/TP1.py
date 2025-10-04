#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo");

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("¿Cómo te llamás? ");
print(f"Hola {nombre}");

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ");
apellido = input("Ingrese su apellido: ");
edad = int(input("Edad: "));
residencia = input("Lugar de residencia: ");

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}");


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.


radio = float(input("Radio de un círculo: "));
pi = float(3.1416);

area = float(pi* (radio**2));

print(f"El área de un círculo es: {area}");

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos: "));

seg = 3600
horas = segundos/seg

print("Los segundos ingresados, ", segundos,", equivalen a ", horas," horas");

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.

num = int(input("Ingrese un numero: "));

print("La tabla de multiplicar del numero ", num," es: 0 * ",num," = ", 0*num);
print("La tabla de multiplicar del numero ", num," es: 1 * ",num," = ", 1*num);
print("La tabla de multiplicar del numero ", num," es: 2 * ",num," = ", 2*num);
print("La tabla de multiplicar del numero ", num," es: 3 * ",num," = ", 3*num);
print("La tabla de multiplicar del numero ", num," es: 4 * ",num," = ", 4*num);
print("La tabla de multiplicar del numero ", num," es: 5 * ",num," = ", 5*num);
print("La tabla de multiplicar del numero ", num," es: 6 * ",num," = ", 6*num);
print("La tabla de multiplicar del numero ", num," es: 7 * ",num," = ", 7*num);
print("La tabla de multiplicar del numero ", num," es: 8 * ",num," = ", 8*num);
print("La tabla de multiplicar del numero ", num," es: 9 * ",num," = ", 9*num);
print("La tabla de multiplicar del numero ", num," es: 10 * ",num," = ", 10*num);


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

n1 = int(input("Ingrese un numero entero: "));
n2 = int(input("Ingrese otro numero entero: "));

suma = n1+n2
resta = n1-n2
producto = n1*n2
division = n1/n2

print("La suma de ", n1," y ", n2," es: ", suma);
print("La resta de ", n1," y ", n2," es: ", resta);
print("La multiplicacion de ", n1," y ", n2," es: ", producto);
print("La division de ", n1," y ", n2," es: ", division);

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su 
# índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del 
# siguiente modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura = float(input("Ingrese su altura: "));
peso = float(input("Ingrese su peso: "));

IMC = peso/(altura**2);

print("Su indice de masa corporal es: ", IMC," kg/m2");

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingrese la Temperatura en grados Celsius: "));

Fahrenheit = (celsius * 9/5)+32;

print("La temperatura en grados Fahrenheit es: ", Fahrenheit);

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de 
#dichos números.

n1 = float(input("Ingrese un numero: "));
n2 = float(input("Ingrese otro numero: "));
n3 = float(input("Ingrese otro numero: "));

promedio = (n1+n2+n3)/3;

print("El promedio es: ", promedio);
