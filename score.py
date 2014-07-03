# -*- coding: utf-8 -*-

"""
Module containing a class that deals with the scoring system
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

class ScoreSystem():
    """
    Class that deals with the scoring and star system
    """
    def __init__(self,  score,  questions=None):
        """ Constructor"""
        self.score = score
        self.questions = questions
        
    def checkAnswers(self, buttonClicks,  answer1, qx, x, answer2 = None,  qy = None,  y = None):
        """
        check answers and add points if correct based on the number of answers already submitted. 
        Remember to update the score after you have called this function.
        
        parameters: number of clicks on the check answers button, correct answer 1, qx, question #, correct answer 2, qy, y
        
        returns: score, qx, qy
        """

        points = self.assignPoints(buttonClicks)
        
        if answer2 is not None and qy is not None and y is not None:
            if  answer1.isChecked() and answer2.isChecked() and qx == False and qy == False:
                self.score += (2*points)
                qx= True
                qy = True
            elif answer1.isChecked() and qx == False:
                self.score += points
                qx = True
            elif answer2.isChecked() and qy == False:
                self.score += points
                qy = True  
            else:
                self.score += 0
            self.ansMsgBoxes(qx,  x,  qy,  y)
            return self.score,  qx,  qy
        else:
            if  answer1.isChecked() and qx == False:
                self.score += points
                qx = True
            else:
                self.score += 0
            self.ansMsgBoxes(qx,  x)
            return self.score,  qx
        
        
    def assignPoints(self,  buttonClicks):
        """
        Assign a different number of points depending on the number of trials. i.e. 5 points for getting it right
        first time, 3 for getting it right second time and 1 point thereafter.
        """
        if buttonClicks == 1:
            points = 5
        elif buttonClicks == 2:
            points = 3
        else:
            points = 1

        return points
        
    def ansMsgBoxes(self,  qx, x, qy=None,  y=None ):
        """
        show message boxes telling the user if they have got the questions right and informing them to move on
        or highlighting to the user which question they got wrong and telling them to try again.
        """
        msgBox=QMessageBox()
        if qy is not None and y is not None:
            if qx == False and qy == False:
                msgBox.setText("That is the wrong answer for question " +str(x) +" and " +str(y) + ". Try again.")
                msgBox.exec_() 
            elif qx == False:
                msgBox.setText("That is the wrong answer for question "+ str(x) + ". Try again.")
                msgBox.exec_() 
            elif qy == False:
                msgBox.setText("That is the wrong answer for question " + str(y)+ ". Try again.")
                msgBox.exec_() 
            else:
                msgBox.setText("Well done. Click Next to move on.")
                msgBox.exec_() 
        else:
            if qx == False:
                msgBox.setText("That is the wrong answer for question "+ str(x)+". Try again.")
                msgBox.exec_() 
            else:
                msgBox.setText("Well done. Click Next to move on.")
                msgBox.exec_()  
               
    def updateScore(self,  ScoreLabelList,  starView=None):
        """
        update the score at the bottom of the window
        """
        for label in ScoreLabelList:
            label.clear()
            label.setText(str(self.score))
        if starView is not None:
            self.drawStars(starView)
        
    def drawStars(self,  graphicsView):
        """
        Draw stars based on the number of points the user has accumulated
        """
        scene = QGraphicsScene()
        
        graphicsView.setScene(scene)
 
        coords = [QPointF(10, 40),  QPointF(40, 40),  QPointF(50, 10),  QPointF(60, 40),  QPointF(90, 40),  QPointF(65,  60),  QPointF(75,  90),  QPointF(50, 70),  QPointF(25, 90),  QPointF(35,  60)]

        starPoly = QPolygonF()
        
        starPoly2 = QPolygonF()
        
        starPoly3 = QPolygonF()

        for coord in coords:
            starPoly << coord
            starPoly2 << coord
            starPoly3 << coord

            
        yellowBrush = QBrush(QColor(255, 217,  10,  255))
        yellowPen = QPen(QColor(255,  217,  10,  255))
        greyBrush = QBrush(QColor(207, 207, 207,  255))
        greyPen = QPen(QColor(207, 207, 207, 255))

        starPoly2.translate(50, 55)
        starPoly3.translate(100, 0)

        polygon = QGraphicsPolygonItem()
        
        if self.questions == 6:
            a=25
            b=15
            c = 6
        else:
            a=30
            b=20
            c=7
        
        if self.score > a:
            scene.addPolygon(starPoly,  yellowPen,  yellowBrush)
            scene.addPolygon(starPoly2, yellowPen,  yellowBrush)
            scene.addPolygon(starPoly3,  yellowPen,  yellowBrush)
        elif self.score <= a and self.score> b:
            scene.addPolygon(starPoly,  greyPen,  greyBrush)
            scene.addPolygon(starPoly2, yellowPen,  yellowBrush)
            scene.addPolygon(starPoly3,  yellowPen,  yellowBrush)
        elif self.score <= b and self.score > c :
            scene.addPolygon(starPoly,  greyPen,  greyBrush)
            scene.addPolygon(starPoly2, greyPen,  greyBrush)
            scene.addPolygon(starPoly3,  yellowPen,  yellowBrush)  
        else:
            scene.addPolygon(starPoly,  greyPen,  greyBrush)
            scene.addPolygon(starPoly2, greyPen,  greyBrush)
            scene.addPolygon(starPoly3,  greyPen,  greyBrush)
            
        
    
