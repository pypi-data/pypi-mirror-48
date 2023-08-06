# Data Science WorkSpace (dsws)

DSWS is Python package providing conventions for configuration and use of existing python packages. Intent is to make disparate source data platforms consistanly accessible in python ad-hoc and workflow analyses independent of data source or REPL/RunTime environment.

## Main Features
DSWS offers no functionlity beyond what’s in dependency libraries. Instead, it provides conventions to consistantly and concisely use existing libraries. Conventions include:

 * Configurations for data access are instantiated at the beginning of a session, specific to analysis.
 * Configurations include not just source data connection, but also environement preferences in the connection, like default database and resource queue.
 * Common method syntax for connection and query.
 * For ipython environements, include line and cell magic for executing sql.
 * Consistant approach for profile startup scripts.
 * Ability to transition to configured CLI from within python session.

## Environments

DSWS originated to address connectivity complexity of connecting to popular hadoop distributions (HDP, CDH) from edge node. Since the original release, it now includes conventions to connect from cluster edge node virtual environement, local device virtual environement, cdsw, jupyter notebooks, or [quickstart](https://www.cloudera.com/downloads/quickstart_vms/5-13.html)/[sandbox](https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html). DSWS is intended to provide a consistant user experience within any of these evnironements.

## Included Libraries & CLIs

Exisiting libraries, classes, configs, and type.


| library / cli     | default name   | class              | type    | Incl    | Exp  | Roadmap |
|-------------------|----------------|--------------------|:-------:|:-------:|:----:|:-------:|
| [impyla](https://github.com/cloudera/impyla)            | impyla         | ws_impyla.py       | conn    | X       |      |         |
| (Hive) [beeline](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients#HiveServer2Clients-Beeline%E2%80%93CommandLineShell)    | hbl            | ws_hbl.py          | cli     | X       |      |         |
| [impala-shell](https://impala.apache.org/docs/build/html/topics/impala_impala_shell.html)      | imp            | ws_imp.py          | cli     | X       |      |         |
| [phoenixdb](https://github.com/lalinsky/python-phoenixdb)         | pheonix        | ws_pheonix.py      | conn    |         |      | X       |
| [hbase](http://hbase.apache.org/book.html#shell) (shell)     | hbase          | ws_hbase.py        | cli     |         |      | X       |
| [pyspark](https://github.com/apache/spark/tree/master/python/pyspark)             | spark (sql)    | ws_spark.py        | sess    | X       |      |         |
| [dask-yarn](http://yarn.dask.org)              | dask           | ws_dask.py         | sess    |         |      | X       |
| [pandasql](https://github.com/yhat/pandasql) | ps | ws_ps.py |         |         |      | X       |
| [ibis](https://github.com/ibis-project/ibis)              | ibis           | ws_ibis.py         | conn    | X         |      |        |
| [MySQL-python](https://pypi.org/project/MySQL-python/)            | mysql          | ws_mysql.py | conn | | | X |
| [pydruid](https://github.com/druid-io/pydruid) | druid | ws_druid.py | conn | | | X |
| [pyodbc](https://pypi.org/project/pyodbc/) | pyodbc | ws_druid.py | conn | X | | |
| [iopro](https://docs.anaconda.com/iopro/) | iopro | ws_iopro.py | conn | X | | |
