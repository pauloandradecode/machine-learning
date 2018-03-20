#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:39:22 2018

@author: Paulo Andrade
"""

class LinearRegression:
    def __init__ (self, x, t):
        """
        Constructor de la clase
        
        Parametros:
            
            x -- valores del eje Y 
            t -- valores del eje X
        """
        
        self.x = x # valores de X (valores)
        self.t = t # valores de t (tiempo)
        self.n = len(x) # valor de n
    
    
    def b (self):
        """
        Se obtiene el valor de la pendiente respecto a los
        pares ordenados utilizndo la formula:
        
            b = n∑xt - ∑x∑t / n∑t² - [∑t]²
        """
        
        sumxt = 0.0 # Sumatoria XiTi
        sumx = 0.0 # Sumatoria Xi
        sumt = 0.0 # Sumatoria ti
        sumt2 = 0.0 # Sumatoria ti al cuadrado
        
        # Obtenemos las sumatorias
        for i in range(0, self.n):
            sumxt += self.x[i] * self.t[i]
            sumx += self.x[i]
            sumt += self.t[i]
            sumt2 += pow(self.t[i], 2)
            
        # Obtenemos la pendiente
        b = ((self.n*sumxt) - (sumx*sumt)) / ((self.n*sumt2) - pow(sumt, 2))
        
        return b
    
    
    def a (self):
        """
        Se obtiene la interseccion de la recta utilizando la
        formula:
        
            a = ∑x - b*∑t
        """
        
        sumx = 0.0 # Sumatoria Xi
        sumt = 0.0 # sumatoria ti
        b = self.b() # Pendiente
        
        # Obtenemos las sumatorias
        for i in range(0, self.n):
            sumx += self.x[i]
            sumt += self.t[i]
            
        # Obtenemos la interseccion de la recta
        a = (sumx/self.n) - (b*(sumt/self.n))
        
        return a
    
    
    def prediction (self, t):
        """
        Se obtiene la prediccion del valor dado utilizando la
        formula:
        
            xi = a + bt
        
        parametros:
        
            t -- valor a predecir
        """
        
        a = self.a() # interseccion de la recta
        b = self.b() # pendiente
        
        # predecimos el valor solicitado
        xi = a + (b*t)
        
        return xi