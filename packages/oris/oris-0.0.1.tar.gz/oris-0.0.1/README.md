# ORIS for Python

This is a library for the analysis of discrete-event models governed
by *integer variables* and *continuous timers*:

- **Variables** hold positive or negative integers. They represent the
  *observable state* of the system. For example, the variable `queue`
  could store the current number of customers.

- **Timers** track the continuous time to events that change state
  variables:

    - A timer is enabled if its *guard* is satisfied. In the queue
      example, the `service` timer is enabled when `queue > 0`.

    - The value of the timer is sampled according to a probability
      distribution; for example, `Unif(1, 2)` samples a random value
      between 1 and 2.

    - When the timer elapses, it can trigger a change in the state
      variables, for example, `queue = queue-1` after `service`. This
      change can start other timers (because their guards are now
      satisfied) or disable them (the guards are not satisfied
      anymore).

The example of a single-server queue with capacity of 200, Poisson
arrivals (exponential interarrival times) and uniform service times
looks like this:

``` python
from oris import *

b = ModelBuilder()

# for each variable: name, initial value, min, max (defaults: 0, 0, 'inf')
b.var('queue', 1, 0, 200)

# for each timer: name, guard, distribution, state update
b.timer('arrival', 'True',    Exp(0.5),   'queue=min(queue+1, max_value(queue))')
b.timer('service', 'queue>0', Unif(1, 2), 'queue-=1')

m = b.build()
```

Once you have a model, you can
- analyze its state space (e.g., can you reach a goal state within time 10?)
- use simulation to evaluate rewards (e.g., average number of customers in the queue)

Learn more in the [manual](https://www.oris-tool.org/python).


## How to Install

To install ORIS: `pip3.7 install oris --user --upgrade` (you need Python 3.7)

To have a working Python 3.7 environment on Linux, macOS, or Windows,
we recommend using [miniconda](https://docs.conda.io/en/latest/miniconda.html) and Jupyter notebooks:

- Linux and macOS

  ``` bash
  curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/.miniconda
  $HOME/.miniconda/condabin/conda init bash
  bash
  ```

  For macOS, replace `Linux` with `MacOSX` in the first two commands.
  If you are using macOS Catalina, replace `bash` with `zsh`.

- Windows: run the [miniconda installer](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) selecting "Add Anaconda to
  my PATH".

Now you can create an environment for ORIS:

```
conda config --set auto_activate_base false
conda create -y -n oris python=3.7 scipy matplotlib numba jupyter
conda activate oris
pip install oris
```

Every time you want to use ORIS, you can run:

```
conda activate oris
jupyter notebook
```

**If you'd like to avoid installing anything at all:** Just use ORIS
inside [Google Colaboratory](https://colab.research.google.com). The only thing you need is:

``` python
!pip3 install oris
```

at the beginning of your notebook.
