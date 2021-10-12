# Tools

## sql_utils
Provides uility functions to run multi-line sql in Python environment.

### Run from string
```python
from afterpay_gdp_interfaces import RedshiftHook

r = RedshiftHook(cluster='vega', okta_username='john.doe@afterpay.com')
df = sql_from_str(r, 'select * from green.cur_c_m_order_master limit 1;')
```

### Run from script file
```python
from afterpay_gdp_interfaces import RedshiftHook

r = RedshiftHook(cluster='vega', okta_username='john.doe@afterpay.com')
df = sql_from_str(r, 'script.sql')
```

The content in ``script.sql`` is as follows:
```sql
select 
    * 
from 
green.cur_c_m_order_master 
limit 1
;

select
    count(*) cnt
from 
green.cur_c_m_order_master 
;
```

Note that special treatment is needed when comments are added to sql file (due to limitation of ``RedshiftHook``):
* block comments SHOULD be ended with semicolon ``;``;
* inline comments SHOULD NOT be contain any semicolon ``;``;

Any violation would result in incorrect outputs or even errors.

In addition, since ``RedshiftHook`` automatically closes connection once a line of script is executed, one should create persistent table for further usage.
