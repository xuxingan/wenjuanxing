import meilisearch
import json

client = meilisearch.Client('http://150.158.79.10:7700/')


# 导入数据
# json_file = open('culture.json')
# cultures = json.load(json_file)
# client.index('cultures').add_documents(cultures)

# 搜索
def search(keyword):
    result = client.index('cultures').search(keyword)
    count = result.get('estimatedTotalHits')
    if count > 0:
        content = result.get('hits')[0].get('content')
    else:
        content = ''
    return content


if __name__ == '__main__':
    res = search('爱知人的三大职责清楚宣传推荐')
    print(res)
