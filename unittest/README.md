## Components

### test fixture
A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
### test case
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
### test suite
A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
### test runner
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.


## Test case

*  a testcase is created by subclassing `unittest.TestCase`. The methods whose name start with the letters 'test' are the methods represent tests which will be run by test runner.

* The test method should use assert method provided by 'TestCase' base class. These assert method will raise a exception and unittest will identify the test case as a failure. Any other exception will be treated as errors.


## Test Fixture (Setup and tearDown)

repetitive set-up code can be factored out into `setUp` method and its corresponding clean up method is `tearDown`.
```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```

## Test suite

Test case  instances are grouped together according to the features they test. we can user `Test suite` to to this.

* unittest.main(): collect all the module's test cases for you, and then execute them.
* you can also customize the building of test suite:
  * todo: a example of test suite.

## Running TestSuite

### command line

```
python -m unittest unittest_example.py
```
