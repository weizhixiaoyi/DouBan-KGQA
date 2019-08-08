本项目构建了完整的基于豆瓣电影、书籍的知识图谱问答系统，包括**从豆瓣原始数据的爬取**、**豆瓣原始数据转换得到RDF数据**、**三元组数据的存储与检索**、**问句理解和答案推理**、**微信公众号部署**等环节，在此分享给大家，共同学习。为帮助理解，可参考以下文章进行实现知识图谱问答系统，文章已更新完成。

1. [电影知识图谱问答（一）|爬取豆瓣电影与书籍详细信息](https://weizhixiaoyi.com/archives/287.html)
2. [电影知识图谱问答（二）|生成298万条RDF三元组数据](https://weizhixiaoyi.com/archives/296.html)
3. [电影知识图谱问答（三）|Apache Jena知识存储及SPARQL知识检索](https://weizhixiaoyi.com/archives/341.html)
4. [电影知识图谱问答（四）| 问句理解及答案推理](https://weizhixiaoyi.com/archives/368.html)
5. [电影知识图谱问答（五）| BM-KGQA Demo](https://weizhixiaoyi.com/archives/380.html)

---

要求: Ubuntu or MacOS, python3.6, [jieba, refo, SPARQLWrapper, web]依赖包


### 使用方法
#### 1.下载数据
因数据文件过大，所以将文件放到百度云，链接: https://pan.baidu.com/s/1JmyPbNM2aqKn6a6K0b-6kw 提取码: 7ndd。下载完成后放入到data/文件夹内即可。

#### 2. 修改配置文件路径
修改DouBan-KGQA/json2jena/rdf2jena/apache-jena-fuseki-3.10.0.2/run/configuration/fuseki_conf.ttl中ja:rulesFrom和tdb:location路径地址。

#### 3.启动Apache Server
进入到DouBan-KGQA/json2jena/rdf2jena/apache-jena-fuseki-3.10.0.2/路径下，启动fuseki-server。
```python
cd DouBan-KGQA/json2jena/rdf2jena/apache-jena-fuseki-3.10.0.2/ 
./fuseki-server
```


#### 4.启动query_main.py
启动query_main.py进行知识图谱问答。
> python query_main.py
