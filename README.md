#meme-generator-api

The meme-generator-api is a simple api for creating memes. You can use it via GUI or just by makeing a get-request


##Usage - GUI

The GUI is pretty much self explaining and intuitiv. The website is currently running on [meme-gen.github.io](https://meme-gen.github.io).

##Usage - API

To call the API you need 4 Parameters:
- Textsize (integer value between 50 and 100)
- Picture number
- Text to be displayed at the top
- Text to be displayed at the bottom
  
if you got these 4 things, you can make a simple get-request in your browser.

```
function httpGet(Textsize, Picture_number, Text_at_top, Text_at_botttom)
{   
    url = "memegen.pythonanywhere.com/memegen/" + Textsize + "/" + Picture_number + "/" + Text_at_top + "/" + Text_at_bottom
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
```

This will return a webpage with the image embedded in it
