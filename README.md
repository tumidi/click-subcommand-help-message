```
$ poetry install
$ poetry shell
$ click-test-cli foo
Usage: click-test-cli foo [OPTIONS] REQUIRED_ARG
Try 'click-test-cli foo -h' for help.

Error: Missing argument 'REQUIRED_ARG'.
```

But, actually running the suggested `click-test-cli foo -h` yields

```
$ click-test-cli foo -h
Error: Option '-h' requires an argument.
```
