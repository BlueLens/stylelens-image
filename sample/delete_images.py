from __future__ import print_function
from stylelens_image.images import Images
from pprint import pprint

api_instance = Images()

try:
  api_response = api_instance.delete_images('1234', except_version=True)
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->add_image: %s\n" % e)
