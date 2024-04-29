import asyncio
import httpx
from parsel import Selector


class DomCrawler:
    MAIN_URL = 'https://www.house.kg/snyat'
    BASE_URL = 'https://www.house.kg'

    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(url)
        return response.text

    def get_title(self, page: str):
        html = Selector(page)
        title = html.css('title::text').get()
        return title

    def get_houses_links(self, page: str):
        html = Selector(page)
        links = html.css('.title a::attr(href)').getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links

    async def get_houses(self):
        list = []
        async with httpx.AsyncClient() as client:
            for i in range(1,11):
                url = f'{self.MAIN_URL}?page={i}'
                listik = asyncio.create_task(self.get_page(url, client))
                list.append(listik)
            results = await asyncio.gather(*list)
            all_links = []
            for result in results:
                links = self.get_houses_links(result)
                all_links.extend(links)
        for i, link in enumerate(all_links, start=1):
            print(f"{i}. {link}")
        return all_links[:9]


if __name__ == '__main__':
    scrap = DomCrawler()
    asyncio.run(scrap.get_houses())

