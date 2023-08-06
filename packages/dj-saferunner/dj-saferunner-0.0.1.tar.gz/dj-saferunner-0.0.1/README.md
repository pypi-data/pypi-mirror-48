> A mechanism for running processes which might have side effects (e.g.: calling an external API etc.) in a way that is safe by default during testing and provides useful introspection functionality.

It will: Run a list of tasks. If possible, it will run them asyncronously

In TEST_MODE:

* It will not run the code
* It will store information about the calls made in


## Usage

### In your code:

**before**

```python
from myapp.tasks import ping_google
ping_google(url='http://foo.com')
```

**after**

```python
from myapp.tasks import ping_google
from saferunner.process_runner import safely_run_processes
task_list = [
    # task, args, async
    (ping_google, {"url", "http://foo.com"}, False)
]
safely_run_processes(
    run_id='identifier giving some context about where this is run',
    task_list=task_list
)
```

### In your tests

When in test mode, by default the saferunner will not execute your code. Instead it will log your calls using django's cache

**example test**

```python
def test_run_some_tasks(self):
    clear_run_cache()
    run_id = 'this_is_a_test'
    task_list = [
        (hello, {"msg": "hi"} , False),
        (do_something_slowly, {"sleep": 10}, True),
    ]
    safely_run_processes(
        run_id = run_id,
        task_list = task_list
    )
    res = get_process_run(run_id)
```

The results of `get_process_run` would look something like this:

```
[{
	'task_name': 'hello',
	'task_args': "OrderedDict([('msg', 'hi')])",
	'is_async': False
}, {
	'task_name': 'do_something_slowly',
	'task_args': "OrderedDict([('sleep', 10)])",
	'is_async': True
}]
```

#### Explicitly running side effect code

> In your tests, You can force `saferunner` to execute safely run code.

You might want to do this, for example, if you want to test code inside your function from a higher level.
Ideally you should not really need to do this too often. We would recommend that it is preferred to test your
functions by calling them directly (as opposed to checking for side effects in a higher level function)

**Run all side effect code:**

Will essentially turn `saferunner` off for this test

```
@override_settings(FORCE_RUN_SIDE_EFFECTS='__all__')
```

**You can also specify a specific task to pass through:**

This will force `saferunner` to explicitly run this exact function/method

```
@override_settings(FORCE_RUN_SIDE_EFFECTS=task.name)
@override_settings(FORCE_RUN_SIDE_EFFECTS=task.__name__)
```


## FAQ:

Q: Why not just use mocks?
A:
The use-case for this is for code that might get executed often
(for example code in signals), and which might have unwanted
side-effects if accidentally run durung tests (e.g.: send SMSes or making API calls).
We want to err on the side of caution here and mock by default during testing
and be explicit about when we want to run this code

PS: DHH would probably call this test induced damage!

## TODO

* Make it work Class methods