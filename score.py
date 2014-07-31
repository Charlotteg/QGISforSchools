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
        #get points
        points = self.assignPoints(buttonClicks)
        
        #if 2 questions linked to 1 check answers button then...
        if answer2 is not None and qy is not None and y is not None:
            #if both answers are correct (and have not been correct before), add relevant points
            if  answer1.isChecked() and answer2.isChecked() and qx == False and qy == False:
                self.score += (2*points)
                qx= True
                qy = True
            # otherwise if only answer 1 is correct, add points 
            elif answer1.isChecked() and qx == False:
                self.score += points
                qx = True
            #or if only answer 2 is correct, add points
            elif answer2.isChecked() and qy == False:
                self.score += points
                qy = True 
            #or add zero points if wrong
            else:
                self.score += 0
                
            #send up message boxes to notify the user if they are right or wrong
            self.ansMsgBoxes(qx,  x,  qy,  y)
            
            #return the new score and new qx,qy states
            return self.score,  qx,  qy
        #if only one question is linked to the checkanswers button...
        else:
            #if correct add points
            if  answer1.isChecked() and qx == False:
                self.score += points
                qx = True
            #if incorrect, add nothing
            else:
                self.score += 0
            #send up message boxes to notify the user if they are right or wrong
            self.ansMsgBoxes(qx,  x)
            
            #return the new score and new qx state
            return self.score,  qx
        
        
    def assignPoints(self,  buttonClicks):
        """
        Assign a different number of points depending on the number of trials. i.e. 5 points for getting it right
        first time, 3 for getting it right second time and 1 point thereafter.
        """
        #if the button has only been clicked once, assign 5 points for a correct answer
        if buttonClicks == 1:
            points = 5
        #if it has been clicked twice, assign 3 points
        elif buttonClicks == 2:
            points = 3
        #otherwise assign 1 point for any attempts thereafter
        else:
            points = 1

        return points
        
    def ansMsgBoxes(self,  qx, x, qy=None,  y=None ):
        """
        show message boxes telling the user if they have got the questions right and informing them to move on
        or highlighting to the user which question they got wrong and telling them to try again.
        """
        #set up messagebox
        msgBox=QMessageBox()
        
        #if 2 questions linked to checkanswer button...
        if qy is not None and y is not None:
            #if both wrong show message box informing the user
            if qx == False and qy == False:
                msgBox.setText("That is the wrong answer for question " +str(x) +" and " +str(y) + ". Try again.")
                msgBox.exec_() 
            #if only the first question is wrong, tell user which one was incorrect.
            elif qx == False:
                msgBox.setText("That is the wrong answer for question "+ str(x) + ". Try again.")
                msgBox.exec_() 
            #if only the first question is wrong, tell user which one was incorrect.
            elif qy == False:
                msgBox.setText("That is the wrong answer for question " + str(y)+ ". Try again.")
                msgBox.exec_() 
            #if both right, let user know
            else:
                msgBox.setText("Well done. Click Next to move on.")
                msgBox.exec_() 
    
        #if only one question linked to checkanswers button
        else:
            #notify user if wrong
            if qx == False:
                msgBox.setText("That is the wrong answer for question "+ str(x)+". Try again.")
                msgBox.exec_() 
            #notify user if right
            else:
                msgBox.setText("Well done. Click Next to move on.")
                msgBox.exec_()  
               
    def updateScore(self,  ScoreLabelList,  starView=None):
        """
        update the score at the bottom of the window
        """
        #iterate through all the score boxes and update text to correct score
        for label in ScoreLabelList:
            label.clear()
            label.setText(str(self.score))
        #Draw correct number of stars based on score
        if starView is not None:
            self.drawStars(starView)
        
    def drawStars(self,  graphicsView):
        """
        Draw stars based on the number of points the user has accumulated
        """
        #set up scene
        scene = QGraphicsScene()
        #add scene to graphicsview
        graphicsView.setScene(scene)
        
        #set up star point coords
        coords = [QPointF(10, 40),  QPointF(40, 40),  QPointF(50, 10),  QPointF(60, 40),  QPointF(90, 40),  QPointF(65,  60),  QPointF(75,  90),  QPointF(50, 70),  QPointF(25, 90),  QPointF(35,  60)]
        
        #set up stars as floating point polygons
        starPoly = QPolygonF()
        
        starPoly2 = QPolygonF()
        
        starPoly3 = QPolygonF()
        
        #load corrds into each polygon
        for coord in coords:
            starPoly << coord
            starPoly2 << coord
            starPoly3 << coord

        #set up brushes, yellow and grey
        yellowBrush = QBrush(QColor(255, 217,  10,  255))
        yellowPen = QPen(QColor(255,  217,  10,  255))
        greyBrush = QBrush(QColor(207, 207, 207,  255))
        greyPen = QPen(QColor(207, 207, 207, 255))
        
        #move 2 stars so that they are not on top of eachother
        starPoly2.translate(50, 55)
        starPoly3.translate(100, 0)

        polygon = QGraphicsPolygonItem()
        
        #set up star boundaries based on the number of questions in the unit
        if self.questions == 6:
            a=25
            b=15
            c = 6
        else:
            a=30
            b=20
            c=7
        
        #if score is over boundary a, draw 3 yellow stars
        if self.score > a:
            scene.addPolygon(starPoly,  yellowPen,  yellowBrush)
            scene.addPolygon(starPoly2, yellowPen,  yellowBrush)
            scene.addPolygon(starPoly3,  yellowPen,  yellowBrush)
        #if between a and b draw 2 yellow stars and one grey one
        elif self.score <= a and self.score> b:
            scene.addPolygon(starPoly,  greyPen,  greyBrush)
            scene.addPolygon(starPoly2, yellowPen,  yellowBrush)
            scene.addPolygon(starPoly3,  yellowPen,  yellowBrush)
        #if between b and c draw 1 yellow star and 2 grey ones
        elif self.score <= b and self.score > c :
            scene.addPolygon(starPoly,  greyPen,  greyBrush)
            scene.addPolygon(starPoly2, greyPen,  greyBrush)
            scene.addPolygon(starPoly3,  yellowPen,  yellowBrush)  
        #If below c draw 3 grey stars
        else:
            scene.addPolygon(starPoly,  greyPen,  greyBrush)
            scene.addPolygon(starPoly2, greyPen,  greyBrush)
            scene.addPolygon(starPoly3,  greyPen,  greyBrush)
            
        
    
