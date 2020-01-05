+++
# Recent Posts widget.
# Displays recent posts from `content/post/`.
widget = "pages"
active = true
date = 2018-10-26T00:00:00
headless = true

title = "Writing"
subtitle = ""

weight = 40

[content]
  page_type = "post"
  count = 3
  offset = 0
  order = "desc"

[content.filters]
  tag = ""
  category = ""
  publication_type = ""
  exclude_featured = false

# Number of posts to list.

[design]
  # Toggle between the various page layout types.
  #   1 = List
  #   2 = Compact
  #   3 = Card
  #   4 = Citation (publication only)
  view = 2

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.
  
  # Background color.
  # color = "navy"
  
  # Background gradient.
  # gradient_start = "DeepSkyBlue"
  # gradient_end = "SkyBlue"
  
  # Background image.
  # image = "background.jpg"  # Name of image in `static/img/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  # text_color_light = true  
  
[advanced]
 # Custom CSS. 
 css_style = ""
 
 # CSS class.
 css_class = ""
+++
