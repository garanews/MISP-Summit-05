' MAIN NODE '
[dask@scheduler]# dask-scheduler --interface eth1 --port 8786 &
[dask@scheduler]# dask-worker scheduler:8786 --interface eth1 --nprocs 20 --nthreads 1 &

' WORKER NODE 1 '
[dask@worker1]# dask-worker scheduler:8786 --interface eth1 --nprocs 16 --nthreads 1 &

' WORKER NODE 2 '
[dask@worker2]# dask-worker scheduler:8786 --interface eth1 --nprocs 16 --nthreads 1 &

' MAIN NODE '
[dask@scheduler]# python run_ruzicka.py
