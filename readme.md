
step 1 : build container

```powershell
docker-compose up
```


step 2 : test

```python
from workers.tasks.task_1 import add
add.delay(1,1).get()
```