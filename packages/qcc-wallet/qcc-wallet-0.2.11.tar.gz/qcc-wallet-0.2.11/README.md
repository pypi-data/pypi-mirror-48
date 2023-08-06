
### Python支持版本：
支持python3.7及以上版本

#### Python3.7安装（ubuntu16.04)
- 1
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.7
```

- 2
```bash
sudo apt-get install python3-pip
```
注：如果运行报错`ImportError: cannot import name 'main'`，可以重新打开终端再试

- 3
```bash
pip3 install virtualenv
```

- 4
```bash
sudo apt-get install libpython3.7-dev
```

### 环境初始化：
```
sh create-venv.sh
. venv/bin/activate
pip install -r requirements.txt
```

### 运行：
```
. venv/bin/activate
python main.py --env=dev --logging=debug --log_file_prefix=log/fengcun.log
```
或者
```
后台运行：
./bootstrap.sh start
或者：
bash bootstrap.sh start

前台运行：
./bootstrap.sh run
或者：
bash bootstrap.sh run
```

### API文档
- [https://documenter.getpostman.com/view/5245402/S1ETRwW9](https://documenter.getpostman.com/view/5245402/S1ETRwW9)
