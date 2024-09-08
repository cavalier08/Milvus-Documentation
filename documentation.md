### How to install Milvus

1. Download Docker through the link [here](https://docs.docker.com/engine/install/)
2. Open up terminal and copy-paste to install Milvus
```curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh```

```bash standalone_embed.sh start```

3. Install Attu by copy-pasting 
`docker run -p 8000:3000 -e HOST_URL=http://{ your machine IP }:8000 -e MILVUS_URL={your machine IP}:19530 zilliz/attu:latest`. 
You should replace ```{ your machine IP }``` with your machine's IP address, which you can find by entering ```ipconfig getifaddr en0```. Look for the **IPv4 address**.
Attu is the GUI for Milvus, and will allow you to directly view your databases and collections within Milvus.
4. Open up Docker and click start on both Attu and Milvus. You should see 3 containers under Milvus-Download: ```milvus-etcd```, ```milvus-minio```, and ```milvus-standalone```. If not, you probably downloaded Milvus Standalone instead of Milvus Lite
5. In Docker under Attu, click on the port link that says ```8000:3000```. To log into Attu, replace ```127.0.0.1``` with you IP address. Ex: ```123.45.67.89:19530```

### How to use Milvus
To directly access Milvus, we need an SDK that can communicate between our computer and Milvus. The library used here is Pymilvus, which can be installed by running ```pip install pymilvus``` in your terminal.

To insert data into a collection, refer to the file [```load_data.py```](https://github.com/cavalier08/Milvus-Documentation/blob/main/load_data.py). When complete, click on the button that says ```unloaded``` in Attu and wait for the data to load.

### Common problems & Issues
1. Attu not connecting to Milvus servers

Make sure that the IP address in the login page matches the IP address of your computer. It should NOT say localhost or 127.0.0.1. Also make sure that you are not using a VPN.

2. 

