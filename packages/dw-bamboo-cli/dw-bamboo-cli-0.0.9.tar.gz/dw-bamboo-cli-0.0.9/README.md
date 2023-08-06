# Bamboo Command Line Interface (CLI)

The Bamboo CLI allows users to modify pipeline parameters without the need to change any code or configuration files.

## Installation
`pip install dw-bamboo-cli`

## Example Usage

Assuming you have only one pipeline class per module you may now trigger the pipeline without an explicit entry function:

```
bamboo-cli --folder /my/bamboo/pipeline/folder --entry my_pipeline_module --param1=value1 --param2=value2
```


## Optional Entry Function
If you would like to have the ability to add custom logic between the pipeline class and the CLI, you may optionally specify an entry function. That could be called as:

```
bamboo-cli --folder /my/bamboo/pipeline/folder --entry my_pipeline_module.entry_func --param1=value1 --param2=value2
```

Note that the entry function should be supplied as `module_name`.`function_name`. And the function should follow the form of:

```python
def entry_func(params, **kwargs):
  # where params is a dictionary of key/values for the pipeline and MyPipeline is your customized
  # subclass of BasePipeline
  pipeline = MyPipeline()
  # ... apply custom transformations to params here for example ...
  pipeline.run(params)
```
