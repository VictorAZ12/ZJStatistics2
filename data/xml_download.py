import asyncio
import aiohttp
import urllib.parse

async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Modify the filename as per your requirement
            filename = url.split('/')[-1]
            decoded_filename = urllib.parse.unquote(filename)
            with open("./xml_files/"+decoded_filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)
            print(f"Downloaded: {decoded_filename}")

async def main():
    with open("./xmls_anni1.txt", "r") as f:
        urls = [url.rstrip('\n') for url in f.readlines()]
    
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_file(url))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
