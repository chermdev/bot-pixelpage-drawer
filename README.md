# Python script to draw in pixelpage.deno.dev
<div style="text-align: center;">
<img style="max-height: 400px;align-items:center" src="public/pixelpage_flower.png" /></div>

draw.py script sends requests to paint pixels in [pixelpage.deno.dev](pixelpage.deno.dev)


## How to draw

The tool used to draw is
https://es.pixilart.com/
<br>
<img style="max-height: 400px;" src="public/pixilart_banner.png" />

Before starting, we need to configure the tool.

### Import colors palette
First we need to import the colors supported by the pixelpage.
1. Create a new palette
<br>
<img style="max-height:200px;margin-right:50px;" src="public/pixilart_colors_new_palette.png"/>
<img style="max-height:150px;" src="public/pixilart_set_palette_name.png"/>
2. Import colors clicking on the next button and add the next colors  `ff0000,00ff00,0000ff,ffff00,00ffff,ff00ff,ffffff,000000`
<br>
<img style="max-height:200px;margin-right:50px;" src="public/pixilart_colors_import.png"/>
<img style="max-height:150px;" src="public/pixilart_set_colors.png"/>

3. We're ready with the colors of the pixelpage
<br>
<img style="max-height:200px;" src="public/pixilart_colors.png"/>

### Set canvas dimension
1. Edit canvas with the tool or from the bar options.
<br>
<img style="max-height:200px;" src="public/pixilart_button_edit_canvas.png"/>
or 
<img style="max-height:150px;" src="public/pixilart_button_resize_canvas.png"/>
2. Set 16x16 and enable the checkmark if you already imported the image to resize it.
<br>
<img style="max-height:200px;" src="public/pixilart_canvas_resize.png"/>

### Import image
In this example we will use the 
<br>
<a href="flower_example.jpg">
    flower_example.jpg
    <br>
    <img style="max-height:250px;" src="flower_example.jpg"/>
</a>

1. Import the 16x16 image.
if the image is not 16x16 it will be automatically resized.
<br>
<div style="display:flex;align-items:center;">
    <img style="max-height:250px;margin-right:50px;" src="public/pixilart_import.png"/>
    <img style="max-height:250px;" src="public/pixilart_flower_example.png"/>
</div>
2. Apply the color palette to replace the colors with similar supported colors.
<br>
<div style="display:flex;align-items:center;">
    <img style="max-height:180px;margin-right:50px;" src="public/pixilart_apply_palette.png"/>
    <img style="max-height:250px;" src="public/pixilart_flower_example_color_palette.png"/>
</div>
3. Verify and manually edit the pixels if required. In this case some yellow pixels were missing.
<br>
<img style="max-height:250px;" src="public/pixilart_flower_example_complete.png"/>

### Download pixel art
When we are ready, click on the download option on the top bar and save the image as png.
<br>
<img style="max-height:250px;" src="public/pixilart_download.png"/>