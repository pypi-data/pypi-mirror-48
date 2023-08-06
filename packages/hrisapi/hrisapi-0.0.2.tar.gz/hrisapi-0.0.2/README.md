# hrisapi
Human Resource Information Systems API

## Installation
Clone the repository:
```
git clone https://github.com/deep-compute/hrisapi.git
```
Go to the local directory of the repository:
```
cd hrisapi
```
Install locally using:
```
pip install .
```

## Usage
Verify whether the tool is installed properly:
```
hrisapi --help
```

You should get something like this:
```
usage: hrisapi [-h] [--name NAME] [--log-level LOG_LEVEL]
               [--log-format {json,pretty}] [--log-file LOG_FILE] [--quiet]
               [--metric-grouping-interval METRIC_GROUPING_INTERVAL] [--debug]
               [--threadpool-size THREADPOOL_SIZE]
               [--cache-duration CACHE_DURATION]
               [--redis-password REDIS_PASSWORD] [--redis-loc REDIS_LOC]
               {schema,runserver,run} ...

Human Resource Information Systems API

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           Name to identify this instance
  --log-level LOG_LEVEL
                        Logging level as picked from the logging module
  --log-format {json,pretty}
                        Force the format of the logs. By default, if the
                        command is from a terminal, print colorful logs.
                        Otherwise print json.
  --log-file LOG_FILE   Writes logs to log file if specified, default: None
  --quiet               if true, does not print logs to stderr, default: False
  --metric-grouping-interval METRIC_GROUPING_INTERVAL
                        To group metrics based on time interval ex:10 i.e;(10
                        sec)
  --debug               To run the code in debug mode
  --threadpool-size THREADPOOL_SIZE
  --cache-duration CACHE_DURATION
  --redis-password REDIS_PASSWORD
  --redis-loc REDIS_LOC
                        host[:port[:db]] egs: localhost => localhost:6379:0
                        localhost:6379 => localhost:6379:0 :6379 =>
                        localhost:6379:0 ::0 => localhost:6379:0
                        localhost:6379:0 => localhost:6379:0 :: =>
                        localhost:6379:0

commands:
  {schema,runserver,run}
    schema              Show the Schema
    runserver           Run server
```

## Commands

### schema
Show the schema
```
hrisapi --log-file <filename.log> schema
```

### runserver
Run server

#### zoho
Run Zoho API interface
```
hrisapi --log-file <filename.log> --threadpool-size <size> --cache-duration <duration> --redis_password <password> --redis-loc https://example.com/ runserver --port <port> zoho
```

## Redis
To support redis authentication, create a redis.conf file. Inside the .conf file, add:
```
requirepass <password>
```

### Server
Start a redis server with a .conf file in command line:
```
redis-server <path/redis.conf>
```
or without specified .conf file:
```
redis-server
```

### Redis Command Line Interface
To launch the redis CLI, in a new terminal run:
```
redis-cli
```

If your redis server was configured with authentication, in the redis CLI run:
```
AUTH <password>
```


## GraphiQL
In your browser, navigate to:
```
http://localhost:PORT/graphiql
```
Where ```PORT``` is the ```<port>``` you passed when using the ```runserver``` command, or the default ```8888```

## GraphiQL Query Examples for Zoho API
Now you can test some GraphQL queries:

Employees Leaves
```
{
  employees(first: 2) {
    edges {
      node {
        name
        leaves {
          edges {
            node {
              type
              date
              duration
              status
            }
          }
        }
      }
    }
  }
}
```

Employees Holiday Schedule
```
{
  employees(first: 2) {
    edges {
      node {
        name
        holidaySchedule {
          name
          holidays {
            edges {
              node {
                name
                date
              }
            }
          }
        }
      }
    }
  }
}
```

Sorted List of Employees (currently does not respond to orderBy arguments however, it is sorted by descending order of joiningDate)
```
{
  employees(first: 5) {
    edges {
      node {
        name
        email
        timeZone
        joiningDate
      }
    }
  }
}
```

List of Work Locations
```
{
  workLocations {
    edges {
      node {
        name
        timeZone
      }
    }
  }
}
```

List of Leaves
```
{
  leaves(first: 5) {
    edges {
      node {
        employee {
          name
        }
        type
        date
        duration
        status
      }
    }
  }
}
```
