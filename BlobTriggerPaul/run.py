import logging
import azure.functions as func
import http.client, urllib.parse, base64, json
import requests

headers = {
   'Content-Type': 'application/octet-stream',
   'Training-key': '389a2589def94355916b1d5e86e196d4',
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    "tagIds": ["393a7970-13e5-4fdc-9719-72b4caafab2b"]
})


def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    img_data = myblob.read()
    try:
        api_url = "https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Training/projects/d618a87a-b01d-424c-a8d4-e5984af0552f/images?tagIds[]=393a7970-13e5-4fdc-9719-72b4caafab2b"
        logging.info("API URL:{}".format(api_url))

        r = requests.post(api_url,
                    headers=headers,
                    data=img_data)

        parsed = r.json()
        logging.info("Response:")
        logging.info(json.dumps(parsed, sort_keys=True, indent=2))
    except:
        logging.error('Request Error')