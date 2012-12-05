#include <vtkSmartPointer.h>
#include <vtkProperty.h>
#include <vtkDataSetMapper.h>
#include <vtkImageActor.h>
#include <vtkImageReader.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkRenderer.h>
#include <vtkShrinkFilter.h>
#include <vtkLookupTable.h>
#include <vtkImageDataGeometryFilter.h>
#include <vtkPolyDataMapper.h>

 
int main(int argc, char* argv[])
{
  // Verify input arguments
  if(argc != 2)
    {
    std::cout << "Usage: " << argv[0]
              << " Filename.vti" << std::endl;
    return EXIT_FAILURE;
    }
 
  std::string inputFilename = argv[1];
 
  // Read the file
  vtkSmartPointer<vtkImageReader> reader =
    vtkSmartPointer<vtkImageReader>::New();
  reader->SetFileName(inputFilename.c_str());
  reader->Update();
  
  //lookup table for colors
  vtkSmartPointer<vtkLookupTable> lut = 
    vtkSmartPointer<vtkLookupTable>::New();
  lut->SetTableRange(0.0, 16.0);
  lut->Build();


    // Convert the image to a polydata
//  vtkSmartPointer<vtkImageDataGeometryFilter> imageDataGeometryFilter =
//    vtkSmartPointer<vtkImageDataGeometryFilter>::New();
//  imageDataGeometryFilter->SetInputConnection(reader->GetOutputPort());
//  imageDataGeometryFilter->Update();


  // Visualize
  vtkSmartPointer<vtkDataSetMapper> mapper =
    vtkSmartPointer<vtkDataSetMapper>::New();
  mapper->SetInputConnection(reader->GetOutputPort());
//  mapper->SetInputConnection(imageDataGeometryFilter->GetOutputPort());
//  mapper->SetScalarRange(0, 16);
//  mapper->SetLookupTable(lut);

  vtkSmartPointer<vtkActor> actor =
    vtkSmartPointer<vtkActor>::New();
  actor->SetMapper(mapper);
  actor->GetProperty()->SetPointSize(10);
 
  vtkSmartPointer<vtkRenderer> renderer =
    vtkSmartPointer<vtkRenderer>::New();
  renderer->AddActor(actor);
  renderer->ResetCamera();
  renderer->SetBackground(.2,.3,.4);
 
  vtkSmartPointer<vtkRenderWindow> renderWindow =
    vtkSmartPointer<vtkRenderWindow>::New();
  renderWindow->AddRenderer(renderer);
 
  vtkSmartPointer<vtkRenderWindowInteractor> renderWindowInteractor =
    vtkSmartPointer<vtkRenderWindowInteractor>::New();
  renderWindowInteractor->SetRenderWindow(renderWindow);
  renderWindowInteractor->Initialize();
 
  renderWindowInteractor->Start();
 
  return EXIT_SUCCESS;
}
