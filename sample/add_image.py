from __future__ import print_function
from stylelens_image.images import Images
from pprint import pprint

api_instance = Images()

image = {}
image['product_id'] = '1234'

try:
  # Added a new Object
  api_response = api_instance.add_image(image)
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->add_image: %s\n" % e)
