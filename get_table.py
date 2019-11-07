import os
import pandas as pd

def get_table(company_name, company_wiki_url, file_path):

    # set class name for tables.
    attrs = {'class': ['infobox vcard', 'wikitable', 'wikitable unsortable']}

    # get all tables.
    tables = pd.read_html(company_wiki_url, attrs=attrs, header=0)

    # save as csv file.
    for num, table in enumerate(tables):
        path = os.path.join(file_path, company_name + '_' + str(num).zfill(2))
        table.to_csv(path)


# company_name='Microsoft'
# company_wiki_url='https://en.wikipedia.org/wiki/Microsoft'
# file_path='./data' // You can set your own file path //

# get_table(company_name,company_wiki_url,file_path)