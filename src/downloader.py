import requests
import os

def download_file(url, folder_name):
  """Downloads a file from a link to a folder.

  Args:
    url: The URL of the file to download.
    folder_name: The name of the folder to save the file to.

  Returns:
    The path to the downloaded file.
  """

  filename = os.path.basename(url)
  file_path = os.path.join(folder_name, filename)

  if not os.path.exists(folder_name):
    os.mkdir(folder_name)

  with open(file_path, 'wb') as f:
    response = requests.get(url, stream=True)
    for chunk in response.iter_content(chunk_size=1024):
      f.write(chunk)

  return file_path