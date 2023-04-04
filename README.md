# Pants Airflow Minimal
## Step-by-step Guide to launch Airflow
### Step 1: Build the package and install it to `$HOME/airflow/bin/python`
``` bash
bin/install_airflow
```

### Step 2: Init and create the admin user
``` bash
bin/airflow_init
bin/airflow_create_admin # user: admin password: please input by yourself
```

When initializing, `bin/airflow_init` help you:
+ Set `core.dags_folder` to the PEX user code dynamically
+ Set `core.load_examples` to `False`

You can also reset the config via:
```
rm $HOME/airflow/airflow.cfg
$HOME/airflow/bin/python -m airflow_config
```

### Step 3: Launch the Airflow webserver and scheduler
Verify the first two steps by list the dags:
```
bin/airflow dags list
```

Launch the scheduler:
```
bin/airflow scheduler
```

Launch the webserver
```
bin/airflow webserver
```