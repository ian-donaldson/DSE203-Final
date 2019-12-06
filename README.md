# DSE203-Final

- nlp files can be created through the wordproc-clean notebook (urls may have to be udpated for additional companies)
    - dse203 - wordproc - clean.ipynb
- structured elements of wikipedia page can be obtained through 
    1. toc parse -> dse203 - toc_parse.ipynb
    2. info_box -> dse203_scrape_bottom_infobox.ipynb
    3. scrapy spider -> scrapy_spider/scrapy_spider/spiders/wiki_spider_info.py
- naics codes are obtined from naics_scrape folder
    - naics_scrape/scrape_naics.py
- create_graph_updated notebook used to actually create the graph
    - dse203_create_graph_updated.ipynb

The workflow is:
    1. Run the files above. They will create csv, txt, and json files. You can run scrapy with ```scrapy crawl wiki_company_info -o all.json```. Then move that all.json to the info_box folder and rename it all_info_box.json
    2. Run neo4j server that jupyter notebook can connect to. 
    3. Run dse203_create_graph_updated.ipynb to populate the graph DB


Contributors:
    Faezeahghazi
    Jimmmy
    Kevin
    Ying