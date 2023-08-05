# Fcopy

Fcopy is a command line tool (CLI) utility to copy/update several files from different source locations to different target locations.


## Useful for?

Maybe you are building some sort of a library, dependency or utility that is required by several projects you are working on.

It's hard to updated them one by one everytime you build your library again and again by copying it. It's tedious!

fcopy let's you do this repetitive task with one small command.


## How it works

Fcopy reads the configuration from a json file previously specified. The json file or "task file" has the following structure:

```json
[
    {
        "name": "task-1",
        "group": "group-1",
        "source-path": "/path/of/file(s)",
        "target-path": "/destination/folder",
        "files": [{ 
                "name": "file-1.txt", 
                "as": "dest-1/file-1.min.txt" 
            },{ 
                "name": "file-1.txt", 
                "as": "dest-2/compiled.txt" 
            },{ 
                "name": "build/file-2.txt", 
                "as": "dest-3/file-2.txt" 
        }]
    },
    { ... }
]
```

The file contains a list of tasks. Each task has the following properties:

#### name
The name of the task. fcopy will execute the given task names with the option `-t`

```bash
fcopy -t task-1, task-2
```

This will execute only the tasks named "task-1" and "task-2"


#### group
The group of the task. Many task may belong to the same group. By specifying the group, fcopy will execute every task that belongs to that group

```bash
fcopy -t group-1
```

Many groups can be specified

#### source-path and target-path

These are the base path for the source files and destination files respectively. Maybe most of the files are under the same (or a generic) path. So it is easier to specify it only once.

#### files
Is a list of files where each file configuration has the name (just as it is in the file system) and the property "as" which specifies where and under which name is going to be copied. 


## Watching the file
To avoid executing the fcopy command everytime, we can start it with `-w` and it will keep watching the specified tasks (or group of tasks) for changes. It will automatically update only the file or files that have changed within the watched tasks. 


```bash
fcopy -t task-1 -w
```

## Updating the configuration

The configuration has to be specified only the first time or if we changed the location of the json file.

```bash
fcopy -c /path/to/conf.json
```


