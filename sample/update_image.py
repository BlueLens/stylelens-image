from __future__ import print_function
from stylelens_image.images import Images
from pprint import pprint

api_instance = Images()

version_id = '2234'

image = {}
image['product_id'] = '1234sdhjfddf'
image['host_code'] = '13'
image['product_no'] = '1111'
image['version_id'] = version_id

try:
  # Added a new Object
  api_response = api_instance.add_image(image)
  if api_response is not None:
    if 'upserted' in api_response:
      image_id = str(api_response['upserted'])
      print(image_id)
      image = api_instance.get_image(image_id)
      print(image)

      image['images'] = 'bok'

      res = api_instance.update_image(image)
      print(res)

except Exception as e:
  print("Exception when calling ProductApi->add_image: %s\n" % e)
