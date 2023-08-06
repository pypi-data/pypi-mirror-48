**How to run the application to generate audios from Fidelity news**

*if run in debug model, will only tts three news*

*in Debug model, only first three news will tts to audios*

Development:

* Pipenv
    * ref
        * https://blog.csdn.net/weixin_33755847/article/details/91455072
        * https://www.jianshu.com/p/eb9ef9e4c61a
        * https://farer.org/2018/01/16/pipenv-notes/
        * https://www.kennethreitz.org/essays/a-better-pip-workflow

* 版本控制建议
    * 请在版本控制中保留 Pipfile 和 Pipfile.lock 文件
    * 如果目标是多个Python版本，则不要将 Pipfile 保存在版本控制系统中
    * 在 Pipfile 的 [require] 部分中指定目标Python版本。理想情况下，您应该只有一个目标Python版本，因为这是一个部署工具

* Pipenv工作流
    * export PIPENV_VENV_IN_PROJECT=1
        * 配置 PIPENV_VENV_IN_PROJECT 环境变量
    * pipenv install
        * 如果存在 Pipfile，则从中安装依赖项
        * 如果不存在 Pipfile 文件，上一条命令将会创建一个 Pipfile 文件
    * pipenv install <package>
        * 如果不存在 Pipfile 文件，上一条命令将会创建一个 Pipfile 文件
        * 如果 Pipfile 文件已经存在，则会使用上一条命令中指定的包自动编辑 Pipfile 文件
    * 激活 Pipenv shell
        * pipenv shell
        * python --version

* Pipenv升级工作流
    * pipenv update --outdated
        * 查看哪些依赖项已过期
    * pipenv update
        * 更新所有的依赖项
    * pipenv update <pkg>
        * 升级指定的包

* Pipenv
    * pipenv --python 3
    * pipenv --python 3.6
    * 对于没有使用pipenv的环境
        * pip
            * pip freeze > requirements.txt
            * pip install -r requirements-to-freeze.txt --upgrade
        * pipenv install -r path/to/requirements.txt --python 3.6
            * 从requirements.txt安装依赖
        * pipenv lock -r > requirements.txt
            * 生成与 pip 相同格式的依赖管理文件
    * 对于使用pipenv的环境
        * pipenv install
        * pipenv sync
            两者都会创建虚拟环境，使用指定的 PyPI 源按照依赖包，区别是 pipenv install 会根据 Pipfile 中的版本信息安装依赖包，
            并重新生成 Pipfile.lock；而 pipenv sync 会根据 Pipfile.lock 中的版本信息安装依赖包。


* install dev environment
    * pipenv install
    * pipenv install --dev
    * pipenv install --deploy
    * pipenv install --ignore-pipfile
    * pipenv install --skip-lock
    * pipenv install --system --dev
    * pipenv install --system --deploy
        * --system, 表示使用 pip 直接安装相应依赖，不创建虚拟环境。
        * --dev 安装Pipfile中 [default] 和 [devlop] 中的包
        * --deploy, 标志强制Pipfile.lock 文件是最新的
        * –ignore-pipfile 忽略 Pipfile 文件而直接安装 Pipfile.lock 中的包
        * –skip-lock 忽略 Pipfile.lock 文件而直接安装 Pipfile 中的包。此外，不会更新 Pipfile.lock 文件
    * pipenv sync
    * pipenv lock
        * 该命令用于创建 Pipfile.lock 文件，它声明项目的所有依赖项(和子依赖项)、依赖项的最新可用版本以及已下载文件的散列值。这确保了
        构建是可重复的，并且最重要的是确保了构建具有确定性

* export requirements.txt
    * pipenv lock -r > requirements.txt
    * pipenv run pip freeze

* .env
    * 如果你开发调试时需要配一堆环境变量，可以写到.env文件中，在pipenv shell进入虚拟环境时，它会帮你把这些环境变量加载好，非常方便。
        * echo HELLO=WORLD >> .env


* ref:
    * github
        * requests
        * flask
        * django
        * pipenv