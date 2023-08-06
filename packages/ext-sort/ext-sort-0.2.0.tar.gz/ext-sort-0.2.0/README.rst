=============
External sort
=============

.. image:: https://travis-ci.org/dapper91/python-external-sort.svg?branch=master
    :target: https://travis-ci.org/dapper91/python-external-sort
    :alt: Build status
.. image:: https://img.shields.io/pypi/l/ext-sort.svg
    :target: https://pypi.org/project/ext-sort
    :alt: License
.. image:: https://img.shields.io/pypi/pyversions/ext-sort.svg
    :target: https://pypi.org/project/ext-sort
    :alt: Supported Python versions


External sort algorithm implementation. External sorting is a class of sorting algorithms that can handle massive
amounts of data. External sorting is required when the data being sorted do not fit into the main memory (RAM) of a
computer and instead must be resided in slower external memory, usually a hard disk drive.
Sorting is achieved in two passes. During the first pass it sorts chunks of data that each fit in RAM,
during the second pass it merges the sorted chunks together.
For more information see https://en.wikipedia.org/wiki/External_sorting.


Compatibility
=============

ext-sort requires 3.6+.


Installation
============

You can install ext-sort with pip:

.. code-block:: console

    $ pip install ext-sort


Quick start
===========

Quick start.

.. code-block:: python

    import csv
    import io
    import logging

    import ext_sort as es


    class CSVSerializer(es.Serializer):

        def __init__(self, writer):
            super().__init__(csv.writer(io.TextIOWrapper(writer, write_through=True)))

        def write(self, item):
            return self._writer.writerow(item)


    class CSVDeserializer(es.Deserializer):

        def __init__(self, reader):
            super().__init__(csv.reader(io.TextIOWrapper(reader)))

        def read(self):
            return next(self._reader)


    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)-8s] %(asctime)-15s (%(name)s): %(message)s',
    )

    with open('/home/user/data.csv', 'rb') as unsorted_file, open('/home/user/data.sorted.csv', 'wb') as sorted_file:
        # save the csv header
        sorted_file.write(unsorted_file.readline())

        es.sort(
            reader=unsorted_file,
            writer=sorted_file,
            chunk_size=10_000_000,
            Serializer=CSVSerializer,
            Deserializer=CSVDeserializer,
            workers_cnt=4,
        )

