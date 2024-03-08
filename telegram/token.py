# def search(arr, N, x):
#     for i in range(0, N):
#         if (arr[i] == x):
#             return i
#     return -1
#
#
# # Driver Code
# if __name__ == "__main__":
#     arr = [2, 3, 4, 10, 40]
#     x = 10
#     N = len(arr)
#
#     # Function call
#     result = search(arr, N, x)
#     if (result == -1):
#         print("Element is not present in array")
#     else:
#         print("Element is present at index", result)

from concurrent.futures import ThreadPoolExecutor
import requests
def download_image(item):
    url = item['url']
    id = item['id']
    image_data = None
    response = requests.get(url)
    image_data = response.content
    filename = f'images/{id}.jpg'
    with open(filename, 'wb') as image_file:
        image_file.write(image_data)
        print(f'{filename} was downloaded...')
URL = 'https://jsonplaceholder.typicode.com/photos'
rs = requests.get(URL)
if rs.ok:
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(download_image,rs.json())