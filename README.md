# START

```
__pypath__=$(poetry env info --path 2> /dev/null); sed -i "" -r "s#__pypath__#${__pypath__/}#" .vscode/settings.json
```

# One-liner...

Description...

!!! Warnings / gotchas !!!


## Data prep

Preparatory steps:

| email | external_id | user_id | permissions | all_customers | subaccounts |
|-------|-------------|---------|-------------|---------------|-------------|
| john.ryan+test.user2@cloudinary.com | 21***14 | 66***44 | 32768 | True | ['jrdemo'] |
| john.ryan+test.user1@cloudinary.com | d9***6d | 66***42 | 32768 | False | ['jrdemo', 'jrbrandportal'] |


## Execution

Execution steps...

```
# env setup
poetry init

# user_data can be provided in any format supported by Pandas (csv, json, feather etc)
# @threads determines number of threads to execute in parallel (default = 1)
# @thread_delay introduces a terse delay per thread to throttle server requests (millisecs; default = 1000)

export AUTHENTICITY_TOKEN='c8Q1itwS...1QC461g='
export COOKIE_TOKEN='hblid=Kn...8a501734'
python update_user_accounts.py path/to/user_data.csv threads=2 thread_delay=1000
```


## Results

`debug.log` and `error.log` can be found under `logs/` directory

Each `user_data` record will be printed to the logs along with the corresponding HTTP response, both of which will be prefixed with the `user_id`. A successful request will yield a 302 response eg.

```
2022-04-23 00:00:46,421 : DEBUG : ...
```

An unsuccessful request will yield an Error message, eg.

```
2022-04-22 23:52:32,972 : DEBUG : ...
2022-04-22 23:52:48,139 : ERROR : [...] update_user_account: [XXXXXX] ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
```
