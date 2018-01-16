from __future__ import print_function
from stylelens_image.images import Images
from pprint import pprint

api_instance = Images()

ids = ['5a5b2337632e51d6e2b5cbf5', '5a5b2c7d632e51d6e2b6de13']

try:
  api_response = api_instance.get_images_by_ids(ids)
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_images_by_ids: %s\n" % e)
