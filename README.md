# guid-server

인스타그램의 guid 작성 규칙을 구현한 간단한 guid-server 입니다.

## install

    $ pip install git+http://github.com/yoophi/guid-server.git

## run

`localhost:6379` 에 `redis-server` 실행되고 있어야 합니다.
	
    $ redis-server
    
함께 설치되는 `guid_server` 스크립트를 이용해 실행합니다.

    $ guid_server runserver
    
## sample request

    $ http :5000/guid
    HTTP/1.0 200 OK
    Content-Length: 52
    Content-Type: application/json
    Date: Wed, 30 Sep 2015 13:37:20 GMT
    Server: Werkzeug/0.10.4 Python/2.7.10

    {
        "guid": 12109964295484212795, 
        "shard_id": 1
    }

    $ http :5000/guid/100
    HTTP/1.0 200 OK
    Content-Length: 54
    Content-Type: application/json
    Date: Wed, 30 Sep 2015 13:37:47 GMT
    Server: Werkzeug/0.10.4 Python/2.7.10

    {
        "guid": 12109964522010284604, 
        "shard_id": 100
    }

