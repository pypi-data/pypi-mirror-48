A wrapper for PySFTP.

###Features

* Built around PySFTP.

* Grab NEW files from a remote directory using `get_new_files()`.

   Most of the time, I want to get all of the files from the `remote_directory` that I do not already have in my `local_directory`.  This method makes me very happy.

* When putting a file in a remote directory, `confirm=True` performs a stat on the remote file.

   This can help provide warm fuzzies, but shouldn't be used when the remote server immediately removes the file from the remote directory.  This will result in an error, because there will be no file to stat.

* You never have to adjust `pysftp.CnOpts` to `hostkeys=None` again!

   I am constantly getting files from remote SFTP servers that I don't already have the key for.  Maybe, someday, I'll make this feature optional.

###Connect to the remote SFTP server

```python
from cheesefactory-sftp import SFTP

sftp = SFTP(
    host='mysftp.example.com',
    port='22',
    username='testuser',
    password='testpass',
)
```

`hostname` (str): remote server.  Default = `127.0.0.1`

`port` (str): SFTP TCP port.  Default = `'22'`

`username` (str): SFTP username

`password` (str): SFTP password


###Get a file from the server

```python
sftp.get(
    remote_directory='/stuff',
    filename='myfile.txt',
    local_path='/tmp/'
)
```

`remote_directory` (str): Directory to retrieve file from on remote server.  Default = `'/'`

`filename` (str): The name of the file to download.

`local_path` (str):  The local directory and filename to copy to--the destination file.

###Put a file on the server

```python
sftp.put(
    remote_directory = '/stuff',
    filename = 'myfile.txt',
    confirm=True
)
```

`remote_directory` (str):  Directory on remote server to place the uploaded file.

`filename` (str):  The name of the file to upload.

`confirm` (bool):  Whether or not to stat the file once uploaded.

###Get new files from remote directory

```python
sftp.get_new_files(
    remote_directory = '/remote_stuff',
    local_directory = '/local_stuff'
)
```

`remote_directory` (str): Directory on remote server to find new files in.

`local_directory` (str):  Directory on local machine to put new files in.  The contents of both remote and local directories are compared and only files that are present remotely and not locally are moved.
