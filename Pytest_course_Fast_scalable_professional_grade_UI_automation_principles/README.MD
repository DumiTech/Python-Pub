# How to run commands on CLI:

#run a particular mark:
`pytest -m smoke`

`pytest -m "body or engine"`
`pytest -m "not engine" -v`
`pytest -m "backend not UI`"

#too see markers:
`pytest --markers`

#to see the prints:
`pytest -s`

#to use the customized test run
`pytest --env dev -v`

#fast testing with Pytest-xdist, n representing the number of threads
`pytest -s -v -n4`
*If your test is not isolated(dependencies on other tests or database state) you not gonna want ot use this method. If you got multiple tests running in the same time they are interfering with the same memory, and that's gonna be a big problem (eg: a class that share some data).*


# INFO
pytest.ini => handles the text searching patterns and handles the markers 

## Threads are concurrent 
## Processes are concurrent and parallel

*Concurrent testing is what you get with threads. Multithreading, you can use threading library and python. If you set a very high number of jobs in your pytest xdist you will actually use threads not processes because you don't have enough logical CPU's to handle those processes. So you will get threads.*