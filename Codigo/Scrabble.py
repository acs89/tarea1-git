#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------ #
# Scrabble.py                                                        #
# Programa que determina cuales letras no aperecen repetidas de      #
# forma consecutiva en las palabras leidas de un archivo de texto.   #
# Autor: Andrea Salcedo                                              #
# Fecha de ultima modificacion: 11/11/13                             #
# ------------------------------------------------------------------ #

import sys
import string

""" Funcion que lee las palabras de una lista y verifica si alguna
letra aperece repetida de forma consecutiva. """
def buscarDuplicadas(palabras):
   
      listaLetras = map(chr, range(65,91))
      noDuplicadas = []
             
      for letra in listaLetras:
         
         dobleLetra = letra+letra;
         esDuplicada = False;
         
         for palabra in palabras:
                   
         # Si la palabra actual contiene la letra duplicada, entonces se 
         # sale del ciclo y sigue a la proxima letra.
            if (dobleLetra in palabra):
               esDuplicada = True
               break
            
         # Si la letra actual no fue repetida despues de buscar en todas las 
         # palabras, entonces se agrega a la lista de letras no duplicadas.         
         if not (esDuplicada):
            noDuplicadas.append(letra)
               
      return noDuplicadas   

def main():
   
   try:
      archivo = open(sys.argv[1])
      palabras = archivo.readlines()
      noDuplicadas = buscarDuplicadas(palabras)
      print noDuplicadas 
      archivo.close()
               
   except IOError, ex:
      print "IOError", ex
   except IndexError:
      print "No hay suficiente argumentos: ./Scrabble.py archivo.txt "
      
main()
