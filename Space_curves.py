import numpy as np
import matplotlib.pyplot as plt
import pylab as p
from mpl_toolkits.mplot3d import Axes3D

def sierspinski_curve(leng=1, iteracions=2, speed=3, origin=(0,0)):
    import turtle

    #Definindo as letras
    def S(iter=1):
        if iter == 1:
            t.left(45)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.left(45)
        else:
            G1(iter-1)
    def R(iter=1):
        if iter==1:
            t.left(135)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.right(45)
        else:
            G2(iter-1)
    def Z(iter=1):
        if iter==1:
            t.right(135)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.right(135)
        else:
            G4(iter-1)
    def P(iter):
        if iter==1:
            t.right(45)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.right(45)
            t.forward(leng)
            t.left(135)
        else:
            G3(iter-1)

    # Definindo constantes
    def c():
        #anda para cima
        t.left(90)
        t.forward(leng)
        t.right(90)
    def e():
        #anda para a esquerda
        t.right(180)
        t.forward(leng)
        t.right(180)
    def d():
        # anda para a direita
        t.forward(leng)
    def b():
        #anda para baixo
        t.right(90)
        t.forward(leng)
        t.left(90)
    def Ddc():
        # Diagonal direita para cima
        t.left(45)
        t.forward(leng)
        t.right(45)
    def Ddb():
        # Diagonal direita para baixo
        t.right(45)
        t.forward(leng)
        t.left(45)
    def Dec():
        # Diagonal esquerda para cima
        t.left(135)
        t.forward(leng)
        t.right(135)
    def Deb():
        # Direita esquerda baixo
        t.right(135)
        t.forward(leng)
        t.left(135)

    #gramatica
    def G1(iter ,var="S"):
        # S <-
        S(iter)
        Ddc()
        R(iter)
        d()
        P(iter)
        Ddb()
        S(iter)
    def G2(iter, var="R"):
        # R <-
        R(iter)
        Dec()
        Z(iter)
        c()
        S(iter)
        Ddc()
        R(iter)
    def G3(iter, var="P"):
        P(iter)
        Ddb()
        S(iter)
        b()
        Z(iter)
        Deb()
        P(iter)
    def G4(iter, var="Z"):
        Z(iter)
        Deb()
        P(iter)
        e()
        R(iter)
        Dec()
        Z(iter)


    t = turtle.Turtle()
    t.up()
    t.setpos(origin[0], origin[1])
    t.down()
    t.speed(speed)
    Z(iteracions)
    turtle.exitonclick()

def Hilbert_curve(leng=1, iterac=1,speed=3, origin=(-400,-300)):
    import turtle
    t = turtle.Turtle()
    t.up()
    t.setpos(origin[0], origin[1])
    t.down()
    t.speed(speed)
    #Definindo letras
    def H(iter):
        if iter==1:
            t.left(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.left(90)
        else:
            G1(iter-1)

    def A(iter):
        if iter==1:
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.right(180)
        else:
            G2(iter-1)

    def B(iter):
        if iter ==1:
            t.left(180)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
        else:
            G3(iter-1)

    def C(iter):
        if iter==1:
            t.right(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.right(90)
        else:
            G4(iter-1)

    # Definindo as constantes
    def d():
        t.forward(leng)
    def e():
        t.right(180)
        t.forward(leng)
        t.left(180)
    def c():
        t.left(90)
        t.forward(leng)
        t.right(90)
    def b():
        t.right(90)
        t.forward(leng)
        t.left(90)

    # Gramatica
    def G1(iter, var="H"):
        A(iter)
        c()
        H(iter)
        d()
        H(iter)
        b()
        B(iter)
    def G2(iter, var="A"):
        H(iter)
        d()
        A(iter)
        c()
        A(iter)
        e()
        C(iter)
    def G3(iter, var="B"):
        C(iter)
        e()
        B(iter)
        b()
        B(iter)
        d()
        H(iter)
    def G4(iter, var='C'):
        B(iter)
        b()
        C(iter)
        e()
        C(iter)
        c()
        A(iter)

    A(iterac)
    turtle.exitonclick()

def Peano_curve(leng=1, iterac=1, speed=3,origin=(0,0)):
    import turtle
    t = turtle.Turtle()
    t.speed(speed)
    t.up()
    t.setpos(origin[0], origin[1])
    t.down()
    # Definindo letras
    def P(iter):
       if iter==1:
           t.left(90)
           t.forward(leng)
           t.right(90)
           t.forward(leng)
           t.right(90)
           t.forward(leng)
           t.left(90)
           t.forward(leng)
           t.left(90)
           t.forward(leng)
           t.right(90)
       else:
           G1(iter-1)
    def Q(iter):
        if iter==1:
            t.left(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.right(90)
        else:
            G2(iter-1)
    def R(iter):
        if iter ==1:
            t.right(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.left(90)
        else:
            G3(iter-1)
    def S(iter):
        if iter ==1:
            t.right(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.left(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.right(90)
            t.forward(leng)
            t.left(90)
        else:
            G4(iter-1)
    # Definindo as constantes
    def c():
        t.left(90)
        t.forward(leng)
        t.right(90)
    def b():
        t.right(90)
        t.forward(leng)
        t.left(90)
    def d():
        t.forward(leng)
    def e():
        t.right(180)
        t.forward(leng)
        t.right(180)

    # Gramatica
    def G1(iter, var="P"):
        P(iter)
        c()
        Q(iter)
        c()
        P(iter)
        d()
        S(iter)
        b()
        R(iter)
        b()
        S(iter)
        d()
        P(iter)
        c()
        Q(iter)
        c()
        P(iter)

    def G2(iter, var="Q"):
        Q(iter)
        c()
        P(iter)
        c()
        Q(iter)
        e()
        R(iter)
        b()
        S(iter)
        b()
        R(iter)
        e()
        Q(iter)
        c()
        P(iter)
        c()
        Q(iter)

    def G3(iter, var="Q"):
        R(iter)
        b()
        S(iter)
        b()
        R(iter)
        e()
        Q(iter)
        c()
        P(iter)
        c()
        Q(iter)
        e()
        R(iter)
        b()
        S(iter)
        b()
        R(iter)

    def G4(iter, var="Q"):
        S(iter)
        b()
        R(iter)
        b()
        S(iter)
        d()
        P(iter)
        c()
        Q(iter)
        c()
        P(iter)
        d()
        S(iter)
        b()
        R(iter)
        b()
        S(iter)

    S(iterac)
    turtle.exitonclick()

def Gosper_Flowsnake_curve(leng, iterac=1,  speed=3, origin=(0,0)):
    import turtle
    t = turtle.Turtle()
    t.speed(speed)
    t.up()
    t.setpos(origin[0], origin[1])
    t.down()

    # Definindo letras
    def G(iter):
        if iter == 1:
            t.forward(leng)
            t.left(120)
            t.forward(leng)
            t.left(60)
            t.forward(leng)
            t.right(150)
            t.forward(leng)
            t.right(30)
            t.forward(leng)
            t.right(60)
            t.forward(leng)
        else:
            G1(iter-1)
    def R(iter):
        if iter==1:
            t.forward(leng)
            t.left(60)
            t.forward(leng)
            t.left(60)
            t.forward(leng)
            t.left(120)
            t.forward(leng)
            t.right(60)
            t.forward(leng)
            t.right(120)
            t.forward(leng)
        else:
            G2(iter-1)

    # constantes
    def c():
        # Diagonal esquerda para cima
        t.forward(leng)
    def l():
        t.left(60)
    def r():
        t.right(60)
    # Gramatica
    def G1(iter):
        G(iter)
        l()
        c()
        R(iter)
        l()
        c()
        R(iter)
        c()
        r()
        G(iter)
        c()
        r()
        G(iter)
        l()
        c()
        G(iter)
        c()
        r()
        R(iter)

    def G2(iter):
        G(iter)
        l()
        c()
        R(iter)
        c()
        r()
        R(iter)
        l()
        c()
        R(iter)
        l()
        c()
        G(iter)
        c()
        r()
        G(iter)
        c()
        r()
        R(iter)

    R(iterac)
    turtle.exitonclick()

def dragon(level=4, size=200, direction=45):
    from turtle import right, left, forward, exitonclick
    if not level:
        forward(size)
    else:
        right(direction)
        dragon(level-1, size/1.41421356237, 45)
        left(direction * 2)
        dragon(level-1, size/1.41421356237, -45)
        right(direction)
    exitonclick()

class Hilbert_3d:
    """this class will build the hilbert curve in Blender
    """
    import numpy as np

    def __init__(self, x0, y0, z0, size):
        self.x, self.y, self.z = np.array([x0]), np.array([y0]), np.array([z0])
        self.size = size
        self.len = len(self.x)

    def A(self, iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
        else:
            self.G1(iter-1)
    def B(self, iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
        else:
            self.G2(iter-1)
    def C(self, iter):
        if iter ==1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
        else:
            self.G3(iter-1)
    def D(self, iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
        else:
            self.G4(iter-1)
    def E(self, iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
        else:
            self.G5(iter)
    def F(self, iter):
        if iter==1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
        else:
            self.G6(iter-1)
    def G(self,iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.size + self.x[-1]), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
        else:
            self.G7(iter-1)
    def H(self, iter):
        if iter ==1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
        else:
            self.G8(iter-1)
    def I(self, iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), p.append(self.y, self.y[-1]), np.append(
                self.z, self.z[-1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
        else:
            self.G9(iter-1)
    def J(self, iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
        else:
            self.G10(iter-1)
    def K(self, iter):
        if iter == 1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] + self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y,
                                                                                          self.y[-1]), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] - self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                             self.z[
                                                                                                                 -1] - self.size)
            self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y,
                                                                              self.y[-1] + self.size), np.append(self.z,
                                                                                                                 self.z[
                                                                                                                     -1])
        else:
            self.G11(iter-1)
    def L(self, iter):
       if iter == 1:
           self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1] + self.size), np.append(
               self.z, self.z[-1])
           self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                            self.z[
                                                                                                                -1] - self.size)
           self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1] - self.size), np.append(
               self.z, self.z[-1])
           self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y, self.y[-1]), np.append(
               self.z, self.z[-1])
           self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1] + self.size), np.append(
               self.z, self.z[-1])
           self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(self.z,
                                                                                                            self.z[
                                                                                                                -1] + self.size)
           self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1] - self.size), np.append(
               self.z, self.z[-1])
       else:
           self.G12(iter-1)

    #constantes
    def c(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(
            self.z, self.z[-1] + self.size)

    def b(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(
            self.z, self.z[-1] - self.size)

    def e(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y, self.y[-1]), np.append(
            self.z,
            self.z[-1])

    def d(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y, self.y[-1]), np.append(
            self.z,
            self.z[-1])

    def f(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1] + self.size), np.append(
            self.z,
            self.z[
                -1])

    def back(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1] - self.size), np.append(
            self.z,
            self.z[
                -1])

    # Gramática
    def G1(self, iter):
        self.A(iter)
        self.back()
        self.E(iter)
        self.d()
        self.E(iter)
        self.f()
        self.H(iter)
        self.c()
        self.H(iter)
        self.back()
        self.K(iter)
        self.e()
        self.K(iter)
        self.f()
        self.D(iter)
    def G2(self, iter):
        self.D(iter)
        self.f()
        self.F(iter)
        self.d()
        self.F(iter)
        self.back()
        self.G(iter)
        self.b()
        self.G(iter)
        self.f()
        self.L(iter)
        self.e()
        self.L(iter)
        self.b()
        self.C(iter)
    def G3(self, iter):
        self.E(iter)
        self.d()
        self.A(iter)
        self.c()
        self.A(iter)
        self.e()
        self.I(iter)
        self.back()
        self.I(iter)
        self.d()
        self.B(iter)
        self.b()
        self.B(iter)
        self.e()
        self.L(iter)
    def G4(self, iter):
        self.F(iter)
        self.d()
        self.B(iter)
        self.b()
        self.B(iter)
        self.e()
        self.J(iter)
        self.f()
        self.J(iter)
        self.d()
        self.A(iter)
        self.c()
        self.A(iter)
        self.e()
        self.K(iter)
    def G5(self, iter):
        self.A(iter)
        self.c()
        self.C(iter)
        self.back()
        self.C(iter)
        self.b()
        self.F(iter)
        self.d()
        self.F(iter)
        self.c()
        self.J(iter)
        self.f()
        self.J(iter)
        self.b()
        self.G(iter)
    def G6(self, iter):
        self.B(iter)
        self.b()
        self.D(iter)
        self.f()
        self.D(iter)
        self.f()
        self.E(iter)
        self.d()
        self.E(iter)
        self.b()
        self.I(iter)
        self.back()
        self.I(iter)
        self.c()
        self.H(iter)
    def G7(self, iter):
        self.I(iter)
        self.back()
        self.K(iter)
        self.e()
        self.K(iter)
        self.f()
        self.B(iter)
        self.b()
        self.B(iter)
        self.back()
        self.E(iter)
        self.d()
        self.E(iter)
        self.f()
        self.J(iter)
    def G8(self, iter):
        self.J(iter)
        self.f()
        self.L(iter)
        self.e()
        self.L(iter)
        self.back()
        self.A(iter)
        self.c()
        self.A(iter)
        self.f()
        self.F(iter)
        self.d()
        self.F(iter)
        self.back()
        self.I(iter)
    def G9(self, iter):
        self.K(iter)
        self.e()
        self.G(iter)
        self.b()
        self.G(iter)
        self.d()
        self.C(iter)
        self.back()
        self.C(iter)
        self.e()
        self.H(iter)
        self.c()
        self.H(iter)
        self.d()
        self.F(iter)
    def G10(self, iter):
        self.L(iter)
        self.e()
        self.H(iter)
        self.c()
        self.H(iter)
        self.d()
        self.D(iter)
        self.f()
        self.D(iter)
        self.e()
        self.G(iter)
        self.b()
        self.G(iter)
        self.d()
        self.E(iter)
    def G11(self, iter):
        self.G(iter)
        self.b()
        self.I(iter)
        self.back()
        self.I(iter)
        self.c()
        self.L(iter)
        self.e()
        self.L(iter)
        self.b()
        self.D(iter)
        self.f()
        self.D(iter)
        self.c()
        self.A(iter)
    def G12(self, iter):
        self.H(iter)
        self.c()
        self.J(iter)
        self.f()
        self.b()
        self.K(iter)
        self.e()
        self.K(iter)
        self.c()
        self.C(iter)
        self.back()
        self.C(iter)
        self.b()
        self.B(iter)

    def plot(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.gca(projection="3d")
        ax.plot(self.x, self.y, self.z)
        plt.show()

class Peano_3d:
    """this class will build the hilbert curve in Blender
    """
    import numpy as np

    def __init__(self, x0, y0, z0, size):
        self.x, self.y, self.z = np.array([x0]), np.array([y0]), np.array([z0])
        self.size = size
        self.len = len(self.x)
    # letras
    def P(self, iter):
        if iter ==1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1]+self.size), np.append(self.y, self.y[-1] + self.size), np.append(self.z, self.z[-1]+self.size)
        else:
            self.G1(iter-1)
    def R(self, iter):
        if iter==1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y, self.y[
                -1] - self.size), np.append(self.z, self.z[-1] - self.size)
        else:
            self.G2(iter-1)
    def Q(self, iter):
        if iter ==1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y, self.y[
                -1] - self.size), np.append(self.z, self.z[-1] + self.size)
        else:
            self.G3(iter-1)
    def S(self, iter):
        if iter ==1:
            self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y, self.y[
                -1] + self.size), np.append(self.z, self.z[-1] - self.size)
        else:
            self.G4(iter-1)

    def py(self, iter, var="P"):
        self.P(iter)
        self.back()
        self.R(iter)
        self.back()
        self.P(iter)
    def ry(self, iter, var="R"):
        self.R(iter)
        self.f()
        self.P(iter)
        self.f()
        self.R(iter)
    def qy(self, iter, var="Q"):
        self.Q(iter)
        self.f()
        self.S(iter)
        self.f()
        self.Q(iter)
    def sy(self, iter, var="S"):
        self.S(iter)
        self.back()
        self.Q(iter)
        self.back()
        self.S(iter)

    def pyz(self, iter):
        self.py(iter)
        self.c()
        self.qy(iter)
        self.c()
        self.py(iter)
    def ryz(self, iter):
        self.ry(iter)
        self.b()
        self.qy(iter)
        self.b()
        self.ry(iter)
    def qyz(self, iter):
        self.qy(iter)
        self.c()
        self.ry(iter)
        self.c()
        self.qy(iter)
    def syz(self, iter):
        self.sy(iter)
        self.b()
        self.py(iter)
        self.b()
        self.sy(iter)

    # constants
    def c(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(
            self.z, self.z[-1]+ self.size)
    def b(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]), np.append(
            self.z, self.z[-1]- self.size)
    def e(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1] - self.size), np.append(self.y, self.y[-1]), np.append(
            self.z,
            self.z[-1])
    def d(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1] + self.size), np.append(self.y, self.y[-1]), np.append(
            self.z,
            self.z[-1])
    def f(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]+ self.size), np.append(self.z,
                                                                                                         self.z[
                                                                                                             -1])
    def back(self):
        self.x, self.y, self.z = np.append(self.x, self.x[-1]), np.append(self.y, self.y[-1]- self.size), np.append(self.z,
                                                                                                         self.z[
                                                                                                             -1])

    # Gramatics
    def G1(self, iter):
        self.pyz(iter)
        self.d()
        self.ryz(iter)
        self.d()
        self.pyz(iter)
    def G2(self, iter):
        self.qyz(iter)
        self.e()
        self.syz(iter)
        self.e()
        self.qyz(iter)
    def G3(self, iter):
        self.ryz(iter)
        self.d()
        self.pyz(iter)
        self.d()
        self.ryz(iter)
    def G4(self, iter):
        self.syz(iter)
        self.e()
        self.qyz(iter)
        self.e()
        self.syz(iter)

    def plot(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.gca(projection="3d")
        ax.plot(self.x, self.y, self.z)
        plt.show()


