from __future__ import print_function
from stylelens_image.images import Images
from pprint import pprint

api_instance = Images()

try:
  api_response = api_instance.get_image("5a515066dbfef20d384529b3", version_id='5a50d4ba4dfd7d90b8b9369a')
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->add_image: %s\n" % e)
