import scrapy


class ScrapeTableSpider(scrapy.Spider):
    name = "scrape_ms"
    allowed_domains = [
        "https://docs.microsoft.com/en-us/azure/virtual-machines/security-recommendations"
    ]
    start_urls = [
        "http://https://docs.microsoft.com/en-us/azure/virtual-machines/security-recommendations/"
    ]

    def start_requests(self):
        urls = [
            "https://docs.microsoft.com/en-us/azure/virtual-machines/security-recommendations",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath("descendant-or-self::table//tbody/tr"):
            yield {
                "Recommendation": row.xpath("td[1]//text()").extract_first(),
                "Comments": row.xpath("td[2]//text()").extract_first(),
                "Security Center": row.xpath("td[3]//text()").extract_first(),
            }
