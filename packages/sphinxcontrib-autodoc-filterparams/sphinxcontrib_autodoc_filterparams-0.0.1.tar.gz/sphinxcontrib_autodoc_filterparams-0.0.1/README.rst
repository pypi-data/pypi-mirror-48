##################################
sphinxcontrib-autodoc-filterparams
##################################

Although it might usually be a symptom of poor architecture, sometimes you
really want to exclude function parameters from your Sphinx documentation.

This extension does just that.


Usage
=====

- Add it to your **conf.py** extension list, typically immediately after the
  entry for :code:`sphinx.ext.autodoc`.
  If you use something like the :code:`napoleon` extension to re-format
  docstrings, then add it immediately after that.
- Declare a function called :code:`sphinxcontrib_autodoc_filterparams`.


Example
=======

The following would hide all parameters whose names starts with an underscore:

.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        'sphinxcontrib_autodoc_filterparams'
    ]

    def sphinxcontrib_autodoc_filterparams(fun, param):
        return not param.startswith('_')

The callback takes two arguments, the current function and parameter, and it
should return a boolean indicating whether or not to keep the parameter.

A slightly more elaborate example looks at the function context as well as the
name of the parameter:

.. code-block:: python

    exclude_params = {
        'my_package.my_module.MyClass.my_method': {'**kwargs'}
    }

    def sphinxcontrib_autodoc_filterparams(fun, param):
        exclude = exclude_params.get(fun.__module__ + '.' + fun.__qualname__)
        return exclude is None or param not in exclude


Options
=======

:code:`sphinxcontrib_autodoc_filterparams`
------------------------------------------

The callback function, invoked for each function parameter. If this function
returns :code:`True` then the parameter will be documented, otherwise it will
be excluded.

:code:`sphinxcontrib_autodoc_filterparams_stars`
------------------------------------------------

A boolean indicating whether or not asterisks should be prepended to parameter
names when invoking the callback (one star for variadic positional, two stars
for variadic keyword). Default is :code:`True`.