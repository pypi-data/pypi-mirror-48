## fbt ([See the dbt-presto docs](https://docs.getdbt.com/docs/profile-presto#section-required-configuration))

Forked from [dbt-presto](https://github.com/fishtown-analytics/dbt-presto) to more seamlessly work with custom build tools. You're probably looking for [dbt-presto](https://github.com/fishtown-analytics/dbt-presto) instead!

### Installation

This plugin can be installed via pip:

```
$ pip install fbt
```

### Configuring your profile

A dbt profile can be configured to run against Presto using the following configuration:

| Option  | Description                                        | Required?               | Example                  |
|---------|----------------------------------------------------|-------------------------|--------------------------|
| method  | The Presto authentication method to use | Optional(default=`none`)  | `none`|`kerberos` |
| database  | Specify the database to build models into | Required  | `analytics` |
| schema  | Specify the schema to build models into | Required | `dbt_drew` |
| host    | The hostname to connect to | Required | `127.0.0.1`  |
| port    | The port to connect to the host on | Required | `8080` |
| threads    | How many threads dbt should use | Optional(default=`1`) | `8` |



**Example profiles.yml entry:**
```
my-presto-db:
  target: dev
  outputs:
    dev:
      type: presto
      method: none
      host: 127.0.0.1
      port: 8080
      database: analytics
      schema: dbt_dbanin
      threads: 8
```

### Usage Notes

#### Supported Functionality
Due to the nature of Presto, not all core dbt functionality is supported.
The following features of dbt are not implemented on Presto:
- Archival
- Incremental models


If you are interested in helping to add support for this functionality in dbt on Presto, please [open an issue](https://github.com/fishtown-analytics/dbt-presto/issues/new)!

#### Required configuration
dbt fundamentally works by dropping and creating tables and views in databases.
As such, the following Presto configs must be set for dbt to work properly on Presto:

```
hive.metastore-cache-ttl=0s
hive.metastore-refresh-interval = 5s
hive.allow-drop-table=true
hive.allow-rename-table=true
```


### Reporting bugs and contributing code

-   Want to report a bug or request a feature? Let us know on [Slack](http://slack.getdbt.com/), or open [an issue](https://github.com/fishtown-analytics/dbt-spark/issues/new).

## Code of Conduct

Everyone interacting in the dbt project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).
