# Solution

1. upload sample.tar
2. get id of sample.tar from `/results/<archive_id>`. Suppose id is XXX.
3. craft evil.tar containing following entries
  - pardir2 -> ../.. (Symbolic link)
  - pardir2/XXX/result.json -> /app/flag.txt (Symbolic link)
  tar.extractall supports symbolic link, so just checking member.name is not enough.
4. request `/results/XXX` to get flag

create_archive.py is my tar/zip slip tool.
