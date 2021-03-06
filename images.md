Wix Media Python SDK
--------------------
Image Manipulation
===========================
Wix Media Platform provides web developers a versatile infrastructure for image manipulations easily accessable through the [Wix Media Images RESTful API](http://media.wixapps.net/playground/docs/images_restfull_api.html). The Wix Media Python library provides a wrapper over the API.

## Usage ##

### Uploading Images ###

It’s easy to upload images using the Wix Media Python library. For example:

```python
from wix import media

client = media.Client(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
image  = client.upload_image_from_path('/files/images/parrot.jpg')

image_id = image.get_id()
print image_id
```

The code snippet above gives the following image-id as output:
```
wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/parrot.jpg
```

__Note__: Wix Media Services supports the following images file formats: JPEG, GIF and PNG.

### Rendering Images ###

After uploading an image, you can easily apply any manipulation as described later in the document.
For example:

```python
from wix import media

image_id = 'wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/parrot.jpg'

client = media.Client()
image  = client.get_image_from_id(image_id)

print image.fit(width=420, height=420) \
           .unsharp() \
           .oil() \
           .adjust(brightness=10, contrast=-15) \
           .get_url()
```

The last code snippet applies image manipulation on a previously uploaded image and prints the URL for rendering the manipulated image. The URL can be embedded in an HTML *img* tag:

```html
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,usm_0.50_0.20_0.00,oil,con_-15,br_10/parrot.jpg
```
----------------
__Note__: 
All rendered URLs (as shown in the previous *img* tag) conform to the following structure:
```
http://host/user-id/media-type/file-id/version/operation/params(p_value, comma-separated),manipulations(p_value, comma-separated)/filename.ext
```
Using this python package eliminates the need to manually construct such urls. For more information about the URLs browse [Wix Media Images RESTful API](http://media.wixapps.net/playground/docs/images_restfull_api.html) documentation.

-----------------

#### Image Transformation Operations ####

The following image transformations are available (one per image maipulation request):
- Canvas
- Fill
- Fit
- Crop


##### Canvas #####

Resizes the image canvas, filling the width and height boundaries and crops any excess image data. The resulting image will match the width and height constraints without scaling the image.

```python
canvas(width, height, alignment=None, ext_color=None)
```

Parameter | value | Description
----------|-------|------------
width *(mandatory)*|Integer|The width constraint (pixels).
height *(mandatory)*|Integer|The height constraint (pixels).
alignment *(optional)*|string|The position pointing the place from which to start cropping  the picture. See optional values in the table below.```default: center```
ext_color *(optional)*|string (RGB)| the extension color, in case the canvas size is larger than the image itself. Please note that the string expected is a 6 hexadecimal digits representing RRGGBB. 

alignment optional values:

Value | Description
------|------------
center|Focus on the center of the image, both vertical and horizontal center.
top|Focus on the top of the image, horizontal center.
top-left|Focus on the top left side of the image.
top-right|Focus on the top right side of the image.
bottom|Focus on the bottom of the image, horizontal center.
bottom-left|Focus on the bottom left side of the image.
bottom-right|Focus on the bottom right side of the image.
left|Focus on the left side of the image, vertical center.
right|Focus on the right side of the image, vertical center.
face|Focus on a face on the image. Detects a face in the picture and centers on it. When multiple faces are detected in the picture, the focus will be on one of them.
faces|Focus on all faces in the image. Detects multiple faces and centers on them. Will do a best effort to have all the faces in the new image, depending on the size of the new canvas.

*Sample Request:*
```python
print image.canvas(width=480, height=240, ext_color='ffffff').get_url()
```
would generate the URL:
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/canvas/h_240,w_480,c_ffffff/parrot.jpg
```

##### Fill #####

Creates an image with the specified width and height while retaining original image proportion. If the requested proportion is different from the original proportion, only part of the original image may be used to fill the area specified by the width and height.

```python
fill(width, height, resize_filter=None, alignment=None)
```

Parameter | value | Description
----------|-------|------------
width *(mandatory)*|Integer|The width constraint (pixels).
height *(mandatory)*|Integer|The height constraint (pixels).
resize_filter *(optional)*|string|The resize filter to be used. One of the values below. ```default: LanczosFilter```
alignment *(optional)*|string|The position pointing the place from which to start cropping  the picture. See optional values in the table below.```default: center```

alignment optional values:

Value | Description
------|------------
center|Focus on the center of the image, both vertical and horizontal center.
top|Focus on the top of the image, horizontal center.
bottom|Focus on the bottom of the image, horizontal center.
left|Focus on the left side of the image, vertical center.
right|Focus on the right side of the image, vertical center.
face|Focus on a face on the image. Detects a face in the picture and centers on it. When multiple faces are detected in the picture, the focus will be on one of them.

resize_filter optional values + descriptions (view links):

[PointFilter](http://www.imagemagick.org/Usage/filter/#point)|[BoxFilter](http://www.imagemagick.org/Usage/filter/#box)|[TriangleFilter](http://www.imagemagick.org/Usage/filter/#triangle)|[HermiteFilter](http://www.imagemagick.org/Usage/filter/#hermite)
--------|---------|---------|--------
[**HanningFilter**](http://www.imagemagick.org/Usage/filter/#hanning)|[**HammingFilter**](http://www.imagemagick.org/Usage/filter/#hamming)|[**BlackmanFilter**](http://www.imagemagick.org/Usage/filter/#balckman)|[**GaussianFilter**](http://www.imagemagick.org/Usage/filter/#gaussian)
[**QuadraticFilter**](http://www.imagemagick.org/Usage/filter/#quadratic)|[**CubicFilter**](http://www.imagemagick.org/Usage/filter/#cubics)|[**CatromFilter**](http://www.imagemagick.org/Usage/filter/#catrom)|[**MitchellFilter**](http://www.imagemagick.org/Usage/filter/#mitchell)
[**JincFilter**](http://www.imagemagick.org/Usage/filter/#jinc)|[**SincFilter**](http://www.imagemagick.org/Usage/filter/#sinc)|[**SincFastFilter**](http://www.imagemagick.org/Usage/filter/#sinc)|[**KaiserFilter**](http://www.imagemagick.org/Usage/filter/#kaiser)
[**WelchFilter**](http://www.imagemagick.org/Usage/filter/#welch)|[**ParzenFilter**](http://www.imagemagick.org/Usage/filter/#parzen)|[**BohmanFilter**](http://www.imagemagick.org/Usage/filter/#bohman)|[**BartlettFilter**](http://www.imagemagick.org/Usage/filter/#bartlett)
[**LagrangeFilter**](http://www.imagemagick.org/Usage/filter/#lagrange)|[**LanczosFilter**](http://www.imagemagick.org/Usage/filter/#lanczos)|[**LanczosSharpFilter**](http://www.imagemagick.org/Usage/filter/#lanczos_sharp)|[**Lanczos2Filter**](http://www.imagemagick.org/Usage/filter/#lanczos2)
[**Lanczos2SharpFilter**](http://www.imagemagick.org/Usage/filter/#lanczos2sharp)|[**RobidouxFilter**](http://www.imagemagick.org/Usage/filter/#robidoux)|[**RobidouxSharpFilter**](http://www.imagemagick.org/Usage/filter/#robidoux_sharp)|[**CosineFilter**](http://www.imagemagick.org/Usage/filter/#cosine)

*Sample Request:*

```python
print image.fill(width=480, height=240).get_url()
```
would generate the URL:
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fill/h_240,w_480/parrot.jpg
```

##### Fit #####

Resizes the image to fit to the specified width and height while retaining original image proportion. The entire image will be visible but not necessarily fill the area specified by the width and height.

```python
fit(width, height, resize_filter=None)
```

Parameter | value | Description
----------|-------|------------
width *(mandatory)*|Integer|The width constraint (pixels).
height *(mandatory)*|Integer|The height constraint (pixels).
resize_filter *(optional)*|string|The resize filter to be used. One of the in the table below. ```default: LanczosFilter```

resize_filter optional values + descriptions (view links):

[PointFilter](http://www.imagemagick.org/Usage/filter/#point)|[BoxFilter](http://www.imagemagick.org/Usage/filter/#box)|[TriangleFilter](http://www.imagemagick.org/Usage/filter/#triangle)|[HermiteFilter](http://www.imagemagick.org/Usage/filter/#hermite)
--------|---------|---------|--------
[**HanningFilter**](http://www.imagemagick.org/Usage/filter/#hanning)|[**HammingFilter**](http://www.imagemagick.org/Usage/filter/#hamming)|[**BlackmanFilter**](http://www.imagemagick.org/Usage/filter/#balckman)|[**GaussianFilter**](http://www.imagemagick.org/Usage/filter/#gaussian)
[**QuadraticFilter**](http://www.imagemagick.org/Usage/filter/#quadratic)|[**CubicFilter**](http://www.imagemagick.org/Usage/filter/#cubics)|[**CatromFilter**](http://www.imagemagick.org/Usage/filter/#catrom)|[**MitchellFilter**](http://www.imagemagick.org/Usage/filter/#mitchell)
[**JincFilter**](http://www.imagemagick.org/Usage/filter/#jinc)|[**SincFilter**](http://www.imagemagick.org/Usage/filter/#sinc)|[**SincFastFilter**](http://www.imagemagick.org/Usage/filter/#sinc)|[**KaiserFilter**](http://www.imagemagick.org/Usage/filter/#kaiser)
[**WelchFilter**](http://www.imagemagick.org/Usage/filter/#welch)|[**ParzenFilter**](http://www.imagemagick.org/Usage/filter/#parzen)|[**BohmanFilter**](http://www.imagemagick.org/Usage/filter/#bohman)|[**BartlettFilter**](http://www.imagemagick.org/Usage/filter/#bartlett)
[**LagrangeFilter**](http://www.imagemagick.org/Usage/filter/#lagrange)|[**LanczosFilter**](http://www.imagemagick.org/Usage/filter/#lanczos)|[**LanczosSharpFilter**](http://www.imagemagick.org/Usage/filter/#lanczos_sharp)|[**Lanczos2Filter**](http://www.imagemagick.org/Usage/filter/#lanczos2)
[**Lanczos2SharpFilter**](http://www.imagemagick.org/Usage/filter/#lanczos2sharp)|[**RobidouxFilter**](http://www.imagemagick.org/Usage/filter/#robidoux)|[**RobidouxSharpFilter**](http://www.imagemagick.org/Usage/filter/#robidoux_sharp)|[**CosineFilter**](http://www.imagemagick.org/Usage/filter/#cosine)

*Sample Request:*

```python
print image.fit(width=480, height=240, resize_filter=media.Lanczos2SharpFilter).get_url()
```
would generate the URL:
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_240,w_480,rf_25/parrot.jpg
```

##### Crop #####

Crops the image based on the supplied coordinates, starting at the x, y coordinates along with the width and height parameters.

```python
crop(x, y, width, height)
```

Parameter | Value | Description
----------|-------|------------
x *(mandatory)*|Integer|The x-pixel-coordinate to start cropping from. (represents the top-left corner point of the cropped area).
y *(mandatory)*|Integer|The y-pixel-coordinate to start cropping from. (represents the top-left corner point of the cropped area).
width *(mandatory)*|Integer|The width constraint (pixels).
height *(mandatory)*|Integer|The height constraint (pixels).

*Sample Request:*
```python
print image.crop(x=1900, y=800, width=800, height=900).get_url()
```
would generate the URL:
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/crop/h_900,w_800,x_1900,y_800/parrot.jpg
```

#### Image Adjustment Operation ####

##### Adjust #####

Applies an adjustment to an image.

```python
adjust(brightness=None, contrast=None, saturation=None, hue=None):
```
the parameters may be one or more of the following options:

function | parameter(s) | Description
---------|--------------|------------
brightness *(optional)*|Integer (%)|brightness. ```value between -100 and 100```
contrast *(optional)*|Integer (%)|contrast ```value between -100 and 100```
saturation *(optional)*|Integer (%)|saturation ```value between -100 and 100```
hue *(optional)*|Integer (%)|hue ```value between -100 and 100```

*Sample Request:*
```python
print image.fit(width=120, height=120) \
           .adjust(brightness=10, contrast=-15) \
           .get_url()
```
would generate the URL: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_120,w_120,con_-15,br_10/parrot.jpg
```

#### Oil Filter ####

Applies an oil paint effect on an image.

```python
oil()
```

*Sample Request:*
```python
print image.fit(width=420, height=420) \
           .oil() \
           .get_url()
```
would generate the URL: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,oil/parrot.jpg
```

#### Negative Filter ####

Negates the colors of the image.

```python
neg()
```

*Sample Request:*
```python
print image.fit(width=420, height=420) \
           .neg() \
           .get_url()
```
would generate the URL: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,neg/parrot.jpg
```


#### Pixelate Filter ####

Applies a pixelate effect to the image. The parameter value is the width of pixelation squares (in pixels).

```python
pixelate(value)
```

*Sample Request:*
```python
print image.fit(width=420, height=420) \
           .pixelate(5) \
           .get_url()
```
would generate the URL: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,pix_5/parrot.jpg
```

#### Blur Filter ####

Applies a blur effect to the image. The parameter value indicates the blur in percents.

```python
blur(value)
```

*Sample Request:*
```python
print image.fit(width=420, height=420) \
           .blur(5) \
           .get_url()
```
would generate the URL: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,blur_5/parrot.jpg
```

*** 

#### Sharpening Filter ####

Applies a sharpening filter on the image, using the radius parameter. please note that the radius’ value is a float number.

```python
sharpen(radius)
```
parameters:

Value | Description | Valid values
------|-------------|-------------
radius|sharpening mask radius|0 to image size


*Sample Request:*
```python
print image.fit(width=420, height=420) \
           .sharpen(0.8) \
           .get_url()
```
would generate the URL: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,shrp_0.8/parrot.jpg
```

***

#### Unsharp Mask Filter ####

The Unsharp Mask, applies the filter using radius, amount & threshold parameters. (see table below)

```python
unsharp(radius=0.5, amount=0.2, threshold=0.0)
```

optional parameters:

Value | Description | Valid values
------|-------------|-------------
radius|sharpening mask radius|0 to image size
amount|sharpening mask amount|0 to 100
threshold|shapening mask threshold|0 to 255

*Sample Request:*
```python
print image.fit(width=420, height=420) \
           .unsharp(radius=0.4, amount=0.2, threshold=0.0) \
           .get_url()
```
would generate the URL: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,usm_0.40_0.20_0.00/parrot.jpg
```

#### JPEG Options ####

Extra options for JPEGs only:

option | parameter(s) | description
-------|------------|------------
baseline|-|An option for JPEGs only. Applies baseline encoding on the image, instead of progressive encoding.
quality|Integer (%)|Quality of the image, values between 0 and 100 

*Sample Requests:*
```python
print image.fit(width=420, height=420) \
           .baseline() \
           .get_url()
```
would generate the URL:
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,bl/parrot.jpg
```
and:
```python
print image.fit(width=420, height=420) \
           .quality(35) \
           .get_url()
```
would generate: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,q_35/parrot.jpg
```

### Composite Image Manipulation ###

The Image API allows linking several manipulations one after the other. 

For example:

```python
print image.fit(width=420, height=420) \
           .crop(x=60, y=60, width=300, height=300) \
           .unsharp() \
           .get_url()

```
would generate: 
```
http://media.wixapps.net/wixmedia-samples/images/cdf1ba9ec9554baca147db1cb6e011ec/v1/fit/h_420,w_420,q_35/fit/h_420,w_420/crop/h_300,w_300,x_60,y_60,usm_0.50_0.20_0.00/parrot.jpg
```

### Best Paractices ###

* When Fill or Fit are used it is recomended to apply Unsharp Mask filter on the result:
```python
print image.fit(width=420, height=420) \
           .unsharp() \
           .get_url()
```

* If the image is in JPEG format, it is recomended to set qulity to 75:

```python
print image.fit(width=420, height=420) \
           .unsharp() \
           .quality(75) \
           .get_url()
```

The recomendations above, describe simple image optimization while maintaining good balance between output size and quality.
