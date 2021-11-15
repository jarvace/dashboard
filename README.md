# dashboard
连接mysql_data数据库并获取智慧闸口仿真数据

## 数据库结构

```mermaid
graph LR
db(mysql_model数据库) --> | 用于记录实际仿真数据 | table1(data表)
db --> |用于存放神经网络预测数据| table2(forcast表)
```


