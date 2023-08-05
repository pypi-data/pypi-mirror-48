# -*- coding: utf-8 -*-
"""rackio/core.py

This module implements the core app class and methods for Rackio.
"""

import falcon
import concurrent.futures

from ._singleton import Singleton
from .logger import LoggerEngine
from .controls import ControlManager
from .workers import LoggerWorker, ControlWorker, APIWorker, _ContinousWorker
from .api import TagResource, TagCollectionResource, TagHistoryResource


class Rackio(Singleton):

    """Rackio main application class.

    This class is a singleton by inheritance, this makes
    it available in each module of an end application or
    code project

    # Example
    
    ```python
    >>> from rackio import Rackio
    >>> app = Rackio()
    ```

    """

    def __init__(self, context=None):

        super(Rackio, self).__init__()
        
        self._context = context

        self._worker_functions = list()
        self._continous_functions = list()
        self._control_manager = ControlManager()
        self._db_manager = None

        self._api = falcon.API()

        _tag = TagResource()
        _tags = TagCollectionResource()
        _tag_history = TagHistoryResource()

        self._api.add_route('/api/tags/{tag_id}', _tag)
        self._api.add_route('/api/tags', _tags)

        self._api.add_route('/api/tags/history/{tag_id}', _tag_history)

    def set_db(self, dbfile):
        """Sets the database file.
        
        # Parameters
        dbfile (str): a path to database file.
        """

        self._db_manager = LoggerEngine()
        self._db_manager.set_db(dbfile)

    def set_dbtags(self, tags):
        """Sets the database tags for logging.
        
        # Parameters
        tags (list): A list of the tags.
        """

        for _tag in  tags:
            self._db_manager.add_tag(_tag)

    def append_rule(self, rule):
        """Append a rule to the control manager.
        
        # Parameters
        rule (Rule): a rule object.
        """

        self._control_manager.append_rule(rule)

    def append_control(self, control):
        """Append a control to the control manager.
        
        # Parameters
        control (Control): a control object.
        """

        self._control_manager.append_control(control)

    def rackit(self, period):
        """Decorator method to register functions plugins.
        
        This method will register into the Rackio application
        a new function to be executed by the Thread Pool Executor

        # Example
    
        ```python
        @app.rackit
        def hello():
            print("Hello!!!")
        ```

        # Parameters
        period (float): Value of the default loop execution time.
        """

        def decorator(f):

            _worker_function = (f, period)
            self._worker_functions.append(_worker_function)
            return f
        
        return decorator

    def rackit_on(self, function=None, period=0.5, pause_tag=None, stop_tag=None):
        """Decorator method to register functions plugins with continous execution.
        
        This method will register into the Rackio application
        a new function to be executed by the Thread Pool Executor

        # Example
    
        ```python
        @app.rackit_on(period=0.5)
        def hello():
            print("Hello!!!")

        @app.rackit_on
        def hello_world():
            print("Hello World!!!")
        ```

        # Parameters
        period (float): Value of the default loop execution time, if period is not defined 0.5 seconds is used.
        """
    
        if function:
            return _ContinousWorker(function)
        else:
            def wrapper(function):
                return _ContinousWorker(function, period, pause_tag, stop_tag)

            return wrapper

    def run(self, port=8000):

        """Runs the main execution for the application to start serving.
        
        This will put all the components of the application at run

        # Example
    
        ```python
        >>> app.run()
        ```
        """

        _control_worker = ControlWorker(self._control_manager)
        _api_worker = APIWorker(self._api, port)

        if self._db_manager:
            self._db_manager._logger.set_db()
            _db_worker = LoggerWorker(self._db_manager)
            _db_worker.start()
        
        _control_worker.start()
        _api_worker.start()

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            
            for _f, period in self._worker_functions:

                executor.submit(_f)

            for _f in self._continous_functions:

                executor.submit(_f)

        _control_worker.join()
            