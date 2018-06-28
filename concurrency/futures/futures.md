The module provide 2 types of classes for interacting with the pools.

* Executors are used for managing pools of workers.

To use a pool of workers, an application creates an instance of the appropriate executor class and then submits tasks for it to run

* future are used for managing results computed by the workers.

When each task is started, a Future instance is returned. When the result of the task is needed, an application can use the Future to block until the result is availabl

