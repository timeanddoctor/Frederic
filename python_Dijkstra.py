#!/usr/bin/env python

import vtk

##################
#Since Python
##################
filename = "Model_3_skin.stl"

#read .STL
reader = vtk.vtkSTLReader()
reader.SetFileName(filename)

mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(reader.GetOutput())
else:
    mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

#creat geodesic path: vtkDijkstraGraphGeodesicPath
dijkstra = vtk.vtkDijkstraGraphGeodesicPath()
dijkstra.SetInputConnection(reader.GetOutputPort())
dijkstra.SetStartVertex(20) #start
dijkstra.SetEndVertex(500000) #end
dijkstra.Update() 

pathMapper = vtk.vtkPolyDataMapper()
pathMapper.SetInputConnection(dijkstra.GetOutputPort())

pathActor = vtk.vtkActor()
pathActor.SetMapper(pathMapper);
pathActor.GetProperty().SetColor(1,0,0)# Red
pathActor.GetProperty().SetLineWidth(4);

# Create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

## Assign actor to the renderer
ren.AddActor(actor)
ren.AddActor(actor1)
#ren.RemoveActor(actor1);
ren.AddActor(pathActor)
ren.SetBackground(1,1,1)
renWin.SetSize(200, 200)

# This allows the interactor to initalize itself. It has to be
# called before an event loop.
iren.Initialize()

# We'll zoom in a little by accessing the camera and invoking a "Zoom"
# method on it.
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

# Start the event loop.
iren.Start()

#get the distance of the geodesic path (In progress)
weights = vtk.vtkDoubleArray()
dijkstra.GetCumulativeWeights(weights) 