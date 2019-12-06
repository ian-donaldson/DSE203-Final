# DSE203-Final

- Nlp files can be created through the wordproc-clean notebook (urls may have to be udpated for additional companies)
    - dse203 - wordproc - clean.ipynb
- Structured elements of wikipedia page can be obtained through 
    1. toc parse -> dse203 - toc_parse.ipynb
    2. info_box -> dse203_scrape_bottom_infobox.ipynb
    3. scrapy spider -> scrapy_spider/scrapy_spider/spiders/wiki_spider_info.py
- Naics codes are obtained from naics_scrape folder
    - naics_scrape/scrape_naics.py
- Create_graph_updated notebook used to actually create the graph
    - dse203_create_graph_updated.ipynb

-The workflow is:
1. Run the files above. They will create csv, txt, and json files. You can run scrapy with 
```scrapy crawl wiki_company_info -o all.json``` . Then move that all.json to the info_box folder and rename it all_info_box.json . Also some manual data cleaning was done from the scrapy dump and those are found in info_box folder (leave those as is)
2. Run neo4j server that jupyter notebook can connect to. 
3. Run dse203_create_graph_updated.ipynb to populate the graph DB

- database file is in root repo structure (databases.zip)


Contributors:
    Faezeahghazi
    Jimmy
    Kevin
    Ying
