from elasticsearch import Elasticsearch 

es =Elasticsearch([{'host': 'localhost', 'port': 9200}])

# query={"query" : {
#         "match" : {"topic":"My"}
#     }}


def esearch_result(search_term=""):
    # body={
    #     "match" : {"topic":search_term}
    # }
    body={
        "multi_match":{
            "query":search_term,
            "fields":["title","topic"],
        }
    }

    res = es.search(index="armysearch", query=body, size=1000)
    #print(res)
    hits = res["hits"]["hits"]
    results=[]
    for item in hits:
        #if i want specific or only url
        #    print(item["_source"]["title"])
        final_title=(item["_source"]["title"])
        final_url=(item["_source"]["url"])
        results_list=(final_title,final_url)
        results.append(results_list)
        #print(result)
    return results


