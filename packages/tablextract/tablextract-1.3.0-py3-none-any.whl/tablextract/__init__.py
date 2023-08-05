from tablextract.utils import *
from tablextract.table_processing import *

def tables(url, css_filter='table', xpath_filter=None, request_cache_time=0, add_image_text=True, add_link_urls=False):
	document = cache(get_with_render, (url, css_filter), identifier=url, cache_life=request_cache_time)
	document = soup(document, 'html.parser')
	res = []
	for table in locate(url, document):
		if xpath_filter == None or table.xpath == xpath_filter:
			try:
				segmentate(table, add_image_text, add_link_urls, url)
				if len(table.features) < 2 or len(table.features[0]) < 2: continue
				functional_analysis(table)
				structural_analysis(table)
				interpret(table)
				compute_score(table)
			except:
				log_error()
				table.error = format_exc()
			res.append(table)
	return res