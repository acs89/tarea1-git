#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------ #
# Scrabble.py                                                        #
# Programa que determina cuales letras nunca aperecen repetidas de   #
# forma consecutiva en las palabras leidas de un archivo de texto.   #
# Autor: Andrea Salcedo                                              #
# Fecha de ultima modificacion: 11/11/13                             #
# ------------------------------------------------------------------ #

import sys
import string

""" Funcion que lee las palabras de un archivo y verifica si alguna
letra aperece repitida de forma consecutiva. """
def buscarDuplicadas(archivo):
   
      listaLetras = map(chr, range(65,91))
      noDuplicadas = []
             
      for letra in listaLetras:
         
         dobleLetra = letra+letra;
         esDuplicada = False;
         
         for palabra in archivo:
         
         """ Si la palabra contiene la letra duplicada, entonces se sale 
         del ciclo y busca la proxima letra en la palabra actual. """
            if (palabra.find(dobleLetra) >= 0):
               esDuplicada = True
               break
            
         """ Si despues de buscar en todas las palabras la letra no fue
         repetida, entonces se agrega a la lista de letras no duplicadas. """
         if not (esDuplicada):
            noDuplicadas.append(letra)
               
      return noDuplicadas   

def main():
   
   try:
      archivo = open(sys.argv[1])
      noDuplicadas = buscarDuplicadas(archivo)
      print noDuplicadas 
      archivo.close()
               
   except IOError, ex:
      print "IOError", ex
   except IndexError:
      print "No hay suficiente argumentos: ./Scrabble archivo.txt "
      
main()