Flask-PluginKit
===============

基于Flask的插件式开发工具(Web program plugin development kit based on flask).

*能耐一般水平有限，目前版本功能弱爆了，准备重构新版，不建议使用当前版本，因为你不熟悉代码实际用起来问题多多，文档还不全~~*

|Build Status| |Documentation Status| |codecov| |PyPI| |Pyversions| |Anti996|

使用概述(Overview)
-------------------

安装(Installation)

.. code:: bash

    # 正式版(Release)
    $ pip install -U Flask-PluginKit
    # 开发版(Dev)
    $ pip install -U git+https://github.com/staugur/Flask-PluginKit.git@master

测试用例(TestCase)

.. code:: bash

    $ make dev && make test

普通模式(Usage)

.. code:: python

    from flask_pluginkit import PluginManager
    plugin = PluginManager(app)

工厂模式(The factory pattern)

.. code:: python

    from flask_pluginkit import PluginManager
    plugin = PluginManager()
    plugin.init_app(app)

贡献(Contributing)
-------------------

有关设置开发环境以及如何为Flask-PluginKit做出贡献，请参阅 `contributing guidelines`_.

.. _contributing guidelines: https://github.com/staugur/Flask-PluginKit/blob/master/CONTRIBUTING.rst


资源(Resources)
-----------------

-  GitHub https://github.com/staugur/Flask-PluginKit
-  码云 https://gitee.com/staugur/Flask-PluginKit
-  Author https://www.saintic.com
-  Issues https://github.com/staugur/Flask-PluginKit/issues
-  使用 *Flask-PluginKit* 的项目 https://github.com/topics/flask-pluginkit
-  基于 *Flask-PluginKit* 的官方插件 https://github.com/flask-pluginkit

文档(Documentation)
---------------------

-  `中文 <https://flask-pluginkit.readthedocs.io/zh_CN/latest/>`__

-  `English <https://flask-pluginkit.readthedocs.io/en/latest/>`__

许可证(LICENSE)
----------------

`BSD LICENSE <http://flask.pocoo.org/docs/license/#flask-license>`__

说在后面(END)
---------------

欢迎提交PR、共同开发！

.. |Build Status| image:: https://travis-ci.com/staugur/Flask-PluginKit.svg?branch=master
   :target: https://travis-ci.com/staugur/Flask-PluginKit
.. |Documentation Status| image:: https://readthedocs.org/projects/flask-pluginkit/badge/?version=latest
   :target: https://flask-pluginkit.readthedocs.io/
.. |codecov| image:: https://codecov.io/gh/staugur/Flask-PluginKit/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/staugur/Flask-PluginKit
.. |PyPI| image:: https://img.shields.io/pypi/v/Flask-PluginKit.svg?style=popout
   :target: https://pypi.org/project/Flask-PluginKit/
.. |Pyversions| image:: https://img.shields.io/pypi/pyversions/flask-pluginkit.svg
   :target: https://pypi.org/project/Flask-PluginKit
.. |Anti996| image:: https://img.shields.io/badge/link-996.icu-red.svg
   :target: https://996.icu
   :alt: 996.ICU