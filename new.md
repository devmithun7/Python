# dbt Study Notes

These notes expand on the concepts you listed and show how outputs typically look.

## Base models and `ref()`

**Idea**: Create a clean, reusable “base” model (often in a `stg_` or `base_` layer) that other models can reference using `ref()`. This avoids hardcoding schema/table names and keeps lineage intact.

**Why it matters**
- `ref()` makes dependencies explicit, so dbt builds in the right order.
- `ref()` makes renames safe: dbt rewrites the schema/table at compile time.
- Lineage graphs and documentation stay accurate.

**Example**
```sql
-- models/base_orders.sql
select
  order_id,
  customer_id,
  order_ts,
  status
from {{ source('landing', 'orders') }}
```

```sql
-- models/fact_orders.sql
select
  o.order_id,
  o.customer_id,
  o.order_ts,
  o.status,
  p.payment_amount
from {{ ref('base_orders') }} o
left join {{ ref('fact_payments') }} p
  on o.order_id = p.order_id
```

**How the compiled SQL looks**
- dbt replaces `ref('base_orders')` with the fully qualified relation, e.g.:
  - `SLEEKMART_OMS.L2_PROCESSING.BASE_ORDERS`

## Materializations (views vs tables)

**Default**: Models are materialized as **views** unless you override.

**When to choose**
- **View**: light transformations, always live, no storage.
- **Table**: heavy transformations, faster downstream queries, uses storage.

**Project-level override**
```yaml
models:
  +materialized: view  # default
  oms_dbt_proj:
    facts:
      +materialized: table
```

**Output effect**
- `view` creates a database view pointing to the compiled SQL.
- `table` creates a physical table with the query result.

## Snowflake transient tables

**Snowflake default**: dbt creates **transient** tables (no fail-safe, lower cost).

**To make permanent tables**:
```yaml
models:
  +transient: false
```

**Output effect**
- `transient: true` -> `CREATE TRANSIENT TABLE ...`
- `transient: false` -> `CREATE TABLE ...`

## Seeds

**Definition**: CSV files stored in `seeds/` for static or slow-changing data (e.g., mappings, calendars).

**Usage**
- `dbt seed` loads CSVs as tables.
- Useful for lookup tables referenced by models.

**Output**
- A table named after the CSV file, e.g. `seeds/country_codes.csv` -> `COUNTRY_CODES`.

## Analyses

**Analyses folder**: `analyses/` SQL files are **not materialized** by dbt.
- Used for ad hoc queries or exploration.
- You can run the SQL directly in your warehouse or via `dbt compile` to render Jinja.

**Output**
- No table/view is created.
- SQL file is compiled into `target/compiled/` if you compile.

## Sources (avoid hardcoded schemas)

Hardcoding schema/table names becomes painful at scale. Use **sources** instead:

**Source definition (`models/src_oms.yml`)**
```yaml
version: 2

sources:
  - name: landing
    database: SLEEKMART_OMS
    schema: L1_LANDING
    tables:
      - name: cust
        identifier: customers
      - name: ordr
        identifier: orders
```

**Using the source**
```sql
select * from {{ source('landing', 'ordr') }}
```

**Output effect**
- dbt renders to `SLEEKMART_OMS.L1_LANDING.ORDERS`
- You can change the physical name in one file without editing all models.

## Source freshness (from your screenshot)

**Purpose**: Validate how “fresh” source data is, based on a timestamp column.

**Example**
```yaml
sources:
  - name: landing
    database: SLEEKMART_OMS
    schema: L1_LANDING
    freshness:
      warn_after: {count: 1, period: day}
      error_after: {count: 3, period: day}
    loaded_at_field: updated_at
    tables:
      - name: orders
```

**How to run**
- `dbt source freshness`

**Output effect**
- dbt calculates “age” from `loaded_at_field`.
- Logs show `pass`, `warn`, or `error` for each source table.

## dbt Tests

**Tests are SQL queries that return failing records.**
- If the query returns **0 rows**, the test **passes**.
- If it returns **>0 rows**, the test **fails** and shows counts.

### Singular tests
- Written as SQL in `tests/`.
- Hardcoded to a specific model/column.

```sql
-- tests/orders_have_valid_status.sql
select *
from {{ ref('fact_orders') }}
where status not in ('NEW', 'SHIPPED', 'CANCELLED')
```

### Generic tests
- Reusable, parameterized tests defined in YAML.
- dbt ships built-in generic tests: `unique`, `not_null`, `accepted_values`, `relationships`.
 - You can also create **custom generic tests** as macros and apply them in YAML.

**Example YAML (apply generic tests)**
```yaml
version: 2

models:
  - name: fact_orders
    columns:
      - name: order_id
        tests:
          - not_null
          - unique
      - name: status
        tests:
          - accepted_values:
              values: ['NEW', 'SHIPPED', 'CANCELLED']
      - name: customer_id
        tests:
          - relationships:
              to: ref('dim_customers')
              field: customer_id
```

**Output effect**
- dbt generates SQL behind the scenes for each test.
- Test results show passes/fails and failing row counts in logs.

## Where to define tests
- **Singular**: `tests/` folder.
- **Generic**: YAML in `models/` folders.

## YAML files in `models/`

You typically create a `schema.yml` (or any `*.yml`) in a model folder to:
- define **sources**
- apply **generic tests**
- add **descriptions** for models/columns

dbt reads all YAML files under `models/`.

## Typical dbt outputs to expect

**dbt run**
- Creates or updates views/tables according to materialization.
- Logs show `CREATE VIEW` or `CREATE TABLE` statements.

**dbt test**
- Logs each test with status.
- Failing tests list the number of failing rows.

**Where to check logs**
- CLI output in your terminal.
- Full logs in `logs/dbt.log` (useful for debugging test failures).

### Example `dbt test` terminal output

```text
13:42:01  Running with dbt=1.7.9
13:42:02  Found 12 models, 4 tests, 0 seeds, 0 sources, 0 exposures, 0 metrics
13:42:03
13:42:03  1 of 4 START test not_null_fact_orders_order_id .......... [RUN]
13:42:03  1 of 4 PASS not_null_fact_orders_order_id .................. [PASS in 0.32s]
13:42:03  2 of 4 START test unique_fact_orders_order_id .............. [RUN]
13:42:04  2 of 4 PASS unique_fact_orders_order_id ..................... [PASS in 0.41s]
13:42:04  3 of 4 START test accepted_values_fact_orders_status ........ [RUN]
13:42:05  3 of 4 FAIL accepted_values_fact_orders_status .............. [FAIL 12 in 0.38s]
13:42:05  4 of 4 START test relationships_fact_orders_customer_id ..... [RUN]
13:42:06  4 of 4 PASS relationships_fact_orders_customer_id ........... [PASS in 0.29s]
13:42:06
13:42:06  Finished running 4 tests in 0.00 minutes.
13:42:06
13:42:06  Completed with 1 error and 0 warnings:
13:42:06  Failure in test accepted_values_fact_orders_status (models/schema.yml)
13:42:06    Got 12 results, configured to fail if != 0
```

## dbt Docs

**What it is**
- dbt builds documentation that is **integrated with code**.
- It combines metadata from your **warehouse** (columns, types) and your **dbt model definitions** (YAML, tests, descriptions).

**Where descriptions live**
- In model YAML files (e.g., `models/schema.yml`) you can add descriptions for models and columns.
- The same approach works for source YAML files.

**Example: descriptions in model YAML**
```yaml
version: 2

models:
  - name: fact_orders
    description: "Fact table of orders with one row per order."
    columns:
      - name: order_id
        description: "Primary key for the order."
      - name: order_ts
        description: "Order timestamp in UTC."
```

**Example: descriptions in source YAML**
```yaml
version: 2

sources:
  - name: landing
    description: "Raw landing tables from OMS."
    tables:
      - name: orders
        description: "Raw orders from the OMS application."
        columns:
          - name: updated_at
            description: "Last update time from source system."
```

### Docs blocks in `.md` files

You can also create rich documentation blocks in Markdown files and reference them in YAML.

**Example doc block (`docs/orders.md`)**
```md
{% docs orders_long_description %}
This model is the canonical order fact table.

It includes:
- order status
- customer linkage
- payment summary
{% enddocs %}
```

**Reference the docs block in YAML**
```yaml
models:
  - name: fact_orders
    description: "{{ doc('orders_long_description') }}"
```

**Output effect**
- `dbt docs generate` builds searchable HTML docs.
- `dbt docs serve` opens a local docs site with lineage, tests, and descriptions.

## Jinja in dbt: building blocks

dbt uses Jinja to make SQL and YAML dynamic. The four main building blocks are:

### 1) Control statements (logic)
Use `{% ... %}` for control flow like `set`, `if`, and `for`.
```sql
{% set min_count = 100 %}
{% if target.name == 'prod' %}
  select * from {{ ref('fact_orders') }} where is_deleted = false
{% else %}
  select * from {{ ref('fact_orders') }}
{% endif %}
```

### 2) Expressions (values)
Use `{{ ... }}` to print values or call functions/macros.
```sql
select
  {{ current_timestamp() }} as run_ts,
  {{ var('region', 'US') }} as region
from {{ ref('dim_customers') }}
```

### 3) Plain text (SQL/YAML)
Everything outside Jinja tags is treated as literal text.
```sql
select * from {{ ref('fact_orders') }}
```

### 4) Comments
Use `{# ... #}` for Jinja-only comments (not sent to the warehouse).
```sql
{# This comment will not appear in compiled SQL #}
select * from {{ ref('fact_orders') }}
```

**Common dbt Jinja helpers**
- `ref('model_name')` and `source('source_name', 'table_name')`
- `var('name', default)` for project variables
- `env_var('NAME')` for environment variables
- `target` (active target profile), e.g., `target.name`

## Macros in dbt

**What is a macro?**
- A macro is a reusable Jinja function (stored in `macros/`) that returns SQL.
- It lets you standardize logic, avoid copy/paste, and keep models consistent.

**Why macros are used**
- Standardize transformations across many models.
- Add default behavior (e.g., default column names).
- Generate multiple models from similar logic.

### Example: standardization model + defaults

**Macro with default values (`macros/standardize.sql`)**
```sql
{% macro standardize_customer_data(relation, id_col='customer_id', ts_col='updated_at') %}
select
  {{ id_col }} as customer_id,
  lower(trim(first_name)) as first_name,
  lower(trim(last_name)) as last_name,
  cast({{ ts_col }} as timestamp) as updated_at
from {{ relation }}
{% endmacro %}
```

**Model using the macro (`models/stg_customers.sql`)**
```sql
{{ standardize_customer_data(source('landing', 'customers')) }}
```

**Model using non-default column names**
```sql
{{ standardize_customer_data(source('landing', 'cust'),
    id_col='cust_id',
    ts_col='last_modified') }}
```

**Output effect**
- Consistent, standardized columns across models.
- Defaults keep usage simple when column names match.

### Example: macro to create multiple models

You can generate several models by calling the same macro with different inputs.

**Macro (`macros/generate_profit_model.sql`)**
```sql
{% macro generate_profit_model(table_name) %}
select
  sales_date,
  sum(quantity_sold * unit_sell_price) as total_revenue,
  sum(quantity_sold * unit_purchase_cost) as total_cost,
  sum(quantity_sold * unit_sell_price) - sum(quantity_sold * unit_purchase_cost) as total_profit
from {{ source('training', table_name) }}
group by sales_date
{% endmacro %}
```

**Models that reuse the macro**
```sql
-- models/profit_us.sql
{{ generate_profit_model('sales_us') }}
```

```sql
-- models/profit_eu.sql
{{ generate_profit_model('sales_eu') }}
```

**Output effect**
- You get multiple models with the same logic, just different inputs.

## dbt Materializations (types with examples)

Materialization controls **how dbt builds a model** in your warehouse.

### 1) View
**What it is**: A logical layer. Query runs at read time.

**When to use**: Lightweight transformations, fast iteration.

**Example**
```sql
-- models/stg_orders.sql
{{ config(materialized='view') }}
select * from {{ source('landing', 'orders') }}
```

**Output effect**
- Creates a view (no extra storage).
- Downstream queries re-run the view SQL.

### 2) Table
**What it is**: A physical table created by running the model query.

**When to use**: Heavy logic or frequently queried models.

**Example**
```sql
-- models/fact_orders.sql
{{ config(materialized='table') }}
select ... from {{ ref('stg_orders') }}
```

**Output effect**
- `CREATE TABLE AS SELECT ...`
- Faster downstream queries, uses storage.

### 3) Incremental
**What it is**: Build only **new or changed** records after the first run.

**When to use**: Large tables where full refresh is expensive.

**Core idea**
- First run creates the table.
- Later runs insert or merge only new rows based on a **unique key** or filter.

**Example (append-only)**
```sql
-- models/fact_events.sql
{{ config(materialized='incremental') }}
select * from {{ source('landing', 'events') }}
{% if is_incremental() %}
  where event_ts > (select max(event_ts) from {{ this }})
{% endif %}
```

**Example (merge by key)**
```sql
-- models/dim_customers.sql
{{ config(materialized='incremental', unique_key='customer_id') }}
select * from {{ ref('stg_customers') }}
```

**Output effect**
- `is_incremental()` is true only on incremental runs.
- dbt issues inserts or merges depending on adapter.

### 4) Ephemeral
**What it is**: A model that **does not create** a table or view.
dbt inlines the SQL as a CTE into downstream models.

**When to use**: Small helper transformations, reduce clutter.

**Example**
```sql
-- models/ephemeral_helpers.sql
{{ config(materialized='ephemeral') }}
select
  order_id,
  case when status = 'C' then 'CANCELLED' else status end as status
from {{ ref('stg_orders') }}
```

**Output effect**
- No database object.
- Downstream compiled SQL includes this logic as a CTE.

### 5) Snapshots (special case, not a model materialization)
Snapshots track **slowly changing dimensions** over time.

**Example**
```sql
-- snapshots/customers_snapshot.sql
{% snapshot customers_snapshot %}
{{
  config(
    target_schema='snapshots',
    unique_key='customer_id',
    strategy='timestamp',
    updated_at='updated_at'
  )
}}
select * from {{ source('landing', 'customers') }}
{% endsnapshot %}
```

**Output effect**
- Creates a snapshot table with history columns like `dbt_valid_from`.

### Where to set materialization
- In model SQL with `{{ config(materialized='table') }}`.
- In `dbt_project.yml` for folders or model groups.

```yaml
models:
  oms_dbt_proj:
    staging:
      +materialized: view
    marts:
      +materialized: table
```

## Hooks (pre-hook and post-hook)

Hooks let you run SQL **before** or **after** a model, snapshot, or seed.

### Pre-hook
**Runs before the model SQL**.

**Use cases**
- Set session parameters
- Delete old partitions before loading

**Example**
```sql
{{ config(
    materialized='table',
    pre_hook="delete from {{ this }} where order_date < dateadd(day, -30, current_date)"
) }}
select * from {{ ref('stg_orders') }}
```

### Post-hook
**Runs after the model SQL**.

**Use cases**
- Grant permissions
- Insert audit records

**Example**
```sql
{{ config(
    materialized='table',
    post_hook="grant select on {{ this }} to role analytics_read"
) }}
select * from {{ ref('stg_orders') }}
```

### Project-level hooks
You can also define hooks in `dbt_project.yml`:
```yaml
models:
  oms_dbt_proj:
    +pre-hook: "alter session set query_tag = 'dbt_run'"
    +post-hook: "grant select on {{ this }} to role analytics_read"
```

**Output effect**
- Hooks appear in compiled SQL as separate statements.

If you want, send the next topic or more screenshots and I’ll expand these notes further.
