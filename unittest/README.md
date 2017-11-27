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

Test all testcase in a module
```
python -m unittest unittest_example.py
```

Test a particular testcase in a module

```
python -m unittest unittest_example.TestStringMethods
```

### hard code in module

```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
```

## Special test assertion

### Almost Equal 
In addition to strict equality, it's possible to test for near equality of floating point numbers.

```
import unittest


class AlmostEqualTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1.1, 3.3 - 2.2)

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3 - 2.2, places=1)

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 3.3 - 2.0, places=1)
```

### Containers 

In addition to the generic assertEqual() and assertNotEqual(), there are special methods for comparing containers like list, dict, and set objects

```
import textwrap
import unittest


class ContainerEqualityTest(unittest.TestCase):

    def testCount(self):
        self.assertCountEqual(
            [1, 2, 3, 2],
            [1, 3, 2, 3],
        )

    def testDict(self):
        self.assertDictEqual(
            {'a': 1, 'b': 2},
            {'a': 1, 'b': 3},
        )

    def testList(self):
        self.assertListEqual(
            [1, 2, 3],
            [1, 3, 2],
        )

    def testMultiLineString(self):
        self.assertMultiLineEqual(
            textwrap.dedent("""
            This string
            has more than one
            line.
            """),
            textwrap.dedent("""
            This string has
            more than two
            lines.
            """),
        )

    def testSequence(self):
        self.assertSequenceEqual(
            [1, 2, 3],
            [1, 3, 2],
        )

    def testSet(self):
        self.assertSetEqual(
            set([1, 2, 3]),
            set([1, 3, 2, 4]),
        )

    def testTuple(self):
        self.assertTupleEqual(
            (1, 'a'),
            (1, 'b'),
        )
```

### Testing for exceptions

As previously mentioned, if a test raises an exception other than AssertionError it is treated as an error. This is very useful for uncovering mistakes while modifying code that has existing test coverage. There are circumstances, however, in which the test should verify that some code does produce an exception. For example, if an invalid value is given to an attribute of an object. In such cases, assertRaises() makes the code more clear than trapping the exception in the test. Compare these two tests:

```
import unittest


def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))


class ExceptionTest(unittest.TestCase):

    def testTrapLocally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def testAssertRaises(self):
        self.assertRaises(
            ValueError,
            raises_error,
            'a',
            b='c',
        )
```

## Other Techniques

### Repeating Tests with different inputs

It is frequently useful to run the same test logic with different inputs. Rather than defining a separate test method for each small case, a common way of doing this is to use one test method containing several related assertion calls. The problem with this approach is that as soon as one assertion fails, the rest are skipped. A better solution is to use subTest() to create a context for a test within a test method. If the test fails, the failure is reported and the remaining tests continue.

```
import unittest


class SubTest(unittest.TestCase):

    def test_combined(self):
        self.assertRegex('abc', 'a')
        self.assertRegex('abc', 'B')
        # The next assertions are not verified!
        self.assertRegex('abc', 'c')
        self.assertRegex('abc', 'd')

    def test_with_subtest(self):
        for pat in ['a', 'B', 'c', 'd']:
            with self.subTest(pattern=pat):
                self.assertRegex('abc', pat)
```

### Skipping test

It is frequently useful to be able to skip a test if some external condition is not met. For example, when writing tests to check behavior of a library under a specific version of Python there is no reason to run those tests under other versions of Python. Test classes and methods can be decorated with skip() to always skip the tests. The decorators skipIf() and skipUnless() can be used to check a condition before skipping.

```
import sys
import unittest


class SkippingTest(unittest.TestCase):

    @unittest.skip('always skipped')
    def test(self):
        self.assertTrue(False)

    @unittest.skipIf(sys.version_info[0] > 2,
                     'only runs on python 2')
    def test_python2_only(self):
        self.assertTrue(False)

    @unittest.skipUnless(sys.platform == 'Darwin',
                         'only runs on macOS')
    def test_macos_only(self):
        self.assertTrue(True)

    def test_raise_skiptest(self):
        raise unittest.SkipTest('skipping via exception')
```

### Ignoring Failing Tests

Rather than deleting tests that are persistently broken, they can be marked with the expectedFailure() decorator so the failure is ignored.

```
import unittest


class Test(unittest.TestCase):

    @unittest.expectedFailure
    def test_never_passes(self):
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_always_passes(self):
        self.assertTrue(True)
```