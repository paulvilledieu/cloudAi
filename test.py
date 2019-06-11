import http.client, urllib.parse, base64, json
import requests
from PIL import Image


headers = {
   'Content-Type': 'application/octet-stream',
   'Training-key': '389a2589def94355916b1d5e86e196d4',
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'tagIds': ['393a7970-13e5-4fdc-9719-72b4caafab2b']
})


def main():
    img_data = Image.open("img.png")
    img_data = base64.b64encode(img_data.tobytes())
    try:
        api_url = "https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Training/projects/d618a87a-b01d-424c-a8d4-e5984af0552f/images?{}".format(params)
        print("API URL:{}".format(api_url))

        r = requests.post(api_url,
                    headers=headers,
                    data=img_data)

        parsed = r.json()
        print(parsed)
    except:
        print('error')

if __name__ == "__main__":
    main()
