# Galaxy 10 DECALS Image Classification Project 


![outerspace-adobestock-1024x720](https://user-images.githubusercontent.com/104231685/168537080-430b3bb0-ed34-41c7-a9be-3dc3615023b3.jpeg)

# About/Background of Dataset

Galaxy10 DECals is a dataset contains 17736 256x256 pixels colored galaxy images that are seperated into 10 classes based on shape. The 10 classes that equal the  y target variable: 
Our Y variable (target) All 10 Classes 
Galaxy10 dataset (17736 images)
* Class 0 (1081 images): Disturbed Galaxies
* Class 1 (1853 images): Merging Galaxies
* Class 2 (2645 images): Round Smooth Galaxies
* Class 3 (2027 images): In-between Round Smooth Galaxies
*  Class 4 ( 334 images): Cigar Shaped Smooth Galaxies
*  Class 5 (2043 images): Barred Spiral Galaxies
*  Class 6 (1829 images): Unbarred Tight Spiral Galaxies
*  Class 7 (2628 images): Unbarred Loose Spiral Galaxies
*  Class 8 (1423 images): Edge-on Galaxies without Bulge
* Class 9 (1873 images): Edge-on Galaxies with Bulge
Galaxy10 dataset classification labels come from Galaxy Zoo. This is sample of the data below.

![galaxy10_example](https://user-images.githubusercontent.com/104231685/168537714-2df86fcc-aff1-4198-94dd-55aa9dad14ce.png)

"The original Galaxy10 dataset was created with Galaxy Zoo (GZ) Data Release 2 where volunteers classify ~270k of SDSS galaxy images where ~22k of those images were selected in 10 broad classes using volunteer votes. GZ later utilized images from DESI Legacy Imaging Surveys (DECals) with much better resolution and image quality. Galaxy10 DECals has combined all three (GZ DR2 with DECals images instead of SDSS images and DECals campaign ab, c) results in ~441k of unique galaxies covered by DECals where ~18k of those images were selected in 10 broad classes using volunteer votes with more rigorous filtering. Galaxy10 DECals had its 10 broad classes tweaked a bit so that each class is more distinct from each other and Edge-on Disk with Boxy Bulge class with only 17 images in original Galaxy10 was abandoned. The source code for this dataset is released under this repositary so you are welcome to play around if you like, otherwise you can use the compiled Galaxy10 DECals with dowload link below.

These classes are mutually exclusive, but Galaxy Zoo relies on human volunteers to classify galaxy images and the volunteers do not agree on all images. For this reason, Galaxy10 only contains images for which more than 55% of the votes agree on the class. That is, more than 55% of the votes among 10 classes are for a single class for that particular image. If none of the classes get more than 55%, the image will not be included in Galaxy10 as no agreement was reached. As a result, 21785 images after the cut.

The justification of 55% as the threshold is based on validation. Galaxy10 is meant to be an alternative to MNIST or Cifar10 as a deep learning toy dataset for astronomers. Thus astroNN.models.Cifar10_CNN is used with Cifar10 as a reference. The validation was done on the same astroNN.models.Cifar10_CNN. 50% threshold will result a poor neural network classification accuracy although around 36000 images in the dataset, many are probably misclassified and neural network has a difficult time to learn. 60% threshold result is similar to 55% , both classification accuracy is similar to Cifar10 dataset on the same network, but 55% threshold will have more images be included in the dataset. Thus 55% was chosen as the threshold to cut data.

The original images are 424x424, but were cropped to 207x207 centered at the images and then downscaled 3 times via bilinear interpolation to 69x69 in order to make them manageable on most computer and graphics card memory.

There is no guarantee on the accuracy of the labels. Moreover, Galaxy10 is not a balanced dataset and it should only be used for educational or experimental purpose. If you use Galaxy10 for research purpose, please cite Galaxy Zoo and Sloan Digital Sky Survey." - (https://astronn.readthedocs.io/en/latest/galaxy10.html#download-galaxy10-decals, https://astronn.readthedocs.io/en/latest/galaxy10.html)

# Project Planning Questions 
Project Planning Questions: Galaxy Image Classification Project

* What value does this project add? How will the model get used? *  What data do we have currently?
  
  The value that this project will add consists of supporting AI’s advancement in space exploration. These images will be of value to the space industry in educational textbooks for students. This project will help students distinguish variations between galaxies. It will help educate the public on how and what galaxies look like and the architecture in which they are formed.  Additionally, it can help support astronauts in their research when they conduct missions in outer space.  This would also be of value to telescope observatories globally to help advance their research  in their laboratories. Observatories examine and observe celestial objects in the sky. These models can help assist with images to identify those celestial objects.  
 
The model will be used by professionals primarily in the space industry and The data we currently have is an extracted Galaxy10_DECals.h5 dataset that contains 17736 256x256 pixels colored galaxy images separated in a total of 10 classes. The datasets have images with a shape of (17736, 256, 256, 3). The Galaxy 10 DECals images come from “DESI Legacy Imaging Surveys which includes the Beijing- Arizona Sky Survey(BASS), the DECam Legacy Survey(DECaLS) and the Mayall z- band Legacy Survey and the labels come from Galaxy Zoo”, https://github.com/henrysky/Galaxy10.
Dataset Authors: Henry Leung Department of Astronomy & Astrophysics, University of Toronto, Jo Bovy  Department of Astronomy & Astrophysics, University of Toronto
 
How would we get more data if we needed to? 
To get more data, we can extract images of the web and use more datasets, i.e NASA, google images. (We will not be getting any more data for this project. Will be beyond the scope of this project) 
 
Do the results of the model need to be explainable to humans? These results need to be explainable to project managers, hiring managers, recruiters, fellow data scientists, and this is open to public use.  As a result, we will you the classification “Accuracy” and explain the resample if our “y” target variable is unbalanced. 
 
 
How many users will potentially use this model overall? Broad → Narrow 
Broad Space Industry : Rough Estimate of professionals in the data science industry 
Astrophysics students>
-number of Space Professionals in the industry
          More than 179,000 people are employed in the U.S. space industry.   
          Students in Astronomy Education:    
            6,000 professional Astronomers in America 
The total number of students taking an introductory astronomy course at a degree-granting physics or astronomy department is approaching 200,000. ”https://www.aip.org/sites/default/files/statistics/undergrad/enrolldegrees-a-12.3.pdf”
           

 
How many users will potentially use this model at the same time? 
      Approximately : 1- 5 users at a time > 15. 
 
How often should the model be retrained with new images?  We will not be retraining the model with new images. 
 
Do we want the model to make predictions instantly in real-time, or can there be a bit of a delay? 
We want to make model predictions instantly because with as short as delay as possible because we want the user to be able to click on the web application button and receive a classified image. 
 
Can all the model training be done on a simple computer, or do we need to leverage additional computational power? 
The model will be done on a simple computer.  
Our budget constraint is limited to one simple computer. Leveraging google collab as an external computational power to ensure that our simple computer will not crash. 
 
 Do we have any cost / budget limitations / constraints? 
Current cost constraints are that we will be conducting this project at free of cost. 
We will be using a simple laptop computer and building the code in the project in google collab so that model will not crash on a single laptop.
 
What is our “y” or target variable that we are predicting (classes that we are separating our images into)? 
 
* Class 0 (1081 images): Disturbed Galaxies
* Class 1 (1853 images): Merging Galaxies
* Class 2 (2645 images): Round Smooth Galaxies
* Class 3 (2027 images): In-between Round Smooth Galaxies
* Class 4 ( 334 images): Cigar Shaped Smooth Galaxies
* Class 5 (2043 images): Barred Spiral Galaxies
* Class 6 (1829 images): Unbarred Tight Spiral Galaxies
* Class 7 (2628 images): Unbarred Loose Spiral Galaxies
* Class 8 (1423 images): Edge-on Galaxies without Bulge
* Class 9 (1873 images): Edge-on Galaxies with Bulge
 
 


![galaxypurple](https://user-images.githubusercontent.com/104231685/168538698-6fa71da5-cfa7-434d-8a2c-9002698d56eb.jpg)


# Galaxy Web Application Button
As a result, we created an interactive web application button that displays the images and shows below our predicted class of image and the actual class. 

## Please view button with this link:
https://galaxyclassification-347700.uc.r.appspot.com/

Here's whats happening behind the scenes that went in to building the button 
using docker to upload image and build a container deploying to google cloud's registry, app engine

Building application: Button is doing behind the scenes

* 1.) Define images per class: What we want the user experience to be ? How would we define that? 5 images per class so 50 images total --> It will pick 1 image out of 50 to show them from any class

* 2.) Display the image that we picked

* 3.) Now we want to pre-process this image --> so that we can make a prediction
* 4.) Feed this pre-processed image to our model and get back a prediction *What class the image belongs to ?
* 5.) Display the prediction
User's eye

user clicks our button -users see's image that was selected
user see's the prediction that the model made (class of image)
Randomly select 50 image where 5 belong to each of the 10 classes : this is through sampling

# Results: The project's final score received 42 %. Why did we get that score, what can we do to improve the score ? 
* Orginally , we made the images smaller in the pre-processing stage. We could have used bigger images 
* Another reason, we could actually try gray scaling. The color difference can be an upside factor when identifying shapes and patterns 
* Adding ensemble modeling with traditional classification models (through boosting)
* Introduce transfer learning: This is where we introduce pre-trained models as the starting point that allows rapid progress or improved performance. 
* Increase our epochs in our basic neural network from 20 to intervals of +25, +100. (within constraints of budget in project planning questions)
* Switch our optimizers from Adam to Gradient Descent, add sigmoid as a non- linear function(adds non-linearity to our function)
*  In the CNN, increase filter size from 32 to 64. Every layer of filters is there to capture patterns, edges, corners, dots, etc.
