# airflow-testing

Code for testing Airflow DAGs.

## Initialise the Database

Before running Airflow, initialise the metastore. This step only needs to be
performed once.

``` bash
docker compose up airflow-init
```

## Running Airflow

Run in detached mode.

```bash
docker compose up -d
```

## Complete Cleanup

```bash
docker compose down --volumes --remove-orphans
```
