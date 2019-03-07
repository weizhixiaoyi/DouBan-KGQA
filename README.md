基于豆瓣, 书籍的知识图谱问答系统

### 1.Json2RDF
> 将Json数据转换为RDF数据，并存储到Jena之中，步骤如下。
1. 将Json数据存储到MySQL之中。
2. 利用Protege构建本体，理解数据格式。
2. 将MySQL数据通过d2rq转换成RDF数据。
3. 利用Jena将RDF数据转换为TDB数据。
4. 利用Jena Fuseki构建推理机制，进行SPARQL查询。

### TODO
- [ ] 命名实体识别和意图识别