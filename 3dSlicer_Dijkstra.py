#!/usr/bin/env python

import vtk

##################
#Since Python Interactor (3dslicer)
##################

#load the mesh model made by Segment Editor tool
filename='Model.stl'
modelNode = slicer.util.loadModel("/netapp/vol1_homeunix/briend/Model.stl", returnNode=True)[1]

##centrer image
layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()

##add texte
view=slicer.app.layoutManager().threeDWidget(0).threeDView()
view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperLeft,filename) # Set text to "filename"
view.cornerAnnotation().GetTextProperty().SetColor(1,0,0) # Set color to red
view.forceRender() # Update the view

##Adding fiducials via mouse clicks
placeModePersistence = 1
slicer.modules.markups.logic().StartPlaceMode(placeModePersistence)

##Access to Fiducial Properties (to determinate the start and the end point of the geodesic path)
fidList = slicer.util.getNode('F')
numFids = fidList.GetNumberOfFiducials()
for i in range(numFids):
  ras = [0,0,0]
  fidList.GetNthFiducialPosition(i,ras)
  print i,": RAS =",ras
  
#get index of a point closest to a spatial position (In progress)
somePolyData = someModelNode.GetPolyData()
pointLocator = vtk.vtkPointLocator()
pointLocator.SetDataSet(somePolyData)
pointLocator.BuildLocator()
closestPointId = curvePointsLocator.FindClosestPoint(point)

#add geodesic path to the mapper (In progress)
dijkstra = vtk.vtkDijkstraGraphGeodesicPath()
dijkstra.SetInputConnection(SomePolyData.GetOutputPort())

#add this coordinate in the geodesic path (In progress)
dijkstra.SetStartVertex(20) #start
dijkstra.SetEndVertex(500000) #end
dijkstra.Update()

#get the distance of the geodesic path (In progress)
weights = vtk.vtkDoubleArray()
dijkstra.GetCumulativeWeights(weights) 