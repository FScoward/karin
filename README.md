# Shell DEBUG
`scrapy shell 'url'`

# タイトルを取得する
response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[1]/div[2]/h3/text()').extract()

# 本文を取得する
response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[2]/div/div[2]/div[3]//text()').extract()

# 投稿日を取得する
response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[3]/ul/li/text()').extract()

# 次へのリンクを取得する
response.xpath('/html/body/div/div/div[1]/div/div/div[1]/div[1]/div[3]/div[2]/a/@href').get()