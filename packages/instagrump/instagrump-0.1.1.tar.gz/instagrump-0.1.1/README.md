# Instagrump
Just a simple Instagram Public API wrapper. The codes are self-explanatory.

### Example usage
Installing:
```sh
pip3 install instagrump 
```

Importing:
```sh
from instagrump import Profile,  Content 
```

Initialize Profile class:
```sh
username = Profile('ig_username')
```

Also Content class:
```sh
a_content = Content('url_with_shortcode_from_Profile')
```

Get :
```sh
a_content.get_content()
```
#### Helpful tip
To get all class attribute:
```sh
dir(your_class_here)
```

### Todos

 - Write MORE Documentations
 - Sleep

License
----
MIT

