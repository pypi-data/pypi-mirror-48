*Changes in master, but not released yet are under the draft section*.

vDRAFT (2019-05-23)
-------------------


Bugfixes
^^^^^^^^

- Turns out the output of the ``py -0p`` is not stable yet and varies depending on various edge cases. Instead now we read the interpreter values directly from registry via `PEP-514 <https://www.python.org/dev/peps/pep-0514>`_ - by :user:`gaborbernat`.
  `#1306 <https://github.com/tox-dev/tox/issues/1306>`_

