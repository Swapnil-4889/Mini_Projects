pkg load image             %Image package has been provided in the folder please install

var = input("Enter the image file name : ");



I=imread(var);             % Image reading step
%imshow(I)

I=rgb2gray(I);                     %Here we convert RGB image to Grayscale image
%imshow(I)

J=im2bw(I,graythresh(I));       %Now we convert this grayscale image to a black and white image(binary) image
%imshow(J)

Img_without_holes = imfill(J,'holes');    %Now imfill is used to detect and clear holes in the image


Img_without_holes = medfilt2(Img_without_holes); %Now using medianfilter the noise is removed




[L,N] = bwlabel(Img_without_holes);   %Now we apply labels for each connected components in binary image and store it in [L,N]
				       %N stores the number to holes detected(or the no. of connected objects found)
					%L is the label matrix
printf("The number of objects different from the background are = %d\n",N)
