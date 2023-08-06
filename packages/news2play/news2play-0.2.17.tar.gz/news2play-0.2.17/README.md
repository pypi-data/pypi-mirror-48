#News To Play

##Index:
    0. python version >= 3.6
    1. How to setup dev environment
    2. How to use news2play package
    3. How to deploy

##How to setup dev/running environment

##### Command for init dev/running environment
```bash
make init
```

##How to use news2play package

##### Command for install news2play from PyPI
```bash
pip3 install news2play
```

##### Command for run news2play after installation.
```python
import news2play

news2play.app.run()
```

After the process finished, you can find the generated audios for news in ./storage/data

##### Command for run Docker from DockerHub
```bash
TBD
```

##How to deploy

##### Command for deploy to PyPI
```bash
make publish
```

##### Command for deploy to Dockerhub
```bash
TBD
```

##Backup

```bash
echo hello news2play
```
```python
print('hello news2play')
```
```javascript
```